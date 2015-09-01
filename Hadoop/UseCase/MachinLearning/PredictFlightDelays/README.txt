This is based on http://hortonworks.com/blog/data-science-apacheh-hadoop-predicting-airline-delays/
I am running :
	- step 1,3 on my machine which has 4MB of RAM
	- step 2 on the sandox @ Azure

Components involves :
1. Python and Matplotlib to explore data (2007 is about 700 MB data file , about 7.5 MB rows and about 30 colmns ) - plot.py
2. Pig and python UDF to clean the data and create new data files for years 2007 (train) and 2008 (test) for scikit-learn :
	- remove cancled flights
	- consider only flights originating at ORD airport
	- use only 9 colmns
3. Python's Scikit-learn to predict 2008 delays based on 2007 delays , use : 
	-  LogisticRegression 
	- RandomForest
	- RandomForest with OneHotEncoder to create more features


Remarks :
1. my machine got MemoryError when plot.py was invoked 
2. it is interesting to note that new data files created by Pig on step 2 are actually devided by Map\Reduce to few files
    part-m-00000 , ... ,part-m-00006.
3. my machine got MemoryError on OneHotEncoder 