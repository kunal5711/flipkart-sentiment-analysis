from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
from flask_cors import CORS
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load models
try:
    with open(r"C:\Users\Ps199\Desktop\Python\Projects\Review Scrapper\Model\countVectorizer.pkl", 'rb') as cv_file:
        cv = pickle.load(cv_file)
    with open(r"C:\Users\Ps199\Desktop\Python\Projects\Review Scrapper\Model\scalar.pkl", 'rb') as scalar_file:
        scalar = pickle.load(scalar_file)
    with open(r"C:\Users\Ps199\Desktop\Python\Projects\Review Scrapper\Model\xgb.pkl", 'rb') as xgb_file:
        xgb = pickle.load(xgb_file)
except Exception as e:
    logger.error(f"Error occurred while loading models: {e}")
    raise

app = Flask(__name__)
CORS(app)

def sentimental_analysis(review_list):
    sentiment_dict = {"Neutral":0, "Negative":0, "Positive":0, "Error": 0}
    for input_review in review_list:
        input_review = [input_review]  # Wrap the string in a list
        embedding = cv.transform(input_review).toarray()
        scaled_embedding = scalar.transform(embedding)
        
        # Get predictions and probabilities
        y_preds = xgb.predict(scaled_embedding)  # Predicted class (0, 1, 2)
        
        # Map prediction to sentiment
        sentiment = y_preds[0]
        if sentiment == 0:
            sentiment_dict['Neutral'] += 1
        elif sentiment == 1:
            sentiment_dict['Negative'] += 1
        elif sentiment == 2:
            sentiment_dict['Positive'] += 1
        else:
            sentiment_dict['Error'] += 1
        
    return sentiment_dict


@app.route("/", methods = ['GET'])
def home():
    return render_template("index.html")

@app.route("/analyze", methods = ["POST"])
def search():
    if request.method == "POST":
        search_query = request.form['product_name']

        driver = webdriver.Chrome()
        driver.get(f"https://www.flipkart.com/search?q={search_query}")

        links = driver.find_elements(By.TAG_NAME, "a")
        pages = []
        for link in links:
            if "CGtC98" in link.get_attribute("class"): 
                pages.append(link.get_attribute("href"))

        review_list = []
        for link in pages:
            driver.get(link)
            reviews = driver.find_elements(By.CLASS_NAME, "EPCmJX")
            for i, review in enumerate(reviews):
                if i<10:                    
                    try:
                        content = review.find_element(By.CLASS_NAME, "ZmyHeo").text
                    except:
                        content = "No content found"

                    # data = {"Content":content}
                    review_list.append(content)
                else:
                    break

    results = sentimental_analysis(review_list)
    logger.info(results)
    return results   

if __name__ == "__main__":
    app.run(debug=True)