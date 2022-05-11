class Dates:
    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    @staticmethod
    def to_dash_date(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
date_from_DB = "15/12/2016"
date_with_dash = Dates.to_dash_date(date_from_DB)

if date.get_date() == date_with_dash:
    print("Equal")
else:
    print("Unequal")
