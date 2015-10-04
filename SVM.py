#参考
#http://scikit-learn.org/stable/auto_examples/exercises/plot_iris_exercise.html
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics, grid_search
from sklearn.cross_validation import KFold
import time


iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 0, :2]
y = y[y != 0]

n_sample = len(X)

np.random.seed(0)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(np.float)

X_train = X[:.9 * n_sample]
y_train = y[:.9 * n_sample]
X_test = X[.9 * n_sample:]
y_test = y[.9 * n_sample:]


# fit the model
start = time.time()
C = np.logspace(-4, 4, 10)
parameters = [{'kernel':['rbf'], 'C':C, 'gamma':C},
            {'kernel': ['linear'], 'C': C},
            {'kernel': ['poly'], 'C': C}
            ]
svr = svm.SVC()
cv = KFold(n=len(X_train), n_folds=10, shuffle=True)
clf = grid_search.GridSearchCV(svr, parameters, n_jobs = -1,cv=cv) 


# clf = svm.SVC(kernel='rbf')
clf.fit(X_train, y_train)
print(clf.best_estimator_)
print(clf.fit(X_train, y_train).score(X_test, y_test))
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time))
                    
label_predict = clf.predict(X_test)
print(metrics.classification_report(label_predict, y_test))



plt.figure('svm')
plt.clf()
plt.scatter(X[:, 0], X[:, 1], c=y, zorder=10, cmap=plt.cm.Paired)

# Circle out the test data
plt.scatter(X_test[:, 0], X_test[:, 1], s=80, facecolors='none', zorder=10)

plt.axis('tight')
x_min = X[:, 0].min()
x_max = X[:, 0].max()
y_min = X[:, 1].min()
y_max = X[:, 1].max()

XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

# Put the result into a color plot
Z = Z.reshape(XX.shape)
plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
plt.contour(XX, YY, Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'],
            levels=[-.5, 0, .5])

plt.title('svm')

#成績表示
    
plt.show()