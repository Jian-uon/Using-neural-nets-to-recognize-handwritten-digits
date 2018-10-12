#coding: utf-8
from captcha.image import ImageCaptcha
from PIL import Image
import random, time
import matplotlib.pyplot as plt
import numpy as np


number = [chr(i+ord('0')) for i in range(10)]
letterUp = [chr(i+ord('A')) for i in range(26)]
letterLower = [chr(i+ord('a')) for i in range(26)]

def random_chars_generate(charset=number, length=4):
    random_set = []
    for i in xrange(length):
        random_set.append(random.choice(charset))
    return random_set

def veritify_code_generate_text_and_image():
    image = ImageCaptcha()
    captha_text = ''.join(random_chars_generate())

    captha = image.generate(captha_text)
    captha_image = Image.open(captha)
    #captha_image.show()
    captha_text = np.array(captha_image)
    return captha_text, captha_image

if __name__ == '__main__':
    #print letterUp + number + letterLower
    text, image = veritify_code_generate_text_and_image()
    print 'begin ',time.ctime(),type(image)
    f = plt.figure()
    ax = f.add_subplot(111)
    #ax.text(0.1, 0.9,text, ha='center', va='center', transform=ax.transAxes)
    plt.imshow(image)


    plt.show()
    print 'end ',time.ctime()
