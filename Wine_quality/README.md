# Predict wine quality from review texts
**Shuai Hao, Eugene M. Joseph** 

The three notebooks predict the quality of the wine using [the wine reviews data](https://www.kaggle.com/zynicide/wine-reviews) from Kaggle. The data were scraped on November 22nd, 2017. For all three parts, only the wine from the US are used.

- In part1, we built a model with non-text features and a bag-of-word model. Then we combined them together, and the test score reaches 0.7754.
- In part2, we trained different models using pretrained word embeddings, but none of them performed better than our bag-of-word model.
- In part3, we used a BERT model to predict the wine quality. Without fine tuning, the model doesn't perform very well.