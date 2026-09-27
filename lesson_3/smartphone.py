class Smartphone:
    def __init__(self, brand, model, subscriber_number):
        self.brand=brand
        self.model=model
        self.subscriber_number=subscriber_number
    def __str__(self):
        return f"{self.brand} - {self.model}. {self.subscriber_number}"
