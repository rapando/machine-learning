import math

class KMC():
    def __init__(self):
        self.meds, self.med, self.data = [], {}, [[0]*4, [0]*4]
        self.d , self.data = [[0] * 4, [0] * 4 ], [[0] * 4, [0] * 4 ]
        self.groups = []
        self.centroids = {}
        self.no_samples = 4

        print "\nKMC DEMO USING K = 2"
        print "Written in Python 2.7.13"
        print "Rapando C Samson\n"

    def set_data(self):
        "set the data for the app, in cases where the data has to be manually entered, this is the point of modification"
        names = ['A', 'B', 'C', 'D']
        weights = [1,2,4,5]
        pHs = [1,1,3,4]
        for i in range(self.no_samples):
            self.meds.append({"name" : names[i], "weight" : weights[i], "pH" : pHs[i]})

        self.data[0] = weights
        self.data[1] = pHs

    def get_centroids(self):     
        if len(self.groups) == 0:
            c1 = [self.data[0][0], self.data[1][0]]
            c2 = [self.data[0][1], self.data[1][1]]

        else:
            group_one = group_two = [[0] * 2, [0] * 2]
            for i in range(2):
                for j in range(int(self.no_samples/2)):
                    group_one[i][j] = self.data[i][j]

            for i in range(2):
                for j in range(int(self.no_samples / 2)):
                    group_two[i][j] = self.data[i][j+ int(self.no_samples / 2)]

            c1 = c2 = []
            for row in group_one:
                c1.append(sum(row) / len(row))
            for row in group_two:
                c2.append(sum(row) / len(row))
              
        self.centroids = {"c1" : c1, "c2" : c2}

    def get_d(self, centroids):
        c1 = centroids['c1']
        c2 = centroids['c2']
      
        for i in range(self.no_samples):
            self.d[0][i] = math.sqrt((self.data[0][i] - c1[0])**2 + (self.data[1][i] - c1[1])**2)
            self.d[1][i] = math.sqrt((self.data[1][i] - c2[0])**2 + (self.data[1][i] - c2[1])**2)
       
    def create_group(self):
        group= [[0] * self.no_samples, [0] * self.no_samples]
        for i in range(self.no_samples):
            group[0][i] = self.return_one_or_zero(self.d[0][i] > self.d[1][i])
            group[1][i] = self.return_one_or_zero(not group[0][i])

        self.groups.append(group)

    def return_one_or_zero(self, boolvalue):
        if boolvalue == True:
            return 1
        else:
            return 0
# -----------------------------
k = KMC()
k.set_data()
while True:
    k.get_centroids()
    k.get_d(k.centroids)
    k.create_group()
    if len(k.groups) > 2 and k.groups[-1] == k.groups[-2]:
        break

print "The groups are : "
for i in k.groups:
    print i
print
print "The last group is \t\t\t", k.groups[-1]
print "The second last group is \t", k.groups[-2]
print "Cluster found\n\n"