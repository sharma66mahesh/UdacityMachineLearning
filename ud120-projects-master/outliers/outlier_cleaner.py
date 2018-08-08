#!/usr/bin/python
#In outliers/outlier_cleaner.py, you will find the skeleton for a function called outlierCleaner() that you will fill in with a cleaning algorithm.
#It takes three arguments: predictions is a list of predicted targets that come from your regression, ages is the list of ages in the training set,
#and net_worths is the actual value of the net worths in the training set. There should be 90 elements in each of these lists
#(because the training set has 90 points in it). Your job is to return a list #called cleaned_data that has only 81 elements in it,
# which are the 81 training points where the predictions and the actual values (net_worths) have the smallest errors (90 * 0.9 = 81).
#The format of cleaned_data should be a list of tuples, where each tuple has the form (age, net_worth, error). *

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    residual_error = abs(predictions - net_worths)
    ages_error_coupled = zip(ages, net_worths, residual_error)  #form a list of tuples
    ages_error_coupled.sort(key = lambda t: t[2])   #sort the list of tuples in increasing order of residual error
    cleaned_data = ages_error_coupled[: int(.9 * len(ages))]    #clear the last 10% data

    return cleaned_data
