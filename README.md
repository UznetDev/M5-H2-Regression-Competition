# M5-H2-Regression-Competition

## Project Overview

This project focuses on building a regression model to predict crop yield ('yield') using a dataset with various agricultural metrics. We employ extensive data analysis, feature engineering, and model tuning to minimize the model's error. The final model is stored as a serialized object for easy reuse in production.

## Key Features

- **Custom Preprocessing Pipelines:** Includes transformers for feature selection, feature engineering, and outlier handling.
- **Extensive Feature Engineering:** New features are crafted based on domain knowledge to improve model performance.
- **Pipeline Integration:** A single unified pipeline to streamline preprocessing, feature engineering, and model training.
- **Hyperparameter Tuning:** Optimized hyperparameters for the RandomForestRegressor using advanced techniques optuna.

## Repository Structure

```
M5-H2-Regression-Competition/
├── notebooks/
│   ├── custom_transformers.py   # transformers class for feature engenering
│   ├── EDA.ipynb                # Exploratory Data Analysis
│   ├── Model.ipynb              # Model training and evaluation
│   └── EXPLAIN_model.ipynb      # Model explainability and interpretation
└── data/
│   ├── train.csv                # train.csv model trained datset
│   └── test.csv                 # test csv
├── README.md                    # Project documentation
├── LICENSE                      # Project license (MIT)
├── requirements.txt             # Required Python packages
├── model.joblib                 # Final model
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/UznetDev/M5-H2-Regression-Competition.git
   ```

2. Navigate to the project directory:

   ```bash
   cd M5-H2-Regression-Competition
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Loading and Using the Model

To use the model stored in `model.joblib`, follow these steps:

```python
import joblib
from notebooks.custom_transformers import ColumnSelector, FeatureEngineer, OutlierReplacer
import pandas as pd

# Load the trained model
model = joblib.load('model.joblib')

# Prepare your test data (ensure it matches the training data format)
test_data = pd.read_csv('data/test.csv')

# Make predictions
predictions = model.predict(test_data)
```

## Model Details

The model pipeline integrates several custom transformers and a tuned RandomForestRegressor:

```python
class ColumnSelector(BaseEstimator, TransformerMixin):
    ...
class FeatureEngineer(BaseEstimator, TransformerMixin):
    ...
class OutlierReplacer(BaseEstimator, TransformerMixin):
    ...
    
model = Pipeline([
    ('column_selector', ColumnSelector(columns=['seeds', 'fruitmass', 'fruitset', 'AverageOfUpperTRange'])),
    ('outlier_replacer', OutlierReplacer()),
    ('feature_engineer', FeatureEngineer()),
    ('model', RandomForestRegressor(...))
])
```

## Dataset

The dataset is loaded from `train.csv` and includes features related to crop characteristics and environmental conditions. Detailed exploratory data analysis (EDA) is documented in `notebook/EDA.ipynb`.

## Feature Engineering

The project includes custom feature engineering steps, such as creating ratios and interactions between features (e.g., `FruitToSeedRatio`, `fruitset_seeds`). These are implemented within the `FeatureEngineer` class.

## Models Used

The primary model used is a **RandomForestRegressor** with custom hyperparameters. The pipeline approach allows easy modification and extension of the model, making it robust for handling diverse datasets.

## Hyperparameter Tuning

Hyperparameters for the RandomForestRegressor were optimized with settings such as:

- `max_depth=9`
- `n_estimators=497`
- `max_features=0.809`
- `min_samples_split=10`
- `min_samples_leaf=4`
- `criterion='absolute_error'`

These values were chosen to maximize model performance while preventing overfitting.

## Evaluation

The model was evaluated using standard regression metrics, including RMSE, R^2 and MAE. Details on evaluation and insights are in `notebook/Model.ipynb`.

### Model Explanation

To understand this model, we use two powerful model explainers: **SHAP** and **Permutation Importance**.

1. **Permutation Importance**:
   - **Purpose**: Permutation importance measures the impact of each feature on the model’s accuracy. It works by shuffling each feature and observing how much the model’s accuracy decreases. This technique helps identify which features are most crucial to the overall performance of the model.
   - **Usage**: We calculate the importance of each feature using `permutation_importance` from `sklearn.inspection`.
   - **Plot**: The permutation importance plot ranks features by their influence on model accuracy, making it easy to see which features are essential for the model’s performance.

2. **SHAP (SHapley Additive exPlanations)**:
   - **Purpose**: SHAP values explain individual predictions by showing the impact of each feature on the model’s output. This method highlights how each feature contributes to specific predictions.
   - **Usage**: We use `shap.TreeExplainer` to analyze our model, showing the effect each feature has on the model output.
   - **Plot**: The SHAP summary plot provides a bar chart, showing the average importance of each feature across all predictions, offering insights into which features are most influential.

You can w model explener in `notebook/model_explain.ipynb`

## Usage

The model is pre-trained and saved as `model.joblib`. Load and run it directly to make predictions on new data without retraining.

## Results

The final model achieved strong results on the provided dataset, making it suitable for practical yield predictions in agricultural applications.

## Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository and make a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.
   

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact's

If you have any questions or suggestions, please contact:
- Email: uznetdev@gmail.com
- GitHub Issues: [Issues section](https://github.com/UznetDev/M5-H2-Regression-Competition/issues)
- GitHub Profile: [UznetDev](https://github.com/UznetDev/)
- Telegram: [UZNet_Dev](https://t.me/UZNet_Dev)
- Linkedin: [Abdurakhmon Niyozaliev](https://www.linkedin.com/in/abdurakhmon-niyozaliyev-%F0%9F%87%B5%F0%9F%87%B8-66545222a/)

---

Thank you for your interest in this project. We hope it helps in your journey to understand and predict smoking habits using data science!
