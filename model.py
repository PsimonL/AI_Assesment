class VolkswagenModel(object):

    list_of_models = ["181", "Amarok", "Arteon", "Atlas", "Beetle", "Bora", "Buggy", "Caddy", "California", "Caravelle", "CC", "Corrado", "Crafter", "Eos", "Fox", "Garbus", "Golf", "Golf Plus", "Golf Sportsvan", "ID.3", "ID.4", "ID.5", "ID.6", "ID.Buzz", "Iltis", 
        "Jetta", "Kafer", "Karmann Ghia", "LT", "Lupo", "Multivan", "New Beetle", "Passat", "Passat CC", "Phaeton", "Polo", "Routan", "Santana", "Scirocco", "Sharan", "T-Cross", "T-Roc", "Taigo", "Teramont", "Tiguan", "Tiguan Allspace", "Touareg", "Touran", "Transporter", "up!", "Vento"]

    def __init__(self, price, year, mileage, capacity, fuel, model, estimation):

        self.price = price
        self.year = year
        self.mileage = mileage
        self.capacity = capacity
        self.fuel = fuel
        self.model = model
        self.estimation = estimation

    def clean_data(self):

        # Price
        text = self.price.replace(" ", "")
        text = text.replace("PLN", "")
        try:
            self.price = int(text)
        except ValueError:
            self.price = '-'

        # Year
        try:
            self.year = int(self.year)
        except ValueError:
            self.year = '-'

        # Mileage
        text = self.mileage.replace(" ", "")
        text = text.replace("km", "")
        try:
            self.mileage = int(text)
        except ValueError:
            self.mileage = '-'

        # Fuel capacity
        text = self.capacity.replace(" ", "")
        text = text.replace("cm3", "")
        try:
            self.capacity = int(text)
        except ValueError:
            self.capacity = '-'

        # Fuel type
        text = self.fuel
        if text == "Benzyna": self.fuel = int(0)
        else: self.fuel = int(1)

        # Model
        check = False
        for i, model in enumerate(self.list_of_models):
            if model in self.model:
                self.model = str(i)
                check = True
        if check == False: self.model = '-'
        else: self.model = int(self.model)

        # Estimation
        # 0 -> Below average
        # 1 -> Within average
        # 2 -> Above average
        # - -> Lack of data
        if self.estimation == "Poniżej średniej": self.estimation = int(0)
        if self.estimation == "W granicach średniej": self.estimation = int(1)
        if self.estimation == "Powyżej średniej": self.estimation = int(2)

    def return_data(self):

        return ([self.price, self.year, self.mileage, self.capacity, self.fuel, self.model, self.estimation])
