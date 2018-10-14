import mnist_loader
import network


net = network.Network([784, 30, 10], cost=network.CrossEntropyCost)

def getData():
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
#print training_data[0]

def train():
    net.SGD(training_data, 30, 10, 0.5, 
            lmbda = 5.0,
            evaluation_data=validation_data,
            monitor_evaluation_accuracy=True,
            monitor_evaluation_cost=True,
            monitor_training_accuracy=True,
            monitor_training_cost=True)

if __name__ == '__main__':
   getData() 
