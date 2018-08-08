#!/usr/bin/python
from __future__ import division     #import this in python 2 so that "/" means float division and "//" means integer division

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

    NaN in the values of dictionary means that there is no value defined for that key
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#print (enron_data.values()[0])     #to print what values the dictionary inside the enron_data dictionary has
    #note that values() method is built in python dictionary's method
#print len(enron_data)   #number of persons in enron data set. Ans is 146

#print len(enron_data.values()[0])   #no. of feautres available for each person

# cnt = 0   #printing the number of POI in the dataset
#
# for i in range (0, len(enron_data)):
#     if enron_data.values()[i]["poi"] == 1:
#         cnt = cnt + 1
#
# print cnt

###printing all the keys of enron_data dictionary
# for key in enron_data:
#     print "key is:", key

################    total POIs as found from newspaper  ##################
# fd = open("../final_project/poi_names.txt", "r")
# lineList = fd.readlines()
# cnt = 0
# for i in lineList:
#     if "(y)" in i:
#         print i
#         cnt = cnt + 1
# print cnt

#for i in range(0:len(enron_data)):
#    if(enron_data)

#to find the total stock belonging to james prentice
#print enron_data["PRENTICE JAMES"]["total_stock_value"]    #note that first key is all capital

#to print all the emails from wesley colwell to any POIs
#print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#print stock options for jeffrey k skilling
#print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

#######find who fled with the most money and the amount
# if(max(enron_data["LAY KENNETH L"]["total_payments"], enron_data["FASTOW ANDREW S"]["total_payments"], enron_data["SKILLING JEFFREY K"]["total_payments"]) == enron_data["SKILLING JEFFREY K"]["total_payments"]):
#     print "Jeff", enron_data["SKILLING JEFFREY K"]["total_payments"]
# elif(max(enron_data["LAY KENNETH L"]["total_payments"], enron_data["FASTOW ANDREW S"]["total_payments"], enron_data["SKILLING JEFFREY K"]["total_payments"]) == enron_data["FASTOW ANDREW S"]["total_payments"]):
#     print "Andrew", enron_data["FASTOW ANDREW S"]["total_payments"]
# else:
#     print "Ken", enron_data["LAY KENNETH L"]["total_payments"]

###########count the number of people with quantified salary and emails
# email = 0
# salary = 0
# for i in range(0,len(enron_data)):
#     if(enron_data.values()[i]["email_address"] != "NaN"):
#         email = email + 1
#     if(enron_data.values()[i]["salary"] != "NaN"):
#         salary = salary + 1
# print "salary count", salary, "email count", email

#####how many people have NaN as their value for total_payments
# count = 0
# for i in range(0, len(enron_data)):
#     if(enron_data.values()[i]["total_payments"] == "NaN"):
#         count = count + 1
# print count     #ans is 21
# per = count/len(enron_data) * 100
# print "percentage is:", per     #14.3835

######how many pois have NaN in their total_payments
# count = 0
# totalPois = 0
# noPaymentInfo = 0
# for i in range(0, len(enron_data)):
#     if(enron_data.values()[i]["poi"] == True):
#         totalPois = totalPois + 1
#         if(enron_data.values()[i]["total_payments"] == "NaN"):
#             noPaymentInfo = noPaymentInfo + 1
# print noPaymentInfo/totalPois   #0
# print totalPois   #18
