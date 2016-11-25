class Wine:
    def __init__(self, appellation, name, color, vintage, price, global_score):
        self.appellation = appellation
        self.name = name
        self.color = color
        self.vintage = vintage
        self.price = price
        self.global_score = global_score

    def get_appellation(self):
        return appellation

    def get_name(self):
        return name

    def get_vintage(self):
        return vintage

    def get_color(self):
        return color

    def get_price(self):
        return price

    def get_global_score(self):
        return global_score

    def __str__(self):
        return "bonjour"

    def __repr__(self):
        return self.appellation
