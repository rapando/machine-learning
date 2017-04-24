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
        self.weights=[0]*13
        self.learning_rate=1
        self.threshold= 1
        self.folder = "files/"

        print("LIST OF FILES AVAILABLE\n")
        self.files = [f for f in listdir(self.folder) if isfile(join(self.folder, f))]
        x = 1
        for f in self.files:
            print(x, f)
            x += 1
        self.load_data()

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

        if len(self.data[-1]) == 1:
            del self.data[-1]
        # convert the last element into an integer value
        for last in self.data:
            last[-1] = int(last[-1])
        pprint(self.data)
    #function to calculate the dot product of the input and weight
    def dot_product(self,input_vector, weight):
        return sum(values*weight for values ,weight in zip(input_vector,weight))
    # function to set up training sets of the type ([input-vector],[desired_output]) eg.([2,1,2,2],[1])
    def training_set(self):
        pass
    #function finds the adjusted weights
    def learning(self,input_vector,error):
        for index,value in enumerate(input_vector):
            self.weights[index]=self.weights[index] + (self.learning_rate * error * value)

p=Perceptron()
iteration= 1
while (True):
    print('-' * 100)
    print("the iteration is ",iteration,"\n")

    error_count = 0
    for input_vector in p.data:
        print(p.weights)
        result = p.dot_product(input_vector[:13], p.weights)
        if result > p.threshold:
            result= 2
        else:
            result=1

        error = input_vector[-1] - result
        if error != 0:
            error_count += 1
            p.learning(input_vector[:13],error)
    iteration+=1
    if error_count == 0:
        break

print("The optimum weights learned are",p.weights)
