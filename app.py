from flask import Flask, request, url_for, render_template
import pickle
import numpy as np
import json

app = Flask(__name__)

app.config.update(
    dict(SECRET_KEY="powerful secretkey", WTF_CSRF_SECRET_KEY="a csrf secret key")
)

__data_columns = None
__locations = None
model = None

def load_saved_artifacts():
    print("Loading the saved artifacts...start !")
    global __data_columns
    global __locations
    global model

    # Load Model
    with open("bangalore_home_prices_model.pickle", "rb") as f:
        model = pickle.load(f)

    # Load Columns
    with open("columns.json", "r") as f:
        __data_columns = json.loads(f.read())["data_columns"]
        __locations = __data_columns[3:] # first 3 are sqft, bath, bhk

# Initialize artifacts immediately
load_saved_artifacts()

def get_estimated_price(input_json):
    try:
        loc_index = __data_columns.index(input_json['location'].lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = input_json['sqft']
    x[1] = input_json['bath']
    x[2] = input_json['bhk']
    if loc_index >= 0:
        x[loc_index] = 1
    result = round(model.predict([x])[0],2)
    return result

@app.route("/get_location_names", methods=["GET"])
def get_location_names_route():
    return json.dumps({"locations": __locations})

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/prediction", methods=["POST"])
def prediction():
    
    if request.method == 'POST':
        input_json = {
            "location": request.form['sLocation'],
            "sqft": request.form['Squareft'],
            "bhk": request.form['uiBHK'],
            "bath": request.form['uiBathrooms']
        }
        result = get_estimated_price(input_json)

        if result > 100:
            result = round(result/100, 2)
            result = str(result) + ' Crore'
        else:
            result = str(result) + ' Lakhs'

    return render_template('prediction.html', result=result)

if __name__ == "__main__":
    print("Starting Python Flask Server")
    app.run(debug=True)
