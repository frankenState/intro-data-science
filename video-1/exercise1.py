from sklearn import discriminant_analysis, neighbors, gaussian_process
from sklearn.gaussian_process.kernels import RBF


# height, weight, shoe_size
X = [
    [181,80,44],[177,70,43],[160,60,31],[154,54,37],[166,65,40],
    [190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],
    [181,85,43]
]

Y = ['male','male','female','female','male','male','female','female','female','male','male']

predict_data = [[190,70,43],[180,50,30]]

clf = discriminant_analysis.QuadraticDiscriminantAnalysis()

clf = clf.fit(X,Y)

print("Quadratic Discriminant Analysis: ")
print(clf.predict(predict_data))

clf = neighbors.KNeighborsClassifier(n_neighbors=5)

clf = clf.fit(X,Y)

print("KNeighbors Classifier: ")
print(clf.predict(predict_data))

clf = gaussian_process.GaussianProcessClassifier(kernel=1.0 * RBF(1.0), random_state=0)
clf = clf.fit(X,Y)

print("Gaussian Process Classifier: ")
print(clf.predict(predict_data))