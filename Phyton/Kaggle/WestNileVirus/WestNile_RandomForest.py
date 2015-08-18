"""
========================
West Nile Virus - Kaggle
========================

use : RandomForest or LogisticRegression or SVM
"""
print(__doc__)


import pandas as pd
import numpy as np
from sklearn import ensemble, preprocessing
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn import linear_model
from sklearn.svm import SVC
from sklearn.learning_curve import learning_curve

# ******************************************
# prepare data : X \ X_test
# ******************************************



# Functions to extract month and day from dataset
# You can also use parse_dates of Pandas.
def create_month(x):
    sep = getSepDate(x)
    return x.split(sep)[1]

def create_day(x):
    sep = getSepDate(x)
    return x.split(sep)[2]

def getSepDate(x):
    if x.find('-') > -1:
        sep = '-'
    else:
        sep = '/'
    return sep        


# Load dataset
root = ".\\Fresh\\"
# X , X_test , sample , weather are type DataFrame 
X = pd.read_csv(root+'train.csv')
X_test = pd.read_csv(root+'test.csv')
sample = pd.read_csv(root+'sampleSubmission.csv')
weather = pd.read_csv(root+'weather.csv')


# Get y
y = X.WnvPresent.values

# Not using codesum for this benchmark (axis = 1 refer to rows)
weather = weather.drop('CodeSum', axis=1) 

# Split station 1 and 2 and join horizontally
weather_stn1 = weather[weather['Station']==1]
weather_stn2 = weather[weather['Station']==2]
weather_stn1 = weather_stn1.drop('Station', axis=1)
weather_stn2 = weather_stn2.drop('Station', axis=1)
weather = weather_stn1.merge(weather_stn2, on='Date')

# replace some missing values and T with -1 
weather = weather.replace('M', -1)
weather = weather.replace('-', -1)
weather = weather.replace('T', -1)
weather = weather.replace(' T', -1)
weather = weather.replace('  T', -1)


# add month and day
X['month'] = X.Date.apply(create_month)
X['day'] = X.Date.apply(create_day)
X_test['month'] = X_test.Date.apply(create_month)
X_test['day'] = X_test.Date.apply(create_day)

# Add integer latitude/longitude columns
X['Lat_int'] = X.Latitude.apply(int)
X['Long_int'] = X.Longitude.apply(int)
X_test['Lat_int'] = X_test.Latitude.apply(int)
X_test['Long_int'] = X_test.Longitude.apply(int)

# drop address columns
#X = X.drop(['Address', 'AddressNumberAndStreet','WnvPresent', 'NumMosquitos'], axis = 1)
X = X.drop(['Address', 'AddressNumberAndStreet','WnvPresent'],  axis = 1)
X_test = X_test.drop(['Id', 'Address', 'AddressNumberAndStreet'], axis = 1)

# Merge with weather data
X = X.merge(weather, on='Date')
X_test = X_test.merge(weather, on='Date')
X = X.drop(['Date'], axis = 1)
X_test = X_test.drop(['Date'], axis = 1)

# Convert categorical data (Species,Street,Trap) to numbers (because thats the algorithm input)
lbl = preprocessing.LabelEncoder() 
lbl.fit(list(X['Species'].values) + list(X_test['Species'].values))
X['Species'] = lbl.transform(X['Species'].values)
X_test['Species'] = lbl.transform(X_test['Species'].values)

lbl.fit(list(X['Street'].values) + list(X_test['Street'].values))
X['Street'] = lbl.transform(X['Street'].values)
X_test['Street'] = lbl.transform(X_test['Street'].values)

lbl.fit(list(X['Trap'].values) + list(X_test['Trap'].values))
X['Trap'] = lbl.transform(X['Trap'].values)
X_test['Trap'] = lbl.transform(X_test['Trap'].values)

# drop columns with -1s (DataFrame.ix is used for index access)

X = X.ix[:,(X != -1).any(axis=0)]
#X_test = X_test.ix[:,(X_test != -1).any(axis=0)]

#X.drop(['NumMosquitos'], axis = 1)
#X_test.drop(['NumMosquitos'], axis = 1)


# ******************************************
# cross validation
# ******************************************
X_train, X_test, y_train, y_test = \
cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)

# ******************************************
# fit model 
# ******************************************


# used this way because otherwise this info is not used sience it does not exist in test
sample_weight = X_train['NumMosquitos'];

X.drop(['NumMosquitos'], axis = 1)
X_train.drop(['NumMosquitos'], axis = 1)
X_test.drop(['NumMosquitos'], axis = 1)

algo = input("Please enter \nRandomForest : r or ENTER \nLogisticRegression : l \nSVM : s\n")


#orig cause MemoryError clf = ensemble.RandomForestClassifier(n_jobs=-1, n_estimators=1000, min_samples_split=1)

if (algo == 'l'):
    #logistic regression
    #precision : 0.6666666666666666 
    #recall : 0.07017543859649122 
    #score : 0.12698412698412698
    clf = linear_model.LogisticRegression()
    clf.fit(X_train, y_train)
elif (algo == 's'):
    # SVM
    ##precision : 0.2549019607843137 
    ##recall : 0.11403508771929824 
    ##score : 0.15757575757575756
    C=10 #changed also by 5 orders and got about the same
    clf = SVC(C,probability=True) # use some like guassian kernel
    clf.fit(X_train, y_train)
else:
    # Random Forest Classifier , n_estimators : number of decision trees
    ##precision : 0.35555555555555557 
    ##recall : 0.14035087719298245 
    ##score : 0.2012578616352201
    clf = ensemble.RandomForestClassifier(n_jobs=-1, n_estimators=400)
    clf.fit(X_train, y_train,sample_weight)

h_test = clf.predict(X_test)

del1 = h_test - y_test # get mismatches between 0 / 1
true_positive  = np.count_nonzero(np.bitwise_and(h_test,y_test))
true_negative  = np.count_nonzero(np.bitwise_and(np.bitwise_not(h_test),np.bitwise_not(y_test)))
false_positive = np.count_nonzero(np.bitwise_and(h_test,np.bitwise_not(y_test)))
false_negative = np.count_nonzero(np.bitwise_and(np.bitwise_not(h_test),y_test))

predicted_positive = (true_positive+false_positive)
actual_positive = (true_positive+false_negative)
precision = true_positive / predicted_positive              # 1 is best
recall = true_positive / actual_positive                    # 1 is best
score = 2*precision*recall/(precision+recall)               # 1 is best
print("precision : %s \nrecall : %s \nscore : %s" % (precision , recall, score))

# create predictions and submission file
_predict_proba = clf.predict_proba(X_test)[:,1]
# h = clf.predict(X_test)
# sample['WnvPresent'] = _predict_proba
# sample.to_csv(root+'beat_the_benchmark.csv', index=False)

plt.figure(1)
plt.subplot(2, 1, 1)
plt.title('predicted prob for WnvPresent [test]')
plt.plot(_predict_proba,'x')

plt.subplot(2, 1, 2)
plt.title('predicted WnvPresent [test]')
plt.plot(h_test,'x')



# ******************************************
# learning curves 
# ******************************************

train_sizes, train_scores, test_scores = \
             learning_curve(clf, X, y,scoring='f1',cv=10, train_sizes=[ 0.01 , 0.1, 0.325, 0.55, 0.775, 1.])
plt.figure(2)
plt.plot(train_sizes,np.average(train_scores,axis=1),'or')
plt.plot(train_sizes,np.average(test_scores,axis=1),'xg')
plt.title('learning curves. average per train size on cross validation')
plt.xlabel('train_sizes')
plt.ylabel('train_scores : o , test_scores : x')
plt.show()
