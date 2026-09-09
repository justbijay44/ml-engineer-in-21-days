import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def euclidean_distance(pt_a, pt_b):
    return np.sqrt(np.sum((pt_a - pt_b) ** 2))

def knn_predict(X, y, q_pt, k):
    distance = [euclidean_distance(q_pt, x) for x in X]
    indexes_till_k = np.argsort(distance)[:k]
    nearest_labels = y[indexes_till_k]
    return max(Counter(nearest_labels).items(), key=lambda x: x[1])[0]

if __name__ == "__main__":
    class_zero = np.random.randn(50, 2) + [2, 2]
    class_one = np.random.randn(50, 2) + [8, 8]

    label_zero = np.zeros(50)
    label_one = np.ones(50) 

    query_pt = np.array([7,7])

    X = np.vstack([class_zero, class_one])
    y = np.concatenate([label_zero, label_one])

    # print(knn_predict(X, y, query_pt, 5))

    test_pts = np.random.rand(10 , 2) * 10
    test_labels = [knn_predict(X, y, pt, 5) for pt in test_pts]

    plt.scatter(X[:, 0], X[:, 1], c = y)
    plt.scatter(test_pts[:, 0], test_pts[:, 1], c = test_labels, marker='x', s=50)
    plt.show()