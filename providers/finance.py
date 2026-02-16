from faker import Faker
import random

class FinanceProvider:
    def __init__(self):
        self.fake = Faker()

    def credit_card(self):
        # Faker has excellent built-in credit card support
        return self.fake.credit_card_number()

    def iban(self):
        return self.fake.iban()

    def amount(self):
        # Generates a realistic transaction amount between 10.00 and 5000.00
        return round(random.uniform(10.00, 5000.00), 2)

    def currency(self):
        return random.choice(["USD", "EUR", "GBP", "JPY", "AUD"])

    def crypto_address(self):
        # Simulates a Bitcoin address
        return "bc1" + self.fake.pystr(min_chars=26, max_chars=35)

    def transaction_status(self):
        return random.choices(
            ["success", "pending", "failed", "declined"], 
            weights=[70, 20, 5, 5]
        )[0]