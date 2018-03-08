from sklearn import neighbors, datasets

# importing data
iris = datasets.load_iris()
X = iris.data[:, :]
y = iris.target

# Splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)


from sklearn import metrics
neighbours =  [1,10,15,25,50]
for x in neighbours:
    clf = neighbors.KNeighborsClassifier(x)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    print("Accuracy Score for K = ",x)
    print(metrics.accuracy_score(y_test, y_pred))