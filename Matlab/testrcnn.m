img = imread('stop sign2.jpg');

[bbox, score, label] = detect(rcnn, img, 'MiniBatchSize', 32);

[score, idx] = max(score);

bbox = bbox(idx, :);
annotation = sprintf('%s: (Confidence = %f)', label(idx), score);

detectedImg = insertObjectAnnotation(img, 'rectangle', bbox, annotation);

figure
imshow(detectedImg)