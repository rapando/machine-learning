import math

class KMC():

    def __init__(self):
        print """
            KMC DEMO Using K = 2
            Python 2.7.13
            Rapando C Samson
            """

        self.no_samples = int(raw_input("How many samples do you have? "))
        self.no_props = 2
        print "Each sample will have 2 properties"
        self.data = self.d = []
        self.groups, self.centroids = [], {}

    def set_data(self):
        for i in range(self.no_samples):
            temp_data = []
            for j in range(self.no_props):
                prop = raw_input("Sample {} Prop {} : ".format(str(i + 1), str(j + 1)))
                temp_data.append(int(prop))
            self.data.append(temp_data)
            
        # self.data = 
        print "\nData set as"
        print self.data

    def set_centroids(self):
        if len(self.groups) == 0:
            c1 = [self.data[0][0], self.data[0][1]]
            c2 = [self.data[1][0], self.data[1][1]]
        else:
            group_one = group_two = c1 = c2 = []
            current_group = self.groups[-1]
            for i in range(self.no_samples):
                if self.d[i][0] == 1:
                    group_one.append(self.data[i])
                else:
                    group_two.append(self.data[i])

            if len(group_one) < 2:
                c1.append(group_one)
            else:
                c1x = c1y = 0
                for i in group_one:
                    c1x += i[0]
                    c1y += i[1]
                c1.append([int(c1x / len(group_one)) , int(c1y / len(group_one))])

            if len(group_two) < 2:
                c2.append(group_two)
            else:
                c2x = c2y = 0
                for i in group_two:
                    c2x += i[0]
                    c2y += i[1]
                c2.append([int(c2x / len(group_two)) , int(c2y / len(group_two))])

        self.centroids = {'c1' : c1, 'c2' : c2}

    def get_distances(self):
        c1 = self.centroids['c1']   
        c2 = self.centroids['c2']

        for i in range(self.no_samples):
            temp_data = []
            for j in range(self.no_props):
                dist = math.sqrt((self.data[i][j] - c1[0])**2 + (self.data[i][j] - c1[1])**2)
                temp_data.append(dist)

            self.d.append(temp_data)

    def create_group(self):
        group = temp_data = []
        for i in range(self.no_samples):
            x = self.return_bool_int(self.d[i][0] > self.d[i][1])
            y = self.return_bool_int(not x)
            group.append([x, y])

        self.groups.append(group)


    def return_bool_int(self, boolvalue):
        if boolvalue: return 1
        else: return 0



kmc = KMC()
kmc.set_data()
x = 1
while True:
    print "cycle ", 1
    kmc.set_centroids()
    kmc.get_distances()
    kmc.create_group()
    if len(kmc.groups) > 2 and kmc.groups[-1] == kmc.groups[-2]:
        break

