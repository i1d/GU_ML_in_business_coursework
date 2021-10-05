import dill
import pandas as pd
import os
# import cloudpickle
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime

dill._dill._reverse_typemap['ClassType'] = type

# initialize our Flask application and the model
app = flask.Flask(__name__)

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

repp_model_path = "/app/app/models/repp_model.dill"
with open(repp_model_path, 'rb') as rw_f:
    repp_model = dill.load(rw_f)
print(repp_model)


@app.route("/", methods=["GET"])
def general():
    return """Welcome to real estate price prediction. Please use 'http://<address>/predict' to POST"""


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the view
    data = {"success": False}
    dt = strftime("[%Y-%b-%d %H:%M:%S]")
    if flask.request.method == "POST":
        pd_data = {
            "Square": 0,
            "LifeSquare": 0,
            "KitchenSquare": 0,
            "Floor": 0,
            "Ecology_1": 0,
            "Social_1": 0,
            "Shops_1": 0,
            "HouseFloor": 0,
            "HouseYear": 0,
            "BldId": 0,
            "DistrictId_count": 0,
            "MedPriceByDistrict": 0,
            "MedPriceBySquare": 0
        }
        # Square = 0
        # LifeSquare = 0
        # KitchenSquare = 0
        # Floor = 0
        # Ecology_1 = 0
        # Social_1 = 0
        # Shops_1 = 0
        # HouseFloor = 0
        # HouseYear = 0
        # BldId = 0
        # DistrictId_count = 0
        # MedPriceByDistrict = 0
        # MedPriceBySquare = 0

        request_json = flask.request.get_json()
        print(request_json)
        for item in request_json.items():
            print(item)
            if item[0] in pd_data.keys():
                pd_data[item[0]] = item[1]

        logger.info(f'Data: {pd_data}')
        try:
            preds = repp_model.predict(pd.DataFrame(pd_data, index=[0]))
        except AttributeError as e:
            logger.warning(f'{dt} Exception: {str(e)}')
            data['predictions'] = str(e)
            data['success'] = False
            e_flask_data = data | pd_data
            return flask.jsonify(e_flask_data)
        print(f'data_predictions : {preds[0]}')
        flask_data = data | pd_data
        flask_data["predictions"] = int(preds[0])
        # indicate that the request was a success
        flask_data["success"] = True
    print(f'data: {flask_data}')
    # return the data dictionary as a JSON response
    return flask.jsonify(flask_data)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading the model and Flask starting server..."
           "please wait until server has fully started"))
    port = int(os.environ.get('PORT', 8280))
    app.run(host='0.0.0.0', debug=True, port=port)
