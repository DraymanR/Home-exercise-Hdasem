class PatientDetailsCRUD():
    def __init__(self):
        self.patients_details = [{"id": "123456789", "firstName": "avi", "lastName": "choen",
                                  "address": {"city": "jerusalem", "street": "srtaus", "houseNumber": "10"},
                                  "dateOfBirth": "1.1.2000", "phone": "02-1234567", "mobilePhone": "055-1234567"},
                                 {"id": "222222222", "firstName": "avi", "lastName": "choen",
                                  "address": {"city": "jerusalem", "street": "srtaus", "houseNumber": "10"},
                                  "dateOfBirth": "1.1.2000", "phone": "02-1234567", "mobilePhone": "055-1234567"},
                                 {"id": "333333333", "firstName": "avi", "lastName": "choen",
                                  "address": {"city": "jerusalem", "street": "srtaus", "houseNumber": "10"},
                                  "dateOfBirth": "1.1.2000", "phone": "02-1234567", "mobilePhone": "055-1234567"}
                                 ]

    def get_by_id(self, _id):
        for i, obj in enumerate(self.patients_details):
            if self.patients_details[i]["id"] == _id:
                return self.patients_details[i]
        return "id not available"
