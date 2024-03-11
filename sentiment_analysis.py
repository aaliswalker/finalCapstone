import spacy
import pandas as pd
from textblob import TextBlob

nlp = spacy.load('en_core_web_sm')

# LOAD DATA.
print("----- LOAD DATA -----")
product_review_df = pd.read_csv('amazon_product_reviews.csv')

product_review_df.info()
print("")

# CLEAN DATA.
reviews_data = product_review_df['reviews.text']
clean_data = product_review_df.dropna(subset=['reviews.text'])

# INPUT VALIDATION FUNCTION.
def review_input():
    text = input("Type in the product review: ")
    # Check if the input is not empty after stripping whitespace.
    if text.strip():
        # Clean the text and assign it back to review.
        review = clean_text(text)
        return review
    else:
        print("Please enter a non-empty description.")
        # Return None when input is empty.
        return None

# CLEANING FUNCTION.
def clean_text(text):
    doc = nlp(text)
    cleaned_tokens = [token.text.lower() for token in doc if not token.is_stop and token.text.strip()]
    cleaned_text = ' '.join(cleaned_tokens)
    return cleaned_text

# SENTIMENT ANALYSIS FUNCTION.
def sentiment_analysis(product_review):
    blob = TextBlob(product_review)
    sentiment = blob.sentiment
    polarity = sentiment.polarity
    if polarity > 0:
        sentiment_label = "Positive"
    elif polarity == 0:
        sentiment_label = "Neutral"
    else:
        sentiment_label = "Negative"
    print(f"{product_review}: {sentiment_label} ({polarity})")

# REVIEW INPUT.
product_review = review_input()
print(" ")

# INPUT VALIDATION.
if product_review:
    print("Sentiment Analysis for User Input:")
    cleaned_product_review = clean_text(product_review)
    sentiment_analysis(cleaned_product_review)
    print(" ")

# SAMPLE REVIEWS.
sample_reviews = [
    "I hate this!",
    "I love this!",
    "When I tried to use this, it didn't work.",
    "It has been the best performing appliance I have bought in a long time."
]

# TESTING MODEL.
def testing_model():
    print("Testing Sentiment Analysis on Sample Reviews:")
    for review in sample_reviews:
        cleaned_review = clean_text(review)
        sentiment_analysis(cleaned_review)

# CALL TESTING MODEL.
testing_model()

# RETREIVE RANDOM DATABASE REVIEWS.
review1_text = clean_data.iloc[20]['reviews.text']
review2_text = clean_data.iloc[8]['reviews.text']

# CLEAN RANDOM REVIEWS.
review1_cleaned = clean_text(review1_text)
review2_cleaned = clean_text(review2_text)

# SENTIMENT ANALYSIS ON RANDOM REVIEWS.
print(" ")
print("Sentiment Analysis for Random Reviews:")
sentiment_analysis(review1_cleaned)
sentiment_analysis(review2_cleaned)
