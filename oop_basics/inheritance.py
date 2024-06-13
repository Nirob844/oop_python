# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class 

class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'Running: {self.brand}'


class Laptop(Gadget):
    def __init__(self, brand, price, color, origin, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd
        super().__init__(brand, price, color, origin)

    def coding(self):
        return f'learning python and practicing'
    
    def __repr__(self) -> str:
        return f'Laptop {self.brand} {self.price} {self.color} {self.origin} {self.memory} {self.ssd}'
    
class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price} {self.dual_sim}'

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass


# inheritance
my_phone = Phone('iphone', 120000, 'silver', 'china', True)
my_laptop = Laptop('MacBook', 120000, 'silver', 'china', True, False)
print(my_phone)
print(my_laptop)