from PIL import Image
import glob
import sys
import os

#i and j will represent the alphabetised obverse and reverse coins (assuming they're paired), so they must be offset by 1
i = 0
j = 1

#This script works with the assumption, currently, that you've been given a folder of font/back coins such that "coin.obv.jpg" is the front (Obverse) and "coin.rev.jpg" is the back, or Reverse.
# and you've been given "coin1.obv.jpg", "coin1.rev.jpg", "coin2.obv.jpg", "coin2.rev.jpg", "coin3..." etc etc.

coin_list = [] #create array for all objects in the directory to be indexed
for file in glob.glob("*.jpg"): #for all objects in the current directory that are JPG files...
    coin_list.append(file) #chuck them in the array we created above

os.mkdir("joined") #Create a new directory to store the joined pictures in

while i < len(coin_list): 
    new_image_name = coin_list[i].replace('.obv', '') #create variable for name of new coin as the "obverse" coin name, minus the .obv part
    width, height = Image.open(coin_list[i]).size #set the width and height of the first coin
    total_width = width*2 #set total width for the creation of the new coin image
    new_img = Image.new('RGB', (total_width, height)) #create new image object with width and height
    
    new_img.paste(Image.open(coin_list[i]), (0,0)) #paste the first coin with 0 offset
    new_img.paste(Image.open(coin_list[j]), (width,0)) #past the second coin, offset by the width of the first coin
    new_img.save(f"joined/{new_image_name}") #save the image into the "joined" folder with the name as set previously
    #increment both i and j by 2 so they both acquire the obverse and reverse images of the new pair
    i+=2
    j+=2
    
