#!/usr/bin/python
#The total of a column isn't going to be close to the mean of that column. (Note that he name of the key in the dataset is TOTAL -
#this may be important later on.)
#IT TOOK ME SO FUCKING LONG TO FIGURE OUT THAT "TOTAL" WAS ALSO A KEY IN THE LOADED DICTIONARY AND HENCE IT WAS AN OUTLIER(very large salary/bonus)
import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

data_dict.pop("TOTAL", 0)   #we figured out that TOTAL was outlier and had to be removed

###########Figure out what is the outlier that was shown in the scatterplot diagram##########
maxi = 0
maxn = 0
for key in data_dict:
    if(data_dict[key]["bonus"] == 5600000 or data_dict[key]["bonus"] == 7000000):
        print key


features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

print data[-1], data[-2]
data = data[data[:,0].argsort()]
print data[-1], data[-2]

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
