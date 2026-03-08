# 50. Implement mini linear regression using NumPy only.

import numpy as np

class LinearRegression:
    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        if X.ndim == 1:
            X = X.reshape(-1, 1)
            
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.weights) + self.bias
            
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
        
    def predict(self, X):
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 6])

model = LinearRegression(lr=0.01, n_iters=1000)
model.fit(X, y)

print(f"Learned weights (slope): {model.weights}")
print(f"Learned bias (intercept): {model.bias}")

test_X = np.array([7, 8])
predictions = model.predict(test_X)
print(f"Predictions for {test_X}: {predictions}")