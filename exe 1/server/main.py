#
# from flask import Flask, jsonify
# import datetime
#
# app = Flask(__name__)
#
# x = datetime.datetime.now()
#
#
# @app.route('/data')
# def get_time():
#     data = {
#         'Name': "geek",
#         "Age": "22",
#         "Date": x,
#         "programming": "python"
#     }
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, jsonify
from flask_cors import CORS
from api.controllers.corona_patient_controller import corona_patient_controller
from api.controllers.patient_controller import patients_details_controller
# from api import create_app
app = Flask(__name__)
app.register_blueprint(corona_patient_controller, url_prefix='/corona_patient_controller/')
app.register_blueprint(patients_details_controller, url_prefix='/patients_details_controller/')

CORS(app)


# @app.route('/api/data')
# def get_data():
#     data = {"message": "Hello from Flask!"}
#     return jsonify(data)

#
# @app.route('/corona-details-of-patients')
# def get_corona_patients_items():
#     data = [
#         {
#             "id": "123456789",
#             "corona_vaccines": [
#                 {"date": "1/1/2000", "manufacturer": "aaa"},
#                 {"date": "2/1/2000", "manufacturer": "bbb"},
#                 {"date": "3/1/2000", "manufacturer": "ccc"},
#                 {"date": "4/1/2000", "manufacturer": "ddd"}
#             ],
#             "positive": "10.10.2000",
#             "recovery": "11.11.2000"
#         },
#         {
#             "id": "222222222",
#             "corona_vaccines": [
#                 {"date": "1/1/2000", "manufacturer": "aaa"},
#                 {"date": "2/1/2000", "manufacturer": "bbb"},
#                 {"date": "3/1/2000", "manufacturer": "ccc"},
#                 {"date": "4/1/2000", "manufacturer": "ddd"}
#             ],
#             "positive": "10.10.2000",
#             "recovery": "11.11.2000"
#         },
#         {
#             "id": "333333333",
#             "corona_vaccines": [],
#             "positive": "---",
#             "recovery": "---"
#         }
#     ]
#     print(data[1])
#     return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
