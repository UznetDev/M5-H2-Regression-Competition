from sklearn.base import BaseEstimator, TransformerMixin

class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.columns]

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()
        X_transformed['FruitToSeedRatio'] = X_transformed['fruitset'] / (X_transformed['seeds'] + 1e-5)
        X_transformed['fruitset_seeds'] = X_transformed['seeds'] * X_transformed['fruitset'] / 100
        X_transformed['fruitmass_seeds'] = X_transformed['seeds'] * X_transformed['fruitmass'] / 100
        X_transformed['fruitset_fruitmass_seeds'] = (
            X_transformed['seeds'] * X_transformed['fruitset'] * X_transformed['fruitmass'] / 10000
        )
        X_transformed['FruitSetToUpperTempRatio'] = (
            X_transformed['fruitset'] / (X_transformed['AverageOfUpperTRange'] + 1e-5)
        )
        return X_transformed.drop('AverageOfUpperTRange', axis=1)

class OutlierReplacer(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None):
        self.columns = columns

    def fit(self, X, y=None):
        if self.columns is None:
            self.columns = X.columns
        self.bounds_ = {}
        for column in self.columns:
            Q1 = X[column].quantile(0.25)
            Q3 = X[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            self.bounds_[column] = (lower_bound, upper_bound)
        return self

    def transform(self, X):
        X_transformed = X.copy()
        for column in self.columns:
            lower_bound, upper_bound = self.bounds_[column]
            X_transformed[column] = X_transformed[column].apply(
                lambda x: lower_bound if x < lower_bound else upper_bound if x > upper_bound else x
            )
        return X_transformed
