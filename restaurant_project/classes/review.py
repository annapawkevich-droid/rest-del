class Review:
    def __init__(self, customer, rating, comment):
        self.customer = customer
        self.rating = rating
        self.comment = comment

    def show(self):
        print(f"\n⭐ Відгук від {self.customer.name}: {self.rating}/5 — {self.comment}")
