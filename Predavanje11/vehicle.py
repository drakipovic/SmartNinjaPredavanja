class Vehicle(object):

    def __init__(self, brand, model, km_so_far, last_general_service_date):
        self.brand = brand
        self.model = model
        self.km_so_far = km_so_far
        self.last_general_service_date = last_general_service_date

    def __str__(self):
        return self.brand + " " + self.model


def list_all_vehicles(vehicles):

    for vehicle in vehicles:
        print vehicle


if __name__ == '__main__':

    fiat = Vehicle('fiat', 'uno', 200000, '12/8/2017')
    ford = Vehicle('ford', 'mondeo', 150000, '12/8/2017')

    vehicles = [fiat, ford]

    list_all_vehicles(vehicles)