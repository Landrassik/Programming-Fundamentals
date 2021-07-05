class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, name):
        self.products.append(name)

    def get_by_letter(self, first_letter):
        first_letter = [i for i in self.products if i[0] == first_letter]
        return first_letter

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        sort_products = sorted(self.products)
        result += "\n".join(sort_products)
        return result

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
