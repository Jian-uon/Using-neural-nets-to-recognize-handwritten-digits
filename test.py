#coding:utf-8
import numpy as np
import network
from PIL import Image
import mnist_loader


net = network.Network([784, 30, 10], cost=network.CrossEntropyCost)

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
#print test_data[0][0] 

temp = test_data[0][0] 
for i in temp:
    i*=255
    i = int(i)

temp = np.resize(temp, (28,28))
#print temp

def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im


def test():
    for i in xrange(10):
        vec = test_data[i][0]
    print 'Results is %d. Answer is %d.' %  (net.recognize(vec), test_data[i][1])

def local_data():
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
    #img = MatrixToImage(temp)
    #img.show()
    local_data()
