
#Binary Bitmap

from PIL import Image
import random 
from logging import error

from PIL import Image
import random
import os
import shutil

#Parameter 
width= 1024
height =768
#Somehow print out a list 
def bmpFile(mList,folder_name,count):
  print(folder_name,count)

  img = Image.new('1', (height , width)) #Input Height and width
  data = mList

  pixels = img.load()

  for i in range(img.size[0]):
      for j in range(img.size[1]):
          pixels[i, j] = data[i][j]
  #flip_img = img.transpose(Image.TRANSPOSE) # if image is flipped disable this

  # rotatedimg = img.rotate(0)
  # transposeimg = rotatedimg.transpose(Image.TRANSPOSE)
  # flip_img = rotatedimg.transpose(Image.FLIP_LEFT_RIGHT)
  flip_img = img.transpose(Image.TRANSPOSE)
  print('fine')
  flip_img.save('./{}/file{}.bmp'.format(folder_name,count),dpi=(2580,2580)) #Change the name

def listShape(width,height):
  myList = []
  for i in range (0, height): #creates how many list there are
    myList.append([0 for i in range(0,width)]) # creates how many indexes per list
  return myList

def magnitude(listm):

  y = ((listm[0]**2)+(listm[1]**2)+(listm[2]**2))**(1/2)
  return y



 

#Rotation
'''print(len(myList))
print(cool)
def moveLeft(num,list = myList):
  for x in range(0,num):
    list[0].append(list[0].pop(0))
  return list[0]

def moveRight(num,list=myList):
  list[0].insert(0, list[0].pop())
  print(list[0])
  return list[0]

myList = moveLeft(255,myList)

print(myList)'''

def printFile(filepath,folder_name,count):
  image = '{}/{}.png'.format(filepath,count)
  print(image)
  im = Image.open(image,'r')

  sensitivity  = 150

  White = magnitude([sensitivity,sensitivity,sensitivity]) #White Pixels
  pix_val = list(im.getdata())

  try:
    pix_val = [0 if (magnitude(x) < White) else 255 for x in pix_val] #Decolorize the image for tuple.
  except:
    pix_val = [0 if x<sensitivity else 255 for x in pix_val] # Try an except detects if the image rgb is in tuples or int







  #Parameters
  Width = width
  idxJump = Width # Input your Width
  start = 0
  end = Width
  #image = [  for i in range(0,int(len(new_image)/102))]


  myList= []

  for i in range(0,int(len(pix_val)/Width)): #divide the length of the list by the Width


    myList.append(pix_val[start:end])

    start+=idxJump
    end+= idxJump

  TestList = [1,2,3,4,5,6,7,8,9,0] 
  print(count,'print')
  bmpFile(myList,folder_name,count)



def convert(folder_name,filepath):

  if not os.path.isdir('./{}'.format(folder_name)): #makes folder
    os.makedirs(folder_name)

  fileList = []

  for filename in os.listdir(filepath):
    name = filename.split('.png')[0]
    fileList.append(name)

  count = 0

  for x in fileList:
    try:
      if type(int(x)) == int:
        count+=1
    except:
      print(x)
  print(count)
  
  for x in range(1,count+1):
    print('the count is ', x)
    
    
    printFile(filepath,folder_name,x)

  shutil.make_archive('./{}'.format(folder_name),'zip')


  return fileList
  
 

    



if __name__ == '__main__':
  convert('90deg',r"filepath") #enter name of output folder and file path of folder you have png images. Make sure png images are named 1.png, 2.png, etc. This is meant to be used with chitubox
