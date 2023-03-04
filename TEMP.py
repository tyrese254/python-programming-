class Temperature:
    def __init__(self,fahrenheit,celsius):
        self.fahrenheit=fahrenheit
        self.celsius=celsius
    def farhrenheit(self):
        return (self.fahrenheit-32)*5/9
    def celsius(self):
        return (self.celsius*9/5)+32
    
t=Temperature(12,8)
print(t.fahrenheit())
print(t.celsius)