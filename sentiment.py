from textblob import TextBlob
text = "The acting was superb, but the plot was a bit cliche."
blob = TextBlob(text)
sentiment = blob.sentiment
print(f"Sentiment: {sentiment.polarity}")
print(f"Subjectivity: {sentiment.subjectivity}")
if sentiment.polarity > 0:
  print("Classification: Positive")
elif sentiment.polarity < 0:
  print("Classification: Negative")
else:
  print("Classification: Neutral")