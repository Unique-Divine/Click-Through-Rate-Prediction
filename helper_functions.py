import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class data_transform:
    """A class similar to sklearn.utils.Bunch that I made for convenience.

    Examples:
        >>> import numpy as np
        >>> import pandas as pd
        >>> x0 = np.array(['a', 'b', 'a', 'a', 'c']).reshape(5, 1)
        >>> other_columns = np.random.rand(20).reshape(5, 4)
        >>> data = pd.DataFrame(np.hstack((x0, other_columns)),
                    columns=['x0', 'x1', 'x2', 'y0', 'y1'])
        >>> dt = data_transform(
                    df=data,
                    feature_names=['x0', 'x1', 'x2'],
                    target_names=['y0', 'y1'])
        >>> dt.target_names
        ['y0', 'y1']
        >>> dt.num_features = ['x0']
        >>> dt.get_cat_features()
        ['x1', 'x2']

    """

    def __init__(self, df, feature_names=None, target_names=None,
            num_features=None, cat_features=None):
        """[summary]

        Args:
            df ([type]): [description]
            feature_names (list, optional): [description]. Defaults to None.
            target_names (list, optional): [description]. Defaults to None.
            num_features (list, optional): [description]. Defaults to None.
            cat_features (list, optional): [description]. Defaults to None.
        """
        self.df = df
        self.feature_names = feature_names
        self.target_names = target_names
        self.num_features = num_features
        self.cat_features = cat_features

    def get_feature_names(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if self.target_names != None:
            cols = list(self.df.columns)
            for i in self.target_names:
                cols.remove(i)
            features = cols 
            return features

        elif self.cat_features and self.num_features != None:
            features = self.num_features + self.cat_features
            return features   

    def get_target_names(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if self.feature_names != None:
            cols = list(self.df.columns)
            for i in self.feature_names:
                cols.remove(i)
            self.targets = cols
            return self.targets

        elif self.cat_features and self.num_features != None:
            feature_names = self.get_feature_names()
            cols = list(self.df.columns)
            for j in feature_names:
                cols.remove(j)
            targets = cols
            return targets

    def get_num_features(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        features = list(self.df.columns)
        # Remove target columns from feature list
        for j in self.target_names:
            features.remove(j)
        # Remove categircal features from feature list
        for i in self.cat_features:
            features.remove(i)
        # What's left over is the numerical features.
        return features

    def get_cat_features(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        features = list(self.df.columns)
        # Remove target columns from feature list
        for j in self.target_names:
            features.remove(j)
        # Remove categircal features from feature list
        for i in self.num_features:
            features.remove(i)
        # What's left over is the categorical features.
        return features

    def one_hot_encode(self):
        """Converts an unstructued 2-D array consisting of categorical values
        into a 2-D array consisting of one-hot-encoded vectors.

        """ 
        X = self.df
        X_cat = X[self.cat_features]
        for cat in self.cat_features[:]:
            X = X.drop(cat, axis=1)

        # Replace the nonnumerical columns with one-hot encoded ones.
        for name in self.cat_features[:]:
            hot_one = pd.get_dummies(X_cat[name], prefix=name)
            X = pd.concat([X, hot_one.set_index(X.index)], axis=1)
        return X