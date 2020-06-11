# CTR-Prediction-with-Stochastic-Gradient-Descent
The goal of this project is to predict whether a dataset of advertisements will be clicked. In solving this problem, I use a stochastic gradient descent algorithm called Pegasos, which is commonly used for [click-through rate (CTR)](https://en.wikipedia.org/wiki/Click-through_rate#:~:text=Click%2Dthrough%20rate%20(CTR)) prediction.


If you only want to read the notebook without downloading anything, here's a link to nbviewer: [CTR-Prediction-with-Stochastic-Gradient-Descent.ipynb](https://nbviewer.jupyter.org/github/Unique-Divine/CTR-Prediction-with-Stochastic-Gradient-Descent/blob/master/CTR%20Prediction%20with%20Stochastic%20Gradient%20Descent.ipynb)

## Contents: ##
1. [Dataset Description](#s1)
2. [Preprocessing](#s2)  
3. [A Generic Classifier Object](#s3)
4. [Decision Boundary Plot Function](#s4)
5. [Regularized Logistic Regression Classifier](#s5)
6. [Regularized Hinge Loss Support Vector Machine Classifier](#s6)
7. [Implementing the Pegasos Algorithm](#s7)
8. [Pegasos on Criteo CTR Prediction Data](#s8)
9. [TODO](#s9)

<a id='s1'></a>
## 1. Dataset Description
### Data Source:
The data is sourced from [CriteoLabs](https://labs.criteo.com/), a multinational corporation in the digital marketing industry, specializing in algorithmic approaches to determine what to show users. In an [old kaggle competition](https://www.kaggle.com/c/criteo-display-ad-challenge), 7 days worth of Criteo's ad data was released. From here on out, this will be referred to as "the Criteo data" in this notebook and it's contained in the  'train_subsampled' file. 

### Data Fields

- Label - Target variable that indicates if an ad was clicked (1) or not (0).
- I1-I13 - A total of 13 columns of integer features (mostly count features).
- C1-C26 - A total of 26 columns of categorical features. The values of these features have been hashed onto 32 bits for anonymization purposes.  

The semantics of the features remain undisclosed.  
  When a value is missing, the field is empty.


### Demo / Usage Instructions:
All required libraries can installed with pip using requirements.txt file. Simply download the file and use
```
pip install -r requirements.txt
```
