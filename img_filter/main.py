###################################################################################################
#   Title: Interactive Image Processor
#   File:  main.py
#   Name:  Bill Vo - 301479119
#   Date:  Mar 25, 2022
###################################################################################################

import cmpt120image as image
import cmpt120imageManip as mani

img = image.getImage("bird.png")

print("FILTER \n1: Swap red and green \n2: Convert to black and white \n3: Reflect")
print("4: Brighten \n5: Reload image \n0: Quit")

toQuit = True

while toQuit:
    option  =  input("Enter 1 to 5, 0 to quit: ")
    if option == "1":
        photoRG = mani.swapRedGreen(img)
        image.saveImage(photoRG, "imgRGswap.png")
        image.showImage(photoRG)
    elif option == "2":
        photoBW = mani.blackWhite(img)
        image.saveImage(photoBW, "imgBW.png")
        image.showImage(photoBW)
    elif option == "3":
        photoR = mani.reflect(img)
        image.saveImage(photoR, "imgReflect.png")
        image.showImage(photoR)
    elif option == "4":
        photoB = mani.brighten(img)
        image.showImage(photoB)
    elif option == "5":
        img = image.getImage("bird.png")
        image.showImage(img)
    elif option == "0":
        toQuit = False

