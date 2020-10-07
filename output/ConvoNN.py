import cv2

def ConvoNN(roi=None,*args,**kwargs):
    img  = cv2.resize(roi,(90,90))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    b,g,r = cv2.split(img)
    gb = g-b
    rb = r-b
    median_gb = gb.mean()
    median_rb = rb.mean()

    if (median_rb > median_gb and median_rb >= 5):
        Q = redpreprocess(gray)
        model_red = load_model('model_red.h5')
        model_red.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
        
        predictedLabel = model_red.predict_classes(Q)[0]
        #predictedLabel = red5.classify(Q)
        #if (predictedLabel == 'r¨®') or (predictedLabel == '¥K') or (predictedLabel == '¬¶'):
        #    predictedLabel = red4.classify(Q)
    elif (median_gb > median_rb and median_gb >= 15):
        thresh = 0.38*255
        im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
        Q = 255 - im_bw
        predictedLabel = categorical(cellstr('­I­±'))
    else:
        Q = blackpreprocess(gray)
        class_list[model_black.predict_classes(X)[0]]
        predictedLabel = black2.classify(Q)

    return predictedLabel