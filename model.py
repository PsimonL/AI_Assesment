class VolkswagenModel(object):

    def __init__(self, price, year, mileage, fuel):
        self.price = price
        self.year = year
        self.mileage = mileage
        self.fuel = fuel

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

        # Fuel
        text = self.fuel.replace(" ", "")
        text = text.replace("cm3", "")
        try:
            self.fuel = int(text)
        except ValueError:
            self.fuel = '-'

    def return_data(self):

        return ([self.price, self.year, self.mileage, self.fuel])
