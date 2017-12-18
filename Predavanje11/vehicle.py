class Vehicle(object):

    def __init__(self, brand, model, km_so_far, last_general_service_date):
        self.brand = brand
        self.model = model
        self.km_so_far = km_so_far
        self.last_general_service_date = last_general_service_date

    def __str__(self):
        return self.brand + " " + self.model

    def update_km(self, km):
        self.km_so_far += km # a = a + b => a += b


def list_all_vehicles(vehicles):

    for vehicle in vehicles:
        print vehicle


def add_new_vehicle(vehicles):
    brand = raw_input("Please enter vehicle brand: ")
    model = raw_input("Please enter vehicle model: ")
    km_so_far = int(raw_input("Please enter how much km vehicle has so far: "))
    last_general_service_date = raw_input("Please enter last service date: ")

    vehicle = Vehicle(brand, model, km_so_far, last_general_service_date)
    vehicles.append(vehicle)

    return vehicles


def edit_vehicles(vehicles):


    for i, vehicle in enumerate(vehicles):
        print i, vehicle

    vehicle_index = int(raw_input("What vehicle do you want to edit? "))

    vehicle = vehicles[vehicle_index]

    km = int(raw_input("How much km has he travelled? "))
    vehicle.update_km(km)
    print vehicle.km_so_far

    return vehicles



if __name__ == '__main__':

    fiat = Vehicle('fiat', 'uno', 200000, '12/8/2017')
    ford = Vehicle('ford', 'mondeo', 150000, '12/8/2017')

    vehicles = [fiat, ford]

    while True:

        print "1) List all vehicles"
        print "2) Add new vehicle"
        print "3) Edit vehicle"
        print "4) Exit"

        option = raw_input("Please choose an option[1, 2, 3, 4]: ")

        if option == '1':
            list_all_vehicles(vehicles)
        elif option == '2':
            vehicles = add_new_vehicle(vehicles)
        elif option == '3':
            vehicles = edit_vehicles(vehicles)
        elif option == '4':
            break