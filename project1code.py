from PIL import Image
import os.path #find files in directory



def median(arr):#this will take the median of an array
    arr = sorted(arr)#sort the array values from least to greatest
    if len(arr) == 0: #when there is nothing in the array
        return None
    elif len(arr) % 2 == 0: #if the length of the array is even we have to take the average of the two middle numbers
        return (arr[len(arr) / 2 - 1] + arr[len(arr)] / 2) / 2
    else:
        return arr[len(arr) / 2] #for when the length is odd



path = "Images/Pics_Project1_CST205" #thisis is where i needed help, thankyou fellow group memebers
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]) - 1 # this is suppose to help with creating a path to the image
        
ImageList = [None] * num_files #this is going to be my image list but it starts out empty

for i in range (0, num_files): #shorthand method to create a list of the images
    ImageList[i] = Image.open("Images/Pics_Project1_CST205/" + str(i + 1) +".png")
    
#before i start modifying the image i need to set a uniform size and shape to an existing picture

width, height = ImageList[0].size #This sets the image shape



#we also ne0ed to create a new image to begin with and add to our lists
ImageList[2].save("Images/Pics_Project1_CST205/noGuy.png") #we copy a picture in the directory to use
finalTemp = Image.open("Images/Pics_Project1_CST205/noGuy.png")#This is going to be the final image that we will use but is not currently modified
endingPicture = finalTemp.load() #we can now change this picture


#so now lets get to changing the pixels
Red = 0
Green = 0 #values that need to be initialized before using them, they will store the new RGB values for the new picture's pixels
Blue = 0

#earlier in class went over this code
redPixelList = [None] * num_files
greenPixelList = [None] * num_files #for color pixel lists to beused later
bluePixelList = [None] * num_files

#need an array to hold all of my pixels
myPixels = [None] * num_files# this is where the images will be converted

for i in range(0 , num_files):
    myPixels[i] = ImageList[i].load() #this puts the images into the pixel list to be computed

for y in range(0, height):#go by column by column
    for x in range(0, width): #we have to go row by row
        for j in range(0, num_files):#we haveto go through all of the files
            pix = myPixels[j] #This is to set an image into a temporary value to be manipulated
            redPixelList[j], greenPixelList[j], bluePixelList[j] = pix[x,y]#we take the temporary information and set it into RGB value arrarys
            
            
        
        Red = median(redPixelList)
        Green = median(greenPixelList) #This is finding the median value of the colors
        Blue = median(bluePixelList)
    
        endingPicture[x,y] = (Red, Green, Blue) #This is setting the midian values to the image we need
    
finalTemp.save("Images/Pics_Project1_CST205/noGuy.png") #saving the image thatwe created

 #Get the width and height of the image
#print pix[x,y] #Get the RGBA value of apixel of an image
#pix[x,y] = value #Set the RGBA value of the image (tuple)
#im.save("Images/Pics_Project1_CST205/new1.png") #Save the modified image

