# Machine Learning for classification and prediction

This repository includes the implementation of machine learning algorithms and some experimental projects about applied machine learning. Most projects used structured data from [Kaggle](https://www.kaggle.com/).

- The "algorithms" folder includes the implementation of the perceptron algorithm and gradient descent in linear regression model. It also includes a experiment to group the images pixels by color.
- The "Australia_Fire" folder includes the visualizations of the wild fire satellite data in Australia in early 2020.
- The "Credit_risk_and_US_house_price" folder includes two experimental prediction tasks. One for predicting the credit risks of German customers and another for predicting the housing price in the US. Applying a grid search on a simple Elastic Net model, the testing score reached 0.76 for the credit dataset, but the score only reaches 0.55 for the housing price dataset.
- The "Used_vehicle_price" folder includes several experimental models and a gradient boosting model used for predicting the price of used vehicles. The best gradient boosting model's test score reaches 0.787.
- The "Wine_quality" folder predicts the quality of the wine with a bag-of-word model, three models using pretrained word embeddings and a BERT model. The best bag-of-word model's test score reaches 0.775.