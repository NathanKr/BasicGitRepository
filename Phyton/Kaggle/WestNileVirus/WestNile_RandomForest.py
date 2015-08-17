
import pandas as pd
import numpy as np
from sklearn import ensemble, preprocessing
import matplotlib.pyplot as plt

# ******************************************
# prepare data : X_train \ X_test
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
# X_train , X_test , sample , weather are type DataFrame 
X_train = pd.read_csv(root+'train.csv')
X_test = pd.read_csv(root+'test.csv')
sample = pd.read_csv(root+'sampleSubmission.csv')
weather = pd.read_csv(root+'weather.csv')


# Get y_labels
y_labels = X_train.WnvPresent.values

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
X_train['month'] = X_train.Date.apply(create_month)
X_train['day'] = X_train.Date.apply(create_day)
X_test['month'] = X_test.Date.apply(create_month)
X_test['day'] = X_test.Date.apply(create_day)

# Add integer latitude/longitude columns
X_train['Lat_int'] = X_train.Latitude.apply(int)
X_train['Long_int'] = X_train.Longitude.apply(int)
X_test['Lat_int'] = X_test.Latitude.apply(int)
X_test['Long_int'] = X_test.Longitude.apply(int)

# drop address columns
X_train = X_train.drop(['Address', 'AddressNumberAndStreet','WnvPresent', 'NumMosquitos'], axis = 1)
X_test = X_test.drop(['Id', 'Address', 'AddressNumberAndStreet'], axis = 1)

# Merge with weather data
X_train = X_train.merge(weather, on='Date')
X_test = X_test.merge(weather, on='Date')
X_train = X_train.drop(['Date'], axis = 1)
X_test = X_test.drop(['Date'], axis = 1)

# Convert categorical data (Species,Street,Trap) to numbers (because thats the algorithm input)
lbl = preprocessing.LabelEncoder() 
lbl.fit(list(X_train['Species'].values) + list(X_test['Species'].values))
X_train['Species'] = lbl.transform(X_train['Species'].values)
X_test['Species'] = lbl.transform(X_test['Species'].values)

lbl.fit(list(X_train['Street'].values) + list(X_test['Street'].values))
X_train['Street'] = lbl.transform(X_train['Street'].values)
X_test['Street'] = lbl.transform(X_test['Street'].values)

lbl.fit(list(X_train['Trap'].values) + list(X_test['Trap'].values))
X_train['Trap'] = lbl.transform(X_train['Trap'].values)
X_test['Trap'] = lbl.transform(X_test['Trap'].values)

# drop columns with -1s (DataFrame.ix is used for index access)
X_train = X_train.ix[:,(X_train != -1).any(axis=0)]
X_test = X_test.ix[:,(X_test != -1).any(axis=0)]


# ******************************************
# fit model 
# ******************************************

# Random Forest Classifier , n_estimators : number of decision trees
#orig cause MemoryError clf = ensemble.RandomForestClassifier(n_jobs=-1, n_estimators=1000, min_samples_split=1)
clf = ensemble.RandomForestClassifier(n_jobs=-1, n_estimators=800, min_samples_split=1)
clf.fit(X_train, y_labels)

# create predictions and submission file
_predict_proba = clf.predict_proba(X_test)[:,1]
h = clf.predict(X_test)
sample['WnvPresent'] = _predict_proba
sample.to_csv(root+'beat_the_benchmark.csv', index=False)

plt.subplot(2, 1, 1)
plt.title('predicted prob for WnvPresent')
plt.plot(_predict_proba,'x')

plt.subplot(2, 1, 2)
plt.title('predicted WnvPresent')
plt.plot(h,'x')
plt.show()
