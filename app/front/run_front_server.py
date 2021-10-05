from flask import Flask, render_template, redirect, url_for, request, render_template_string
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
# from wtforms import IntegerField, SelectField, StringField
from wtforms import StringField, Form
from wtforms.validators import DataRequired
import urllib.request
import json
from wtforms.fields.html5 import DecimalRangeField


class ClientDataForm(Form):
    Square = DecimalRangeField('Square', default=2)
    LifeSquare = DecimalRangeField('LifeSquare', default=1)
    KitchenSquare = DecimalRangeField('KitchenSquare', default=1)
    Floor = DecimalRangeField('Floor', default=1)
    Ecology_1 = DecimalRangeField('Ecology_1', default=0)
    Social_1 = DecimalRangeField('Social_1', default=0)
    Shops_1 = DecimalRangeField('Shops_1', default=0)
    HouseFloor = DecimalRangeField('HouseFloor', default=1)
    HouseYear = DecimalRangeField('HouseYear', default=1900)
    BldId = DecimalRangeField('BldId', default=0)
    DistrictId_count = DecimalRangeField('DistrictId_count', default=0)
    MedPriceByDistrict = DecimalRangeField('MedPriceByDistrict', default=0)
    MedPriceBySquare = DecimalRangeField('MedPriceBySquare', default=0)


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)


def get_prediction(Square=0, LifeSquare=0, KitchenSquare=0, Floor=0, Ecology_1=0, Social_1=0, Shops_1=0,
                   HouseFloor=0, HouseYear=0, BldId=0, DistrictId_count=0, MedPriceByDistrict=0, MedPriceBySquare=0):
    body = {"Square": Square,
            "LifeSquare": LifeSquare,
            "KitchenSquare": KitchenSquare,
            "Floor": Floor,
            "Ecology_1": Ecology_1,
            "Social_1": Social_1,
            "Shops_1": Shops_1,
            "HouseFloor": HouseFloor,
            "HouseYear": HouseYear,
            "BldId": BldId,
            "DistrictId_count": DistrictId_count,
            "MedPriceByDistrict": MedPriceByDistrict,
            "MedPriceBySquare": MedPriceBySquare
            }

    my_url = "http://0.0.0.0:8280/predict"
    req = urllib.request.Request(my_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    json_data = json.dumps(body)
    json_data_bytes = json_data.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', str(len(json_data_bytes)))
    response = urllib.request.urlopen(req, json_data_bytes)
    return json.loads(response.read())['predictions']


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm(csrf_enabled=False)
    data = dict()
    if request.method == 'POST':
        data["Square"] = request.form.get('Square')
        data["LifeSquare"] = request.form.get('LifeSquare')
        data["KitchenSquare"] = request.form.get('KitchenSquare')
        data["Floor"] = request.form.get('Floor')
        data["Ecology_1"] = request.form.get('Ecology_1')
        data["Social_1"] = request.form.get('Social_1')
        data["Shops_1"] = request.form.get('Shops_1')
        data["HouseFloor"] = request.form.get('HouseFloor')
        data["HouseYear"] = request.form.get('HouseYear')
        data["BldId"] = request.form.get('BldId')
        data["DistrictId_count"] = request.form.get('DistrictId_count')
        data["MedPriceByDistrict"] = request.form.get('MedPriceByDistrict')
        data["MedPriceBySquare"] = request.form.get('MedPriceBySquare')

        try:
            response = str(get_prediction(
                data["Square"],
                data["LifeSquare"],
                data["KitchenSquare"],
                data["Floor"],
                data["Ecology_1"],
                data["Social_1"],
                data["Shops_1"],
                data["HouseFloor"],
                data["HouseYear"],
                data["BldId"],
                data["DistrictId_count"],
                data["MedPriceByDistrict"],
                data["MedPriceBySquare"]
            ))
            print(response)
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8281, debug=True)
