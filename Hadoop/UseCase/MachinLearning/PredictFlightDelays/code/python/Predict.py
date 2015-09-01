import os
import pandas as pd
from sklearn import linear_model, cross_validation, metrics, svm
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

def read_csv_from_hdfs_output(path, cols, col_types=None):
    # orig code --> root, dirs, files in os.walk(path, topdown=False):
    pieces = []
    for root, dirs, files in os.walk(path):
        for name in files:
            fname = os.path.join(root, name)
            pieces.append(pd.read_csv(fname, names=cols, dtype=col_types))

    return pd.concat(pieces, ignore_index=True)



# read files
root = '../../data/airline/fm/'
cols = ['delay', 'month', 'day', 'dow', 'hour', 'distance', 'carrier', 'dest', 'days_from_holiday']
col_types = {'delay': int, 'month': int, 'day': int, 'dow': int, 'hour': int, 'distance': int, 
             'carrier': str, 'dest': str, 'days_from_holiday': int}
data_2007 = read_csv_from_hdfs_output(root+'ord_2007_1', cols, col_types)
data_2008 = read_csv_from_hdfs_output(root+'ord_2008_1', cols, col_types)

# Create training set and test set
cols = ['month', 'day', 'dow', 'hour', 'distance', 'days_from_holiday']
train_y = data_2007['delay'] >= 15
train_x = data_2007[cols]

test_y = data_2008['delay'] >= 15
test_x = data_2008[cols]


print (test_x.shape)


# -------- Create logistic regression model with L2 regularization
clf_lr = linear_model.LogisticRegression(penalty='l2', class_weight='auto')
clf_lr.fit(train_x, train_y)

# --------  Predict output labels on test set
pr = clf_lr.predict(test_x)

# --------  display evaluation metrics
cm = confusion_matrix(test_y, pr) # [true_positive false_positive,false_negative true_negative]
print("Confusion matrix")
print(pd.DataFrame(cm))
report_lr = precision_recall_fscore_support(list(test_y), list(pr), average='micro')
print ("\nLogisticRegression : precision = %0.2f, recall = %0.2f, F1 = %0.2f, accuracy = %0.2f\n" % \
        (report_lr[0], report_lr[1], report_lr[2], accuracy_score(list(test_y), list(pr))))


#  -------- Create Random Forest classifier with 50 trees
clf_rf = RandomForestClassifier(n_estimators=50, n_jobs=-1)
clf_rf.fit(train_x, train_y)

#  -------- Evaluate on test set
pr = clf_rf.predict(test_x)

#  -------- print results
cm = confusion_matrix(test_y, pr)
print("Confusion matrix")
print(pd.DataFrame(cm))
report_svm = precision_recall_fscore_support(list(test_y), list(pr), average='micro')
print ("\nRandomForest : precision = %0.2f, recall = %0.2f, F1 = %0.2f, accuracy = %0.2f\n" % \
        (report_svm[0], report_svm[1], report_svm[2], accuracy_score(list(test_y), list(pr))))




# ---------
# this cause MemoryError on my PC (4 GB RAM)
### read files
##cols = ['delay', 'month', 'day', 'dow', 'hour', 'distance', 'carrier', 'dest', 'days_from_holiday']
##col_types = {'delay': int, 'month': int, 'day': int, 'dow': int, 'hour': int, 'distance': int, 
##             'carrier': str, 'dest': str, 'days_from_holiday': int}
##data_2007 = read_csv_from_hdfs_output(root+'ord_2007_1', cols, col_types)
##data_2008 = read_csv_from_hdfs_output(root+'ord_2008_1', cols, col_types)
##
### Create training set and test set
##train_y = data_2007['delay'] >= 15
##categ = [cols.index(x) for x in ['hour', 'month', 'day', 'dow', 'carrier', 'dest']]
##enc = OneHotEncoder(categorical_features = categ)
##df = data_2007.drop('delay', axis=1)
##df['carrier'] = pd.factorize(df['carrier'])[0]
##df['dest'] = pd.factorize(df['dest'])[0]
##train_x = enc.fit_transform(df)
##
##test_y = data_2008['delay'] >= 15
##df = data_2008.drop('delay', axis=1)
##df['carrier'] = pd.factorize(df['carrier'])[0]
##df['dest'] = pd.factorize(df['dest'])[0]
##test_x = enc.transform(df)
##
##print (train_x.shape)
##
##
### Create Random Forest classifier with 50 trees
##clf_rf = RandomForestClassifier(n_estimators=50, n_jobs=-1)
##clf_rf.fit(train_x.toarray(), train_y)
##
### Evaluate on test set
##pr = clf_rf.predict(test_x.toarray())
##
### print results
##cm = confusion_matrix(test_y, pr)
##print("Confusion matrix")
##print(pd.DataFrame(cm))
##report_svm = precision_recall_fscore_support(list(test_y), list(pr), average='micro')
##print ("\nprecision = %0.2f, recall = %0.2f, F1 = %0.2f, accuracy = %0.2f\n" % \
##        (report_svm[0], report_svm[1], report_svm[2], accuracy_score(list(test_y), list(pr))))
##
