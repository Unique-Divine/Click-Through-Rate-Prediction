# CTR-Prediction-with-Stochastic-Gradient-Descent

Predicting whether advertisements will be clicked or not with Pegasos, a stochastic gradient descent algorithm, and other ML algorithms

## Why do this?
The goal of this project is to predict whether a dataset of advertisements will be clicked or not. In solving this problem, I use a stochastic gradient descent algorithm called Pegasos, which is commonly used for [click-through rate (CTR)](https://en.wikipedia.org/wiki/Click-through_rate#:~:text=Click%2Dthrough%20rate%20(CTR)) predictions.


If you only want to read the notebook without downloading anything, here's a link to nbviewer: [CTR-Prediction-with-Stochastic-Gradient-Descent.ipynb](https://nbviewer.jupyter.org/github/Unique-Divine/CTR-Prediction-with-Stochastic-Gradient-Descent/blob/master/CTR%20Prediction%20with%20Stochastic%20Gradient%20Descent.ipynb)

# Contents       <!-- omit in toc --> 

1. [Dataset Description](#dataset-description)
2. [Jupyter Notebook Contents](#jupyter-notebook-contents)
3. [Demo / Usage Instructions](#usage-instructions)

----

<a id='s1'></a>
## Dataset Description

#### Data Source:

The data is sourced from [CriteoLabs](https://labs.criteo.com/), a multinational corporation in the digital marketing industry, specializing in algorithmic approaches to determine what to show users. In an [old kaggle competition](https://www.kaggle.com/c/criteo-display-ad-challenge), 7 days worth of Criteo's ad data was released. From here on out, this will be referred to as "the Criteo data" in the notebook. The Criteo data is contained in the  'train_subsampled' file. 

#### Data Fields

- Label - Target variable that indicates if an ad was clicked (1) or not (0).
- I1-I13 - A total of 13 columns of integer features (mostly count features).
- C1-C26 - A total of 26 columns of categorical features. The values of these features have been hashed onto 32 bits for anonymization purposes.  

The semantics of the features remain undisclosed.  
  When a value is missing, the field is empty.

----

<a id='s2'></a>
## Jupyter Notebook Contents

1. Dataset Description
2. Preprocessing  
3. A Generic Classifier Object
4. Decision Boundary Plot Function
5. Regularized Logistic Regression Classifier
6. Regularized Hinge Loss Support Vector Machine Classifier
7. Implementing the Pegasos Algorithm
8. Pegasos on Criteo CTR Prediction Data
9. TODO

----

<a id='s3'></a>
## Usage Instructions

All required libraries can installed with pip. I would advise using installing miniconda or Anaconda instead to use `conda install -c conda-forge pandas`, for example.

### TODO

- Compare Pegasos with other benchmark models, particularly ensemble methods like XGBoost and random forests. 
