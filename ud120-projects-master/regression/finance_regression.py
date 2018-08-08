#!/usr/bin/python

"""
    Starter code for the regression mini-project.

    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    We're using salary as feature(input) and bonus as target(output).

    You fill in the regression code where indicated:
"""


import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the
### list will be the "target" feature
features_list = ["bonus", "salary"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(feature_train, target_train)
print "slope:", reg.coef_, "intercept", reg.intercept_
print "r-squared score on training data", reg.score(feature_train, target_train)    #very less 0.045
print "r-squared score on test data", reg.score(feature_test, target_test)      #Really shitty score -1.48  (-ve)
        #Now since the score are pathetic, we'd like to find an appropirate feature that could help us predict bonus like long_term_incentive.
        #for that we change the features_list at around line 26.
        #the scores for long_term_incentive are pretty bad too -0.59 for test_data. However, it's better than using salary as a feature
        #scores are shitty mainly due to outliers. (see note on outliers)



### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):  #for python2 zip combines the elements with same index on given lists and forms list of tuples
                                                        #eg:zip([1,2,3], [3,4,5]) gives [(1,3), (2,4), (3,5)]
    plt.scatter( feature, target, color=test_color )
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color )

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")



### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass
#the following two lines are added from outlier note
reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="b")
print "new slope after training on test data instead of using train_data", reg.coef_    #huge difference from previous slope value

plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
