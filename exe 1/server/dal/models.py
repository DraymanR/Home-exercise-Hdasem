class Patient:
    def __init__(self, id, first_name, last_name, house_number, street, city, phone):  # , mobil_phone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = {"city": city, "street": street, "house_number": house_number}
        self.phone = phone
        # self.mobil_phone = mobil_phone


class CoronaPatientDetails:
    def __init__(self, id):
        self.id = id
        self.recovery = ''
        self.positive = ''
        self.corona_vaccines = []
