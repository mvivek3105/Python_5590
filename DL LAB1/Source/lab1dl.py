import pandas as pd
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Loading iris dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
df["target"] = pd.Series(data.target)

# Extract features and labels from pandas data frame
features = df.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
labels = df.loc[:, ['target']]

# Push both features and labels into OneHotEncoder then transform into array
one = OneHotEncoder()
one.fit(features)
features = one.transform(features).toarray()
one.fit(labels)
labels = one.transform(labels).toarray()

# Splitting data into 80% train and 20% test data
xtrain, xtest, ytrain, ytest = train_test_split(features, labels, test_size=0.2)
x = tf.placeholder(tf.float32, [None, 15])
y = tf.placeholder(tf.float32, [None, 3])
w = tf.Variable(tf.zeros([15, 3]))
b = tf.Variable(tf.zeros([3]))

# Declare variable for predicted value
y_predicted = tf.nn.softmax(tf.add(tf.matmul(x, w), b))
loss = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predicted)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

total_row = df.shape[0]

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs/output', sess.graph)

    for _ in range(total_row):
        __, current_loss = sess.run([optimizer, loss], feed_dict={x: xtrain, y: ytrain})
        print("(Iteration,Loss):({},{})".format(_ + 1, sum(current_loss) / total_row))

    prediction = tf.equal(tf.argmax(y_predicted, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))
    print("Model Accuracy is:", accuracy.eval({x: xtest, y: ytest}))
    writer.close()