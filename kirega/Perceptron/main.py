import math
from os import listdir
from os.path import isfile, join
from pprint import pprint

class Perceptron():
    "this is to demonstrate the use of Perceptron"
    def __init__(self):
        print("_" * 100)
        print(
        """
			Perceptron - CSC 323 
			Rapando C Samson
			Kirega Joseph
			Adrian Wanderi
			
		""")
        print("_" * 100)

        self.data=self.train_set=[]
        self.learning_rate=1
        self.threshold= 100
        self.folder = "../files/"
        self.iterations=0

        print("LIST OF FILES AVAILABLE\n")
        self.files = [f for f in listdir(self.folder) if isfile(join(self.folder, f))]
        x = 1
        for f in self.files:
            print(x, f)
            x += 1
        self.load_data()
        # dynamically determine the size of vector of weights
        self.len_of_vector=len(self.data[0])-1
        self.weights = [0] * self.len_of_vector
    def load_data(self):
        chosen = int(input("Choose the data file to load : ", ))
        chosen_file = self.files[chosen - 1]
        print("You have chosen ", chosen_file, "...\n")
        # load the data to the self.data variable
        with open(self.folder + chosen_file, "r") as f:
            for line in f:
                sample = line.strip('\r\n').split(' ')
                one_sample = []
                for x in sample:
                    try:
                        one_sample.append(float(x))
                    except:
                        one_sample.append(x)
                self.data.append(one_sample)


        print("The data has been loaded...")
        pprint(self.data)

        print("_"*100)
        # delete the last element if empty list
        if len(self.data[-1]) == 1:
            del self.data[-1]
        # convert the last element into an integer value and introduce the bias in the inputs
        for last in self.data:
            # last[-1]=int(last[-1])
            l=last.pop()
            last.append(1)
            last.append(int(l))
        print("The data has been prepared for the operations...")
        pprint(self.data)

    #function to calculate the dot product of the input and weight
    def dot_product(self,input_vector, weight):
        return sum(values*weight for values ,weight in zip(input_vector,weight))
    # function to set up training sets of the form ([input-vector],[desired_output]) eg.([2,1,2,2],[1])
    def training_set(self):
        pass
    #function finds the adjusted weights
    def learning(self,input_vector,error):
        for index,value in enumerate(input_vector):
            self.weights[index]=self.weights[index] + (self.learning_rate * error * value)
    # the function that combines all the functions into the perceptron
    def perceptron(self):
        while(True):
            print('_' * 150)
            error_count = 0
            for input_vector in self.data:
                print(self.weights)
                result = self.dot_product(input_vector[:self.len_of_vector], self.weights)
                if result > self.threshold:
                    result = 2
                else:
                    result = 1
                error = input_vector[-1] - result
                if error != 0:
                    error_count += 1
                    self.learning(input_vector[:self.len_of_vector], error)

            if error_count == 0 or self.iterations> 10:
                break
            print('_' * 150)
            print("the number of iterations performed")
            print(self.iterations)
            self.iterations = self.iterations + 1
        print("\n The optimum weights learned are",self.weights)

p=Perceptron()
p.perceptron()
print(p.len_of_vector)