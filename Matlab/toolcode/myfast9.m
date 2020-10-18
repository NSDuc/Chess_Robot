function [ corners ] = myfast9( image , threshold )
[m,n]=size(image);
corner_cnt=0;
precorners=zeros(0,2);
corners_map=zeros(m,n);
scores=zeros(0,0);
scores_map=zeros(m,n);
%% FAST角?提取 效果不好
for i=4:m-3
    
    for j=4:n-3
        
        p=image(i,j);
        
        count=0;
        score=0.0;
        
        p1=image(i-3,j);
        p9=image(i+3,j);
        
        if( abs(p1-p) > threshold)
            count = count+1;
            score=score+abs(p1-p);
        end
        if(abs(p9-p) > threshold)
            count = count+1;
            score=score+abs(p9-p);
        end
        
        if(count==0)
            continue;
        end
        
        p5=image(i,j+3);
        p13=image(i,j-3);
        
        if( abs(p5-p) > threshold)
            count = count+1;
            score=score+abs(p5-p);
        end
        if(abs(p13-p) > threshold)
            count = count+1;
            score=score+abs(p13-p);
        end
        
        if(count<3)
            continue;
        end
        
        p2=image(i-3,j+1);
        p3=image(i-2,j+2);
        p4=image(i-1,j+3);
        
        p6=image(i+1,j+3);
        p7=image(i+2,j+2);
        p8=image(i+3,j+1);
        
        p10=image(i+3,j-1);
        p11=image(i+2,j-2);
        p12=image(i+1,j-3);
        
        p14=image(i-1,j-3);
        p15=image(i-2,j-2);
        p16=image(i-3,j-3);
        
        if( abs(p2-p) > threshold)
            count = count+1;
            score=score+abs(p2-p);
        end
        if(abs(p3-p) > threshold)
            count = count+1;
            score=score+abs(p3-p);
        end
        if(abs(p4-p) > threshold)
            count = count+1;
            score=score+abs(p4-p);
        end
        if(abs(p6-p) > threshold)
            count = count+1;
            score=score+abs(p6-p);
        end
        if(abs(p7-p) > threshold)
            count = count+1;
            score=score+abs(p7-p);
        end
        if(abs(p8-p) > threshold)
            count = count+1;
            score=score+abs(p8-p);
        end
        if(abs(p10-p) > threshold)
            count = count+1;
            score=score+abs(p10-p);
        end
        if(abs(p11-p) > threshold)
            count = count+1;
            score=score+abs(p11-p);
        end
        if(abs(p12-p) > threshold)
            count = count+1;
            score=score+abs(p12-p);
        end
        if(abs(p14-p) > threshold)
            count = count+1;
            score=score+abs(p14-p);
        end
        if(abs(p15-p) > threshold)
            count = count+1;
            score=score+abs(p15-p);
        end
        if(abs(p16-p) > threshold)
            count = count+1;
            score=score+abs(p16-p);
        end
        
        % FAST9
        if(count<9)
            continue;
        end
        
        corner_cnt=corner_cnt+1;
        precorners(corner_cnt,1)=i;
        precorners(corner_cnt,2)=j;
        corners_map(i,j)=1;
        
        scores_map(i,j)=score;
        
        scores(corner_cnt)=score;
        
    end
    
end
%% 非极大值抑制
new_cnt=0;
for k=1:corner_cnt
    i=precorners(k,1);
    j=precorners(k,2);
    ts=scores(k);
    
    ok=1;
    
    for p=i-2:i+2
        for q=j-2:j+2
            if(scores_map(p,q) > ts)
                ok=0;
                break;
            end  
        end
        if(ok==0)
            break;
        end
    end
    
    if(ok==1)
        new_cnt=new_cnt+1;
        corners(new_cnt,1)=j;
        corners(new_cnt,2)=i;
    end
    
end
end