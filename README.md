# fake-news-analysis

## This is a python project analyzing the [FakeNewsNet dataset](https://github.com/KaiDMML/FakeNewsNet) using NLP techniques. 

### Description
The Jupyter notebook contains exploratory data analysis of news articles and tweets from the Politifact part of the FakeNewsNet dataset. This includes:
- NLP preprocessing steps including cleaning, tokenization, lemmatization and stemming
- Term-Document and TF-IDF matrix construction
- visualization of PCA and T-SNE projections
- traininng and testing linear and nonlinear SVM classifiers on the data
- and much more...

### Some interesting takeaways
- 95% of news articles and 99% of the tweets containing the word 'transcript' were about real news.
- Tweets talking about presidents are mostly about real news, while tweets talking about vaccines are mostly about fake ones.
- Using SVM models trained on news articles to predict the turstworthiness of tweets is often impractical and produces mediocre results.
- The FakeNewsNet dataset is enormous, and this analysis barely touches the surface of what could be learned from it.
