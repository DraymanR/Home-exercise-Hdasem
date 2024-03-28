from flask import jsonify, Blueprint

from services.patients_details_CRUD import PatientDetailsCRUD

patients_details_controller = Blueprint('patients_details_controller', __name__)
patients_details = PatientDetailsCRUD()


@patients_details_controller.route("get_by_id/<_id>")
def get_by_id(_id):
    try:
        if _id.isnumeric() and len(_id) == 9:
            final = patients_details.get_by_id(_id)
            print(final)
            return jsonify(final), 200
        else:
            return ({"message": "id is not valid"}), 400
    except Exception as error:
        return jsonify({"error": error}), 400
