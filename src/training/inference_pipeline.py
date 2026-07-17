import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt

model = YOLO("models/best.pt")  # Load the mdoel

def detect_obj_yolo(image_path, model, confidence_threshold=0.25):
 # perform probabilistic obj decetion using yolo. (simply running inference)
 # returns bounding boxes, confidance scores, and class probabilities - reject things below from the confindene threshold

#run inference with YOLO
  results = model(image_path, conf=confidence_threshold) #forward pass (model calling directly to a function - eq to model.predict)


#extract results
  boxes = []
  scores = []
  labels = []
  class_probs = []

#pull out bounding boxes, confidence scores, class indices for each result
  for result in results:

    boxes_xyxy = result.boxes.xyxy.cpu().numpy() #bounding boxes [x1,y1,x2,y2] #.cpu().numpy -> move the tensor off gpu, converts into numpy array
    confidence_scores = result.boxes.conf.cpu().numpy() #confidance scores
    class_indices = result.boxes.cls.cpu().numpy().astype(int) #class indices


    #get class probabilities if available (classification model pattern)
    if hasattr(result.boxes, 'probs') and result.boxes.probs is not None:
      class_probabilities = result.boxes.probs.cpu().numpy()
    else:
      class_probabilities = confidence_scores #for single class case, probability is the confifance score


    boxes.extend(boxes_xyxy)
    scores.extend(confidence_scores)
    labels.extend(class_indices)
    class_probs.extend(class_probabilities)


    #load original image for visualization
  image = cv2.imread(image_path)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  #bug (logic) since its n for loop, it reload the image every single time, wasteful

  return boxes, scores, labels, class_probs, image






def draw_detections_yolo(image, boxes, scores, labels, class_names, class_probs = None):
 #draw yolo detections based with probabilistic info (visualize the result on image)
  img_draw = image.copy() #making copy, so u dont draw on the oringinal image array

  for box, score, label, prob in zip(boxes, scores, labels, class_probs or scores):
    x1, y1, x2, y2 = box.astype(int)  #convert float box coordinations to int

      #color based on confidance (green = high, red = low)
    confidence_color = (0, int(255*score), int(255* (1-score))) #building grb tuple, that shifts from red-green
    cv2.rectangle(img_draw, (x1, y1), (x2, y2), confidence_color, 2) #drawing bounding boxes, 2px thick, from given color.


      #labling with class name, confidence with probability info
    class_name = class_names[label] if label < len(class_names) else f"class_{label}" #looks up for human readable class name from YOLO_CLASSES list using predicted index, falls back with a generic if the index out of range
    if class_probs is not None and isinstance(prob, (list, np.ndarray)):

          #multi class probability
          prob_text = f" | P = {prob[label] :.2f}" if len(prob) > label else"" #builds an optional "| P = 0.87" suffix for the label text when per-class probabilities are available.

    else:
        prob_text = ""


    text = f"{class_name}: {score:.2f}{prob_text} "  #draws the text label with |class name|score|text|
    cv2.putText(img_draw, text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, confidence_color, 2)

  return img_draw #draw the image


#Yolo class names (COCO Dataset)
YOLO_CLASSES = ['defect1', 'defect2', 'defect3', 'defect4', 'defect5', 'defect6', 'defect7']


print("YOLO detection fucntions defined")
print("YOLO provides probabilistic confidence scores and class probabilities")


#demo inference with yolo
#for this project, would replace 'sample_img.jpg' with image path
try:
  boxes, scores, labels, class_probs, image = detect_obj_yolo('../data/test_imgs/888.png', model, confidence_threshold = 0.25) #perform probabilistic detection
  result_image = draw_detections_yolo(image, boxes, scores, labels, YOLO_CLASSES, class_probs) #draw detections w. probabilistic info

  #display result
  plt.figure(figsize = (12,8))
  plt.imshow(result_image)
  plt.axis('off')
  plt.title('YOLO probabilistic detections')
  plt.show()

  print(f"yolo detected {len(boxes)} objects probabilistically")
  print("each detection includes confidence score & class probabilities")
  print("green = high confidence | red = low confidence")

except Exception as e:
  print("sample image not found or YOLO inference failed")
  print(f"error {e}")
  print("in a real scenario: ")
  print("1. place an image file in the workspace")
  print("2. update the image path in detect_object_yolo ")
  print("3. run the probabilistic inference code")


plt.figure(figsize=(12,8))
plt.imshow(result_image)
plt.axis('on')
plt.title('YOLO Detections')
plt.savefig('sample_prediction3.png', dpi=150, bbox_inches='tight')
plt.show()
# DUPLICATE - Old Colab code (commented out, use first demo block above)
# #demo inference with yolo
# #replace sample_img.jpg with image path
# 
# try:
#   boxes, scores, labels, image = detect_objects('sample_img.jpg', model, device) #fail without and actual image, but shows the structure
#   result_image = draw_boxes(image, boxes, scores, labels, COCO_CLASSES) #draw detections, outpiuts as result_image
# 
#   #display image using pyplot
#   plt.figure(figsize = (12,8))
#   plt.imshow(result_image)
#   plt.axis('off')
#   plt.show()
# 
#   print(f"detected {len(boxes)} objects") #confirmation and output
# 
# except FileNotFoundError:
#   print("sample image not found")
#   print("1. place an image file in a real scenario")
#   print("2. update the image path in detect_objects")
#   print("3. run the inference code")