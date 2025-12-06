# Sentiment Analysis of E-Commerce Reviews

**Sentiment Analysis** is a Natural Language Processing (NLP) technique used to determine whether a piece of text expresses a **positive**, **negative**, or **neutral** opinion. It is widely used in industry for understanding customer emotions, monitoring brand reputation, analyzing feedback, and making data-driven decisions.

In this project, sentiment analysis is applied to customer-written product reviews from an e-commerce platform. By processing the review text, we extract emotional signals that reveal how customers feel about different products. This helps identify satisfaction levels, uncover common issues, and visualize the relationship between product ratings and expressed sentiment.

This project uses **VADER (Valence Aware Dictionary and sEntiment Reasoner)** — a **rule-based** sentiment analysis tool designed for social media and review-style text. VADER uses a predefined lexicon and heuristic rules rather than machine learning, making it highly effective for short, informal text while requiring no training data.

---

## Overview

This project processes customer review text, computes sentiment scores, assigns sentiment labels, and visualizes sentiment distribution across product ratings.

The workflow includes:

* Data loading & preprocessing
* Sentiment scoring using **VADER**
* Assigning positive/neutral/negative labels
* Visualizing results (pie charts & stacked bar charts)

---

## Why VADER? (Rule-Based NLP)

This project uses **VADER**, a *lexicon + rule-based NLP approach*.
VADER determines sentiment using:

* A predefined sentiment dictionary
* Heuristics for punctuation, capitalization, negations, degree modifiers, etc.

**It does NOT train on data** — which makes it excellent for quick sentiment scoring with no training cost.

---

## Dataset

The dataset used is:

**Women’s Clothing E-Commerce Reviews**
Contains fields such as:

* `Review Text`
* `Rating`
* `Clothing ID`
* `Title`
* `Recommended IND`

You must place the CSV file in your Colab environment or local directory.

---

## Visual Output

The script generates:
✔ Overall sentiment distribution
✔ Sentiment distribution per star rating (1–5)
✔ Stacked bar chart showing how sentiment varies across ratings


---

## How to Run

1. Upload `Womens Clothing E-Commerce Reviews.csv` to Colab or place in your working directory.
2. Run the script sequentially.
3. Visualizations will display inline.

---

## Key Takeaways

* This is a **rule-based** sentiment analysis system using **VADER**.
* No machine learning model is trained.
* Ideal for social media, reviews, and short text sentiment detection.
* Easy to extend with additional visualizations or ML-based enhancements.

---

## Dataset Source

This project uses the **Women’s Clothing E-Commerce Reviews** dataset, publicly available on Kaggle:

**Kaggle Dataset:**
*Women’s E-Commerce Clothing Reviews*
by *Nicapotato*
[https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews)

The dataset contains over **23,000 customer reviews**, including fields such as:

* Review Text
* Rating
* Recommended IND
* Clothing ID
* Title
* Age

This dataset provides a rich collection of real customer feedback, ideal for analyzing sentiment trends and customer satisfaction.

---


