from dal.models import CoronaPatientDetails


class CoronaPatientDetailsCRUD():
    # data = [
    #     {
    #         "id": "123456789",
    #         "corona_vaccines": [
    #             {"date": "1/1/2000", "manufacturer": "aaa"},
    #             {"date": "2/1/2000", "manufacturer": "bbb"},
    #             {"date": "3/1/2000", "manufacturer": "ccc"},
    #             {"date": "4/1/2000", "manufacturer": "ddd"}
    #         ],
    #         "positive": "10.10.2000",
    #         "recovery": "11.11.2000"
    #     },
    #     {
    #         "id": "222222222",
    #         "corona_vaccines": [
    #             {"date": "1/1/2000", "manufacturer": "aaa"},
    #             {"date": "2/1/2000", "manufacturer": "bbb"},
    #             {"date": "3/1/2000", "manufacturer": "ccc"},
    #             {"date": "4/1/2000", "manufacturer": "ddd"}
    #         ],
    #         "positive": "10.10.2000",
    #         "recovery": "11.11.2000"
    #     },
    #     {
    #         "id": "333333333",
    #         "corona_vaccines": [],
    #         "positive": "---",
    #         "recovery": "---"
    #     }
    # ]

    def __init__(self):
        self.corona_patient_details = [
            {
                "id": "123456789",
                "corona_vaccines": [
                    {"date": "1/1/2000", "manufacturer": "aaa"},
                    {"date": "2/1/2000", "manufacturer": "bbb"},
                    {"date": "3/1/2000", "manufacturer": "ccc"},
                    {"date": "4/1/2000", "manufacturer": "ddd"}
                ],
                "positive": "10.10.2000",
                "recovery": "11.11.2000"
            },
            {
                "id": "222222222",
                "corona_vaccines": [
                    {"date": "1/1/2000", "manufacturer": "aaa"},
                    {"date": "2/1/2000", "manufacturer": "bbb"},
                    {"date": "3/1/2000", "manufacturer": "ccc"},
                    {"date": "4/1/2000", "manufacturer": "ddd"}
                ],
                "positive": "10.10.2000",
                "recovery": "11.11.2000"
            },
            {
                "id": "333333333",
                "corona_vaccines": [],
                "positive": "---",
                "recovery": "---"
            }
        ]

    def get_all(self):
        # self.corona_patient_details = data
        return self.corona_patient_details

    def delete_patient(self, _id):
        for i, obj in enumerate(self.corona_patient_details):
            if self.corona_patient_details[i]["id"] == _id:
                self.corona_patient_details.remove(self.corona_patient_details[i])
        return "patient was deleted successfully"

    def add_patient(self, patient):
        self.corona_patient_details.append(patient)
        return "patient was add successfully"

    def edit_patient(self, patient):
        index = -1
        for i, obj in enumerate(self.corona_patient_details):
            if self.corona_patient_details[i]["id"] == patient["id"]:
                index = i
        if index != -1:
            self.corona_patient_details[index] = patient
        else:
            self.corona_patient_details.append(patient)
        return "patient was update successfully"
