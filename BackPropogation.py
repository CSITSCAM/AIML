from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y=load_iris(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test=train_test_split(
    X, y, 
    test_size=0.2,
    random_state=42
)

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

#fitting only on training data. The test data remains unseen
scaler.fit(X_train)

X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier

clf=MLPClassifier(
    solver='sgd',
    alpha=1e-5,
    random_state=42
)
clf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

y_pred=clf.predict(X_test)
print(accuracy_score(y_test, y_pred))
print(f1_score(y_test, y_pred, labels=[0, 1, 2], average=None))
