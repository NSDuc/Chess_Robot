import numpy as np

def CircularHough_Grd(img=None,radrange=None,varargin=None,*args,**kwargs):
    varargin = CircularHough_Grd.varargin
    nargin = CircularHough_Grd.nargin

    if ndims(img) != 2 or logical_not(isnumeric(img)):
        error('CircularHough_Grd: 'img' has to be 2 dimensional')
    
    if logical_not(all(size(img) >= 32)):
        error('CircularHough_Grd: 'img' has to be larger than 32-by-32')
    
    if numel(radrange) != 2 or logical_not(isnumeric(radrange)):
        error(concat(['CircularHough_Grd: 'radrange' has to be ','a two-element vector']))
    
    prm_r_range=sort(max(concat([[0,0],[radrange(1),radrange(2)]])))
    prm_grdthres=10
    prm_fltrLM_R=8
    prm_multirad=0.5
    func_compu_cen=copy(true)
    func_compu_radii=copy(true)
    vap_grdthres=1
    if nargin > (1 + vap_grdthres):
        if isnumeric(varargin[vap_grdthres]) and varargin[vap_grdthres](1) >= 0:
            prm_grdthres=varargin[vap_grdthres](1)
        else:
            error(concat(['CircularHough_Grd: 'grdthres' has to be ','a non-negative number']))
    
    vap_fltr4LM=2
    if nargin > (1 + vap_fltr4LM):
        if isnumeric(varargin[vap_fltr4LM]) and varargin[vap_fltr4LM](1) >= 3:
            prm_fltrLM_R=varargin[vap_fltr4LM](1)
        else:
            error(concat(['CircularHough_Grd: 'fltr4LM_R' has to be ','larger than or equal to 3']))
    
    vap_multirad=3
    if nargin > (1 + vap_multirad):
        if isnumeric(varargin[vap_multirad]) and varargin[vap_multirad](1) >= 0.1 and varargin[vap_multirad](1) <= 1:
            prm_multirad=varargin[vap_multirad](1)
        else:
            error(concat(['CircularHough_Grd: 'multirad' has to be ','within the range [0.1, 1]']))
    
    vap_fltr4accum=4
    
    if nargin > (1 + vap_fltr4accum):
        if isnumeric(varargin[vap_fltr4accum]) and ndims(varargin[vap_fltr4accum]) == 2 and all(size(varargin[vap_fltr4accum]) >= 3):
            fltr4accum=varargin[vap_fltr4accum]
        else:
            error(concat(['CircularHough_Grd: 'fltr4accum' has to be ','a 2-D matrix with a minimum size of 3-by-3']))
    else:
        # Default filter (5-by-5)
        fltr4accum=ones(5,5)
        fltr4accum[arange(2,4),arange(2,4)]=2
        fltr4accum[3,3]=6
    
    func_compu_cen=(nargout > 1)
    func_compu_radii=(nargout > 2)
    # Reserved parameters
    dbg_on=copy(false)
    
    dbg_bfigno=4
    if nargout > 3:
        dbg_on=copy(true)
    
    ######## Building accumulation array ################################
    
    # Convert the image to single if it is not of
    img_is_double=isa(img,'double')
    if logical_not((img_is_double or isa(img,'single'))):
        imgf=single(img)
    
    if img_is_double:
        grdx,grdy=gradient(img,nargout=2)
    else:
        grdx,grdy=gradient(imgf,nargout=2)
    
    grdmag=sqrt(grdx ** 2 + grdy ** 2)
    # Get the linear indices, as well as the subscripts, of the pixels
    # whose gradient magnitudes are larger than the given threshold
    grdmasklin=find(grdmag > prm_grdthres)

    grdmask_IdxI,grdmask_IdxJ=ind2sub(size(grdmag),grdmasklin,nargout=2)

    # Compute the linear indices (as well as the subscripts) of
    # all the votings to the accumulation array.
    # The Matlab function 'accumarray' accepts only double variable,
    # so all indices are forced into double at this point.
    # A row in matrix 'lin2accum_aJ' contains the J indices (into the
    # accumulation array) of all the votings that are introduced by a
    # same pixel in the image. Similarly with matrix 'lin2accum_aI'.
    rr_4linaccum=double(prm_r_range)
    linaccum_dr=concat([arange((- rr_4linaccum(2) + 0.5),- rr_4linaccum(1)),arange((rr_4linaccum(1) + 0.5),rr_4linaccum(2))])
    lin2accum_aJ=floor(dot(double(grdx(grdmasklin) / grdmag(grdmasklin)),linaccum_dr) + repmat(double(grdmask_IdxJ) + 0.5,concat([1,length(linaccum_dr)])))
    lin2accum_aI=floor(dot(double(grdy(grdmasklin) / grdmag(grdmasklin)),linaccum_dr) + repmat(double(grdmask_IdxI) + 0.5,concat([1,length(linaccum_dr)])))
    mask_valid_aJaI=lin2accum_aJ > logical_and(0,lin2accum_aJ) < logical_and((size(grdmag,2) + 1),lin2accum_aI) > logical_and(0,lin2accum_aI) < (size(grdmag,1) + 1)
    mask_valid_aJaI_reverse=logical_not(mask_valid_aJaI)
    lin2accum_aJ=multiply(lin2accum_aJ,mask_valid_aJaI) + mask_valid_aJaI_reverse
    lin2accum_aI=multiply(lin2accum_aI,mask_valid_aJaI) + mask_valid_aJaI_reverse
    clear('mask_valid_aJaI_reverse')
    # Linear indices (of the votings) into the accumulation array
    lin2accum=sub2ind(size(grdmag),lin2accum_aI,lin2accum_aJ)
    lin2accum_size=size(lin2accum)
    lin2accum=reshape(lin2accum,concat([numel(lin2accum),1]))
    clear('lin2accum_aI','lin2accum_aJ')
    # Weights of the votings, currently using the gradient maginitudes
    # but in fact any scheme can be used (application dependent)
    weight4accum=multiply(repmat(double(grdmag(grdmasklin)),concat([lin2accum_size(2),1])),ravel(mask_valid_aJaI))
    clear('mask_valid_aJaI')
    # Build the accumulation array using Matlab function 'accumarray'
    accum=accumarray(lin2accum,weight4accum)
    accum=concat([[accum],[zeros(numel(grdmag) - numel(accum),1)]])
    accum=reshape(accum,size(grdmag))
    ######## Locating local maxima in the accumulation array ############
    
    # Stop if no need to locate the center positions of circles
    if logical_not(func_compu_cen):
        return accum,varargout
    
    clear('lin2accum','weight4accum')
    # Parameters to locate the local maxima in the accumulation array
# -- Segmentation of 'accum' before locating LM
    prm_useaoi=copy(true)
    prm_aoithres_s=2
    prm_aoiminsize=floor(min(concat([dot(min(size(accum)),0.25),dot(prm_r_range(2),1.5)])))
    # -- Filter for searching for local maxima
    prm_fltrLM_s=1.35
    prm_fltrLM_r=ceil(dot(prm_fltrLM_R,0.6))
    prm_fltrLM_npix=max(concat([6,ceil((prm_fltrLM_R / 2) ** 1.8)]))
    # -- Lower bound of the intensity of local maxima
    prm_LM_LoBndRa=0.2
    
    # Smooth the accumulation array
    fltr4accum=fltr4accum / sum(ravel(fltr4accum))
    accum=filter2(fltr4accum,accum)
    # Select a number of Areas-Of-Interest from the accumulation array
    if prm_useaoi:
        prm_llm_thres1=dot(prm_grdthres,prm_aoithres_s)
        accummask=(accum > prm_llm_thres1)
        accumlabel,accum_nRgn=bwlabel(accummask,8,nargout=2)
        accumAOI=ones(0,4)
        for k in arange(1,accum_nRgn).reshape(-1):
            accumrgn_lin=find(accumlabel == k)
            accumrgn_IdxI,accumrgn_IdxJ=ind2sub(size(accumlabel),accumrgn_lin,nargout=2)
            rgn_top=min(accumrgn_IdxI)
            rgn_bottom=max(accumrgn_IdxI)
            rgn_left=min(accumrgn_IdxJ)
            rgn_right=max(accumrgn_IdxJ)
            if ((rgn_right - rgn_left + 1) >= prm_aoiminsize and (rgn_bottom - rgn_top + 1) >= prm_aoiminsize):
                accumAOI=concat([[accumAOI],[rgn_top,rgn_bottom,rgn_left,rgn_right]])
    else:
        # Whole accumulation array as the one AOI
        accumAOI=concat([1,size(accum,1),1,size(accum,2)])
    
    # Thresholding of 'accum' by a lower bound
    prm_LM_LoBnd=dot(max(ravel(accum)),prm_LM_LoBndRa)
    # Build the filter for searching for local maxima
    fltr4LM=zeros(dot(2,prm_fltrLM_R) + 1)
    mesh4fLM_x,mesh4fLM_y=meshgrid(arange(- prm_fltrLM_R,prm_fltrLM_R),nargout=2)
    mesh4fLM_r=sqrt(mesh4fLM_x ** 2 + mesh4fLM_y ** 2)
    fltr4LM_mask=(mesh4fLM_r > logical_and(prm_fltrLM_r,mesh4fLM_r) <= prm_fltrLM_R)
    fltr4LM=fltr4LM - dot(fltr4LM_mask,(prm_fltrLM_s / sum(ravel(fltr4LM_mask))))
    if prm_fltrLM_R >= 4:
        fltr4LM_mask=(mesh4fLM_r < (prm_fltrLM_r - 1))
    else:
        fltr4LM_mask=(mesh4fLM_r < prm_fltrLM_r)
    
    fltr4LM=fltr4LM + fltr4LM_mask / sum(ravel(fltr4LM_mask))
    # **** Debug code (begin)
    if dbg_on:
        dbg_LMmask=zeros(size(accum))
    
    # **** Debug code (end)
    
    # For each of the AOIs selected, locate the local maxima
    circen=zeros(0,2)
    for k in arange(1,size(accumAOI,1)).reshape(-1):
        aoi=accumAOI(k,arange())
        # Thresholding of 'accum' by a lower bound
        accumaoi_LBMask=(accum(arange(aoi(1),aoi(2)),arange(aoi(3),aoi(4))) > prm_LM_LoBnd)
        candLM=conv2(accum(arange(aoi(1),aoi(2)),arange(aoi(3),aoi(4))),fltr4LM,'same')
        candLM_mask=(candLM > 0)
        candLM_mask[concat([arange(1,prm_fltrLM_R),arange((end() - prm_fltrLM_R + 1),end())]),arange()]=0
        candLM_mask[arange(),concat([arange(1,prm_fltrLM_R),arange((end() - prm_fltrLM_R + 1),end())])]=0
        if dbg_on:
            dbg_LMmask[arange(aoi(1),aoi(2)),arange(aoi(3),aoi(4))]=dbg_LMmask(arange(aoi(1),aoi(2)),arange(aoi(3),aoi(4))) + accumaoi_LBMask + dot(2,candLM_mask)
        # **** Debug code (end)
        # Group the local maxima candidates by adjacency, compute the
    # centroid position for each group and take that as the center
    # of one circle detected
        candLM_label,candLM_nRgn=bwlabel(candLM_mask,8,nargout=2)
        for ilabel in arange(1,candLM_nRgn).reshape(-1):
            candgrp_masklin=find(candLM_label == ilabel)
            candgrp_IdxI,candgrp_IdxJ=ind2sub(size(candLM_label),candgrp_masklin,nargout=2)
            candgrp_IdxI=candgrp_IdxI + (aoi(1) - 1)
            candgrp_IdxJ=candgrp_IdxJ + (aoi(3) - 1)
            candgrp_idx2acm=sub2ind(size(accum),candgrp_IdxI,candgrp_IdxJ)
            if sum(accumaoi_LBMask(candgrp_masklin)) < prm_fltrLM_npix:
                continue
            # Compute the centroid position
            candgrp_acmsum=sum(accum(candgrp_idx2acm))
            cc_x=sum(multiply(candgrp_IdxJ,accum(candgrp_idx2acm))) / candgrp_acmsum
            cc_y=sum(multiply(candgrp_IdxI,accum(candgrp_idx2acm))) / candgrp_acmsum
            circen=concat([[circen],[cc_x,cc_y]])
    
    # **** Debug code (begin)
    if dbg_on:
        figure(dbg_bfigno)
        imagesc(dbg_LMmask)
        axis('image')
        title('Generated map of local maxima')
        if size(accumAOI,1) == 1:
            figure(dbg_bfigno + 1)
            surf(candLM,'EdgeColor','none')
            axis('ij')
            title('Accumulation array after local maximum filtering')
    
    # **** Debug code (end)
    
    ######## Estimation of the Radii of Circles ############
    
    # Stop if no need to estimate the radii of circles
    if logical_not(func_compu_radii):
        varargout[1]=circen
        return accum,varargout
    
    # Parameters for the estimation of the radii of circles
    fltr4SgnCv=concat([2,1,1])
    fltr4SgnCv=fltr4SgnCv / sum(fltr4SgnCv)
    # Find circle's radius using its signature curve
    cirrad=zeros(size(circen,1),1)
    for k in arange(1,size(circen,1)).reshape(-1):
        circen_round=round(circen(k,arange()))
        SCvR_I0=circen_round(2) - prm_r_range(2) - 1
        if SCvR_I0 < 1:
            SCvR_I0=1
        SCvR_I1=circen_round(2) + prm_r_range(2) + 1
        if SCvR_I1 > size(grdx,1):
            SCvR_I1=size(grdx,1)
        SCvR_J0=circen_round(1) - prm_r_range(2) - 1
        if SCvR_J0 < 1:
            SCvR_J0=1
        SCvR_J1=circen_round(1) + prm_r_range(2) + 1
        if SCvR_J1 > size(grdx,2):
            SCvR_J1=size(grdx,2)
        # Build the sgn. curve
        SgnCvMat_dx=repmat((arange(SCvR_J0,SCvR_J1)) - circen(k,1),concat([SCvR_I1 - SCvR_I0 + 1,1]))
        SgnCvMat_dy=repmat((arange(SCvR_I0,SCvR_I1)).T - circen(k,2),concat([1,SCvR_J1 - SCvR_J0 + 1]))
        SgnCvMat_r=sqrt(SgnCvMat_dx ** 2 + SgnCvMat_dy ** 2)
        SgnCvMat_rp1=round(SgnCvMat_r) + 1
        f4SgnCv=abs(multiply(double(grdx(arange(SCvR_I0,SCvR_I1),arange(SCvR_J0,SCvR_J1))),SgnCvMat_dx) + multiply(double(grdy(arange(SCvR_I0,SCvR_I1),arange(SCvR_J0,SCvR_J1))),SgnCvMat_dy)) / SgnCvMat_r
        SgnCv=accumarray(ravel(SgnCvMat_rp1),ravel(f4SgnCv))
        SgnCv_Cnt=accumarray(ravel(SgnCvMat_rp1),ones(numel(f4SgnCv),1))
        SgnCv_Cnt=SgnCv_Cnt + (SgnCv_Cnt == 0)
        SgnCv=SgnCv / SgnCv_Cnt
        # -- Radii that correspond to short arcs
        SgnCv=multiply(SgnCv,(SgnCv_Cnt >= (dot(pi / 4,concat([arange(0,(numel(SgnCv_Cnt) - 1))]).T))))
        SgnCv[arange(1,(round(prm_r_range(1)) + 1))]=0
        SgnCv[arange((round(prm_r_range(2)) + 1),end())]=0
        SgnCv=SgnCv(arange(2,end()))
        SgnCv=filtfilt(fltr4SgnCv,concat([1]),SgnCv)
        SgnCv_max=max(SgnCv)
        if SgnCv_max <= 0:
            cirrad[k]=0
            continue
        # Find the local maxima in sgn. curve by 1st order derivatives
    # -- Mark the ascending edges in the sgn. curve as 1s and
    # -- descending edges as 0s
        SgnCv_AscEdg=(SgnCv(arange(2,end())) - SgnCv(arange(1,(end() - 1)))) > 0
        SgnCv_LMmask=logical_and(concat([[0],[0],[SgnCv_AscEdg(arange(1,(end() - 2)))]]),(logical_not(SgnCv_AscEdg)))
        SgnCv_LMmask=logical_and(SgnCv_LMmask,concat([[SgnCv_LMmask(arange(2,end()))],[0]]))
        SgnCv_LMmask=logical_and(SgnCv_LMmask,(SgnCv(arange(1,(end() - 1))) >= (dot(prm_multirad,SgnCv_max))))
        SgnCv_LMPos=sort(find(SgnCv_LMmask))
        if isempty(SgnCv_LMPos):
            cirrad[k]=0
        else:
            cirrad[k]=SgnCv_LMPos(end())
            for i_radii in arange((length(SgnCv_LMPos) - 1),1,- 1).reshape(-1):
                circen=concat([[circen],[circen(k,arange())]])
                cirrad=concat([[cirrad],[SgnCv_LMPos(i_radii)]])
    
    # Output
    varargout[1]=circen
    varargout[2]=cirrad
    if nargout > 3:
        varargout[3]=dbg_LMmask
    