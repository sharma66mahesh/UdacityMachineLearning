######This is the exercise file###########
def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg

    ### your code goes here!


    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(ages_train, net_worths_train)

    ######to get info about the slope and y intercept######
    print "slope is ", reg.coef_
    print "intercept is", reg.intercept_

    ####predicting######
    print "Net worth at age of 22 is", reg.predict([22])       #note that the predict method takes only list as parameters

    ######get info about scores(how well the regression model performs)########
        #perform on test data set. We can be confident on this result
    print "r-squared score is", reg.score(ages_test, net_worths_test)   #lower score means overfitting(i.e. inclined to test data only or so...)

        #accuracy on train data set. We still don't know if this will perform as expected on any other new data(test data)
    print "r-squared score is", reg.score(ages_train, net_worths_train)
    return reg
