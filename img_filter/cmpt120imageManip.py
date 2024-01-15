###################################################################################################
#   Title: Interactive Image Processor
#   File:  cmpt120imageManip.py
#   Name:  Bill Vo - 301479119
#   Date:  Mar 25, 2022
###################################################################################################

import cmpt120image as image


def swapRedGreen(img):
    '''
    input: img - an image
    return: an image that switch red and green color in RGB position
    '''
    heightImg = len(img)
    widthImg = len(img[0])

    imgRGswap = image.getBlackImage(widthImg, heightImg)

    for h in range(heightImg):
        for w in range(widthImg):
            pixel = img[h][w]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            imgRGswap[h][w] = [g,r,b]
    return imgRGswap

def blackWhite(img):
    '''
    input: img - an image
    return: an image with only black and white color
    '''
    heightImg = len(img)
    widthImg = len(img[0])

    imageBW = image.getBlackImage(widthImg, heightImg)

    for h in range(heightImg):
        for w in range(widthImg):
            pixel = img[h][w]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            totalRGB = r+g+b
            if totalRGB < 765/2:
                imageBW[h][w] = [0,0,0]
            else:
                imageBW[h][w] = [255,255,255]
    return imageBW

def reflect(img):
    '''
    input: img - an image
    return: an image that reflect top half of the origin image
    '''
    heightImg = len(img)
    widthImg = len(img[0])

    imageReflect = image.getBlackImage(widthImg, heightImg)
    reflection = image.getBlackImage(widthImg, heightImg//2)
    reflect1 = imageReflect[:heightImg//2]
    reflect2 = imageReflect[heightImg//2:]

    for h in range(heightImg//2, 0, -1):
        for w in range(widthImg):
            pixel = img[h][w]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            reflect2[heightImg//2-h][w] = [r,g,b]

    for h in range(0,heightImg//2):
        for w in range(widthImg):
            pixel = img[h][w]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            reflect1[h][w] = [r,g,b]

    imageReflect = reflect1 + reflect2
    return imageReflect

def brighten(img):
    '''
    input: img - an image
    return: an image that (continuously) brighter
    '''
    heightImg = len(img)
    widthImg = len(img[0])

    for h in range(heightImg):
        for w in range(widthImg):
            pixel = img[h][w]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if r < 229 and g < 229 and b < 229 :
                img[h][w] = [r*1.1,g*1.1,b*1.1]
    return img

