import unittest

class Product:

    def __init__(self, name, price, quantity) -> None:
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):

        if self.quantity < 0:
            raise ValueError

        return self.price * self.quantity
    

class ShoppingCart:

    def __init__(self) -> None:
        self.cart = []
    
    def add_product(self, product: Product):
        
        self.cart.append(product)
    
    def get_cart_total(self):



        total = 0

        for item in self.cart:
            
            total += item.calculate_total()
        
        return total 
    

class TestShoppingCart(unittest.TestCase):

    def test_integration(self):
        
        product1 = Product("Product 1", 10, 2)
        product2 = Product("Product 2", 5, 3)

        
        cart = ShoppingCart()

        
        cart.add_product(product1)
        cart.add_product(product2)

        self.assertEqual(cart.get_cart_total(), 35)



    



class TestProduct(unittest.TestCase):

    def test_calculate_total(self):
        product = Product("banana", 10, 5)
        self.assertEqual(product.calculate_total(), 50)

    def test_calculate_total_with_zero(self):

        product = Product('orange' , 5, 0)
        self.assertEqual(product.calculate_total() , 0)

    def test_calculate_total_negative_quantity(self):

        product = Product('apple', 15.0, -1)

        with self.assertRaises(ValueError):
            total = product.calculate_total()

if __name__ == '__main__':
    unittest.main()
