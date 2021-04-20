#!/usr/bin/env python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier

def create_data():
    train = np.loadtxt('zip.train')
    y_train = train[:,0]
    x_train = train[:,1:]
    x_train = x_train[(y_train==2) | (y_train==3)]
    y_train = y_train[(y_train==2) | (y_train==3)]
    test = np.loadtxt('zip.test')
    y_test = test[:,0]
    x_test = test[:,1:]
    x_test = x_test[(y_test==2) | (y_test==3)]
    y_test = y_test[(y_test==2) | (y_test==3)]
    
    outf = open('2.8.out', 'w')
    outf.write('Regressor,Train acc,Test acc\n')
    
    lin_reg = LinearRegression()
    lin_reg.fit(x_train, y_train)
    lin_train = np.floor(lin_reg.predict(x_train)+0.5)
    lin_train_acc = np.sum(lin_train==y_train)/lin_train.shape[0]
    lin_test = np.floor(lin_reg.predict(x_test)+0.5)
    lin_test_acc = np.sum(lin_test==y_test)/lin_test.shape[0]
    outf.write('"LR",{},{}\n'.format(lin_train_acc, lin_test_acc))
    
    for k in [1, 3, 5, 7, 15]:
        knn_reg = KNeighborsClassifier(n_neighbors=k)
        knn_reg.fit(x_train, y_train)
        knn_train = np.floor(knn_reg.predict(x_train)+0.5)
        knn_train_acc = np.sum(knn_train==y_train)/knn_train.shape[0]
        knn_test = np.floor(knn_reg.predict(x_test)+0.5)
        knn_test_acc = np.sum(knn_test==y_test)/knn_test.shape[0]
        outf.write('"{}NN",{},{}\n'.format(k, knn_train_acc, knn_test_acc))
    outf.close()

# create_data()

def plot_data():
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
    
    data = pd.read_csv('2.8.out')
    
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_ylim(0.94, 1.01)
    ax.scatter(data['Regressor'], data['Train acc'], label='Train acc', color=(0.6, 0.1, 0.1))
    ax.plot(data['Regressor'][1:], data['Train acc'][1:], color=(0.6, 0.1, 0.1))
    ax.axhline(y=data['Train acc'][0], color=(0.6, 0.1, 0.1, 0.4), ls='--')
    ax.scatter(data['Regressor'], data['Test acc'], label='Test acc', color=(0, 0.6, 0.3))
    ax.plot(data['Regressor'][1:], data['Test acc'][1:], color=(0, 0.6, 0.3))
    ax.axhline(y=data['Test acc'][0], color=(0, 0.6, 0.3, 0.4), ls='--')
    
    plt.legend(loc='lower right')
    plt.savefig('2.8.png', bbox_inches='tight')

plot_data()
