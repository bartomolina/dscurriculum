import statistics

class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        
    def add_item(self, name, price, quantity=1):
        for i in range(quantity):
            self.items.append({'name': name, 'price': price})
            self.total += price
        return self.total

    def mean_item_price(self):
        return self.total / len(self.items)

    def median_item_price(self):
        item_prices = [value['price'] for value in self.items]
        return statistics.median(item_prices)

    def apply_discount(self):
        #return "Sorry, there is no discount to apply to your cart :("
        if self.employee_discount is not None:
            return self.total * (100 - self.employee_discount) / 100
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if self.items:
            self.total -= self.items[-1]['price']
            self.items = self.items[:-1]
        else:
            print("There are no items in your cart!")