```markdown
# Capstone Project: Sentiment Analysis on Amazon Product Reviews

## Overview
This project performs sentiment analysis on Amazon product reviews using Natural Language Processing (NLP) techniques. The goal is to classify the sentiment of reviews as positive, neutral, or negative based on the text content.

## Dependencies
- `spacy`
- `pandas`
- `textblob`

Download the dataset `amazon_product_reviews.csv` from kaggle and place it in the project directory.

## Usage
### 1. Loading and Cleaning Data
The script loads the Amazon product reviews dataset from `amazon_product_reviews.csv`, then cleans the data by removing empty reviews.

### 2. Input Validation and Cleaning
The `review_input()` function allows users to input a product review. It validates the input and cleans the text using the `clean_text()` function.

### 3. Sentiment Analysis
The `sentiment_analysis()` function analyzes the sentiment of the provided review. It uses the TextBlob library to determine sentiment polarity and assigns a label (Positive, Neutral, or Negative).

### 4. Sample Reviews
The project includes a set of sample reviews to demonstrate sentiment analysis. These are predefined in the `sample_reviews` list.

### 5. Testing Model
The `testing_model()` function runs sentiment analysis on the sample reviews and prints the results.

### 6. Random Database Reviews
Two random reviews from the cleaned dataset are analyzed for sentiment to showcase the functionality on real data.

### Running the Code
Run the `capstone_sentiment_analysis.py` script to execute the functions:
```bash
python capstone_sentiment_analysis.py
```

Follow the prompts to input a review or observe the sentiment analysis on sample and random reviews.

## Functions
- `review_input()`: Validates user input for a product review.
- `clean_text(text)`: Cleans the input text by removing stopwords and converting to lowercase.
- `sentiment_analysis(product_review)`: Analyzes the sentiment of a given review.
- `testing_model()`: Tests the sentiment analysis model on sample reviews.

## Example Output
```
----- LOAD DATA -----
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50 entries, 0 to 49
Data columns (total 2 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   reviews.text   50 non-null     object
 1   sentiment      50 non-null     object

Type in the product review: This product is amazing!
 
Sentiment Analysis for User Input:
this product amazing: Positive (0.6000000000000001)
 
Testing Sentiment Analysis on Sample Reviews:
i hate this!: Negative (-0.8)
i love this!: Positive (0.5)
when i try use this work: Negative (-0.2)
best perform appliance buy long time: Positive (1.0)
 
Sentiment Analysis for Random Reviews:
this first tv color easy install great picture love: Positive (0.8)
perfect exactly i wanted price delivery: Positive (1.0)

```
