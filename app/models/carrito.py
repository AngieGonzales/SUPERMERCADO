from app.models.product import Product

class Carrito:
    def __init__(self):
        self.carrito = []

    def add_product(self, product_id, quantity):
        product = Product.query.get(product_id)
        if product:
            item = {'product': product, 'quantity': quantity}
            self.carrito.append(item)

    def calculate_total(self):
        return sum(item['product'].priceProduct * item['quantity'] for item in self.carrito)
    
    def sizeD(self):   
        return len(self.carrito)

    def getItems(self):
        return self.carrito
    
    def clearcarrito(self):
        self.carrito = []