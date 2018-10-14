#coding:utf-8
import numpy as np
import network
from PIL import Image
import mnist_loader


net = network.Network([784, 30, 10], cost=network.CrossEntropyCost)
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

def MatrixToImage(data):
    data = np.resize(data, (28,28))
    data = (1.0-data)*255
    new_im = Image.fromarray(data.astype(np.uint8))
    new_im.show()
    return new_im

def test():
    for i in xrange(10):
        vec = test_data[i][0]
    print 'Results is %d. Answer is %d.' %  (net.recognize(vec), test_data[i][1])

def verify_local_data():
    for index in xrange(4, 10):
        img = Image.open('{}.jpg'.format(index))
        img = img.resize((28,28))
        img = img.convert('L')
        img.show()
        vec = [] 
        for j in xrange(img.size[1]):
            for i in xrange(img.size[0]):
                vec.append((255-img.getpixel((i,j)))/255.0)
        vec = np.reshape(vec, (-1,1))
        #print vec
        print 'result : %d. answer: %d' % (net.recognize(vec), index)

if __name__ == '__main__':
    temp = test_data[0][0] 
    img = MatrixToImage(temp)
    #verify_local_data()
