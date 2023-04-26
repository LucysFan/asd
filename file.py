import os

import cv2 as cv


print("If directory is not in your folder input whole way \n")

while not os.path.exists(path := input("Input directory >>> ")):
  print("There is no such folder")
path2Write = input("Input new directory>>> ")



if not os.path.exists(path2Write):
  os.makedirs(path2Write)

critical = 700
data = {}

for obj in os.listdir(path):
  
  # try:      
    image = cv.imread(path + '/' + obj)
    counter = 0
    height, width, _ = image.shape

    for h in range(height):
      for w in range(width):
        if sum([image[h, w][i] for i in range(3)]):
          counter += 1
    image = cv.putText(image,
                       'PROCESSED',
                       [0, 255],
                       cv.FONT_HERSHEY_SIMPLEX, 
                       1, (0,0,255))

    if counter in data:
      name = path2Write + '/' + f"{counter}_{data[counter]}.{obj.split('.')[-1]}"
      cv.imwrite(name, image)
      data[counter] += 1
    else:
      name = path2Write + '/' + f"{counter}.{obj.split('.')[-1]}"
      print(name)
      print(counter)
      cv.imwrite(name, image)
      data[counter] = 1
        
  # except Exception:
  #       print('Not a picture', obj)
    