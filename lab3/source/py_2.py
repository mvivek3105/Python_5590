from sklearn import svm
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Read IRIS Data
iris = datasets.load_wine()
# Load data and target into x and y
x = iris.data
y = iris.target
# Dividing the data to 20% of testing data & 80% of training data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)
print("SVM with linear kernel:")
# Create SVM model with linear kernel
linear_kernel_model = svm.SVC(kernel="linear"); linear_kernel_model.fit(xtrain, ytrain)
# Generate ypredict from trained model with data from xtest
ypredicted = linear_kernel_model.predict(xtest)
# Print data on both ypredicted and ytest
print("ypredicted:")
print(ypredicted)
print("ytest:")
print(ytest)
# Check accuracy score by compare y_test and y_predicted
print("score of SVM with linear kernel: %.4f" % metrics.accuracy_score(ytest, ypredicted)); print("\nSVM with RBF kernel:")
# Create model for SVM with RBF kernel
rbf_model = svm.SVC(kernel="rbf")
# Fit the data into the model
rbf_model.fit(xtrain, ytrain)
# Generate y_predict from trained model with data from x_test
y_predict = rbf_model.predict(xtest)
# Print data on both y_predicted and y_test
print("ypredicted:")
print(y_predict)
print("ytest:")
print(ytest)
# Check accuracy score by compare y_test and y_predicted
print(" score of SVM with RBF Kernel: %.4f" % metrics.accuracy_score(ytest, ypredicted))