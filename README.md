# Flipkart Review Sentiment Analysis

## Overview
This project is a web application that analyzes the sentiment of Flipkart product reviews. Users input a product name, and the app fetches reviews (to be implemented), performs sentiment analysis, and displays the distribution of sentiments ("Positive," "Negative," "Neutral," "Error") in a pie chart. The backend uses a pre-trained XGBoost model with a `CountVectorizer` and `MinMaxScaler` for text processing, while the front-end is built with HTML, CSS, and Chart.js for visualization.

## Features
- **Input**: Enter a product name to analyze its reviews.
- **Sentiment Analysis**: Classifies reviews into Positive, Negative, Neutral, or Error categories.
- **Visualization**: Displays sentiment counts in an interactive pie chart.
- **Tech Stack**:
  - Backend: Flask (Python), XGBoost, scikit-learn.
  - Frontend: HTML, CSS, JavaScript, Chart.js.

## Project Structure
```
flipkart-sentiment-analysis/
├── static/
│   ├── css/
│   │   └── styles.css        # Styles for the UIfiles
├── templates/
│   └── index.html            # Main HTML template
├── app.py                    # Flask application
├── README.md                 # Project documentation
└── Model/                   
    ├── countVectorizer.pkl   # Pre-trained CountVectorizer
    ├── scalar.pkl            # Pre-trained MinMaxScaler
    └── xgb.pkl               # Pre-trained XGBoost model
```

## Prerequisites
- Python 3.8+
- Flask
- scikit-learn
- xgboost
- numpy
- requests (for review fetching, if implemented)
- BeautifulSoup4 (for scraping, if implemented)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/flipkart-sentiment-analysis.git
cd flipkart-sentiment-analysis
```

### 2. Install Dependencies
Create a virtual environment and install required packages:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Add Pre-trained Models
Place your pre-trained model files in a `models/` folder (update paths in `app.py` if different):
- `countVectorizer.pkl`
- `scalar.pkl`
- `xgb.pkl`

Note: These files are not included in the repo due to size. You must train and save them separately using scikit-learn and XGBoost.

### 4. Run the Application
```bash
python app.py
```
- The app will run on `http://127.0.0.1:5000/` by default.

## Usage
1. Open your browser and navigate to `http://127.0.0.1:5000/`.
2. Enter a product name (e.g., "iPhone 13") in the input field.
3. Click "Analyze Reviews" to see the sentiment distribution in a pie chart.

**Note**: The current implementation uses dummy review data. To fetch real Flipkart reviews, implement the scraping logic in `app.py`.

## Backend Details
- **Endpoint**: `/analyze` (POST)
  - Input: `product_name` (form-data)
  - Output: JSON with sentiment counts (e.g., `{"Positive": 10, "Negative": 5, "Neutral": 3, "Error": 1}`)
- **Sentiment Analysis**:
  - Uses `CountVectorizer` to convert text to numerical features.
  - Scales features with `MinMaxScaler`.
  - Predicts sentiment with an XGBoost classifier (0 = Neutral, 1 = Negative, 2 = Positive).

## Frontend Details
- **Form**: Submits product name via `fetch` to `/analyze`.
- **Chart**: Displays sentiment counts using Chart.js (pie chart).
- **Styling**: Responsive design with Flipkart-inspired blue (#2874f0).