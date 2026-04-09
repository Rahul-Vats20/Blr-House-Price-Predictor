# Bangalore House Price Predictor 🏠

A machine learning web application that predicts property prices in Bangalore, India. This project uses a Linear Regression model trained on real estate data to estimate house prices based on area (square feet), location, and number of BHK/Bathrooms.

## 🚀 Features
- **Accurate Predictions:** Uses a Scikit-learn Linear Regression model optimized via GridSearchCV.
- **Dynamic UI:** Interactive web interface with a dynamic location dropdown fetched from the model's feature set.
- **Data-Driven:** Trained on a comprehensive dataset of Bangalore property prices with robust outlier detection and feature engineering.
- **Deployment Ready:** Includes configuration for deployment on platforms like Heroku.

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-learn, Pandas, NumPy
- **Frontend:** HTML5, CSS3 (Bootstrap), JavaScript (jQuery)
- **Deployment:** Gunicorn

## 📂 Project Structure
- `app.py`: Main Flask application server.
- `model.py`: Script for data cleaning, feature engineering, and model training.
- `model.ipynb`: Jupyter notebook for exploratory data analysis.
- `bangalore_home_prices_model.pickle`: Trained model artifact.
- `columns.json`: Mapping of feature names for the model.
- `templates/`: HTML templates for the web interface.
- `static/`: CSS/JS and image assets.

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/Rahul-Vats20/House-predictor.git
cd House-predictor
```

### 2. Install dependencies
It is recommended to use a virtual environment.
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000/`.

## 📊 Model Training
If you wish to retrain the model, you can run the `model.py` script:
```bash
python model.py
```
This will regenerate `bangalore_home_prices_model.pickle` and `columns.json`.

## 📝 GitHub Metadata Suggestions
- **Description:** A Flask-based web application that predicts house prices in Bangalore using a Linear Regression model.
- **Tags:** `machine-learning`, `flask`, `data-science`, `bangalore-house-price-prediction`, `python`, `linear-regression`, `scikit-learn`, `predictive-modeling`

---
Developed by [Rahul Vats](https://github.com/Rahul-Vats20)
