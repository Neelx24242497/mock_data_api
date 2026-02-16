from faker import Faker
from providers.medical import MedicalProvider
from providers.finance import FinanceProvider

class DataSynthesizer:
    def __init__(self, locale='en_US'):
        self.fake = Faker(locale)
        self.medical = MedicalProvider()
        self.finance = FinanceProvider()  # <--- UNCOMMENTED & ACTIVE

    def resolve_provider(self, path):
        """
        Decides if the string is for Medical, Finance, or Standard Faker.
        """
        # If the value is not a string (e.g. it's an integer), return it as is
        if not isinstance(path, str):
            return path

        try:
            # 1. Check for Custom Medical Provider
            if path.startswith("medical."):
                method_name = path.split(".")[1]
                return getattr(self.medical, method_name)()

            # 2. Check for Custom Finance Provider (NEW!)
            if path.startswith("finance."):
                method_name = path.split(".")[1]
                return getattr(self.finance, method_name)()

            # 3. Default to Standard Faker
            if "." in path:
                parts = path.split('.')
                func = self.fake
                for part in parts:
                    func = getattr(func, part)
                return func()
            
            # Simple Faker calls (like 'name' or 'email')
            return getattr(self.fake, path)()

        except AttributeError:
            return f"Error: '{path}' is not a valid data type."

    def generate_structure(self, template):
        """
        Recursive function to walk through nested dictionaries.
        """
        result = {}
        for key, value in template.items():
            if isinstance(value, dict):
                # RECURSION: Dive deeper if it's a dictionary
                result[key] = self.generate_structure(value)
            elif isinstance(value, list):
                # Handle lists
                result[key] = [self.resolve_provider(v) for v in value]
            else:
                # Base case: It's a string, so generate data
                result[key] = self.resolve_provider(value)
        return result

    def generate(self, schema: dict, count: int, seed: int = None):
        if seed:
            self.fake.seed_instance(seed)
        
        return [self.generate_structure(schema) for _ in range(count)]