from flask import jsonify, Blueprint, request

from services.corona_patient_details_CRUD import CoronaPatientDetailsCRUD

corona_patient_controller = Blueprint('corona_patient_controller', __name__)
corona_patient = CoronaPatientDetailsCRUD()


@corona_patient_controller.route("get_all")
def get_all():
    try:
        final = corona_patient.get_all()
        json_list = list(final)
        return jsonify(json_list), 200
    except Exception as error:
        return jsonify({"error": error}), 400


@corona_patient_controller.route("delete_patient/<_id>", methods=['DELETE'])
def delete_patient(_id):
    try:
        if _id.isnumeric() and len(_id) == 9:
            final = corona_patient.delete_patient(_id)
            return jsonify({"the server answered ": final}), 200
        else:
            return ({"message": "id is not valid"}), 400
    except Exception as error:
        return jsonify({"error": error}), 400


@corona_patient_controller.route('/edit_patient/<_id>', methods=['PUT'])
def edit_patient(_id):
    try:
        patient = request.get_json()
        final = corona_patient.edit_patient(patient)
        return jsonify({"the server answered ": final}), 200
    except Exception as error:
        return jsonify({"error": error}), 400


@corona_patient_controller.route('add_patient', methods=['POST'])
def add_patient():
    try:
        patient = request.get_json()
        final = corona_patient.add_patient(patient)
        return jsonify({"the server answered ": final}), 200
    except Exception as error:
        return jsonify({"error": error}), 400
