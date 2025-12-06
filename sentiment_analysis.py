#Load the libraries
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

#importing the training data
df=pd.read_csv('./Womens Clothing E-Commerce Reviews.csv')
print(df.shape)
df.head(10)

nltk.download('vader_lexicon')

# create a sentiment analyzer object
sid = SentimentIntensityAnalyzer()

# replace missing values with empty string
df['Review Text'] = df['Review Text'].replace(np.nan, '', regex=True)

# iterate over the review text column and calculate the sentiment score
sentiment_scores = []
for text in df['Review Text']:
    scores = sid.polarity_scores(text)
    sentiment_scores.append(scores['compound'])

# add the sentiment scores as a new coloumn in the dataframe
df['Sentiment Scores'] = sentiment_scores

# function to define score to sentiment labels
def get_sentiment_label(score):
  if score >= 0.05:
    return 'Positive'
  elif score <= -0.05:
    return 'Negative'
  else:
    return 'Neutral'

# apply sentiment scores to sentiment labels
sentiment_labels = df['Sentiment Scores'].apply(get_sentiment_label)

# add the sentiment labels as a new coloumn
df['Sentiment Label'] = sentiment_labels

df.head(10)

# count the number of reviews for each sentiment label
sentiment_counts = df['Sentiment Label'].value_counts()

# create a pie chart of the sentiment counts
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%')
plt.title('Sentiment Distribution')
plt.show()

# group the data by rating and sentiment label, and count the number of reviews in each group grouped = df.groupby(['Rating', 'Sentiment Label']).size().reset_index(name='Count')
grouped = df.groupby(['Rating', 'Sentiment Label']).size().reset_index(name='Count')

# iterate over each rating and plot a pie chart of the sentiment label distribution
for rating in range(1, 6):
  data = grouped [grouped [ 'Rating'] == rating]
  plt.pie(data['Count'], labels=data['Sentiment Label'], autopct='%1.1f%%')
  plt.title(f'Sentiment Label Distribution for Rating {rating}')
  plt.show()

# Plot the graph
fig = plt.figure(figsize=(8,6))
df.groupby(['Rating', 'Sentiment Label']).size().unstack().plot(kind='bar', stacked=True)
plt.title('Sentiment Label vs Rating')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()