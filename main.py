class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def set_numerator(self, numerator): #устанавливаем новое значение числителя
        self.numerator = numerator


    def set_denominator(self, denominator): #устанавливаем новое значение знаменателя
        self.denominator = denominator


    def get_numerator(self): # получаеММММММММММ значение числителя
        return self.numerator


    def get_denominator(self): # получаеМММ значение знаменателя
        return self.denominator


    def display_output(self):
        print(f'{self.numerator}/{self.denominator}')


    def sum_fraction(self, fraction67):
        if self.denominator == fraction67.get_denominator():
            new_numerator = self.numerator + fraction67.get_numerator()
            new_denominator = self.denominator
        else:
            new_numerator = self.numerator * fraction67.get_denominator() + fraction67.get_numerator() * self.denominator
            new_denominator = self.denominator * fraction67.get_denominator()
        return new_numerator, new_denominator


    def sub_fraction(self, fraction67):
        if self.denominator == fraction67.get_denominator():
            new_numerator = self.numerator - fraction67.get_numerator()
            new_denominator = self.denominator
        else:
            new_numerator = self.numerator * fraction67.get_denominator() - fraction67.get_numerator() * self.denominator
            new_denominator = self.denominator * fraction67.get_denominator()
        return new_numerator, new_denominator


    def mult_fraction(self, fraction67):
        new_numerator = self.numerator * fraction67.get_numerator()
        new_denominator = self.denominator * fraction67.get_denominator()
        return new_numerator, new_denominator


    def diva_fraction(self, fraction67):
        new_numerator = self.numerator * fraction67.get_denominator()
        new_denominator = self.denominator * fraction67.get_numerator()
        return new_numerator, new_denominator


# ККККлассссссс для конвертации температуры
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = celsius * 9/5 + 32
        return fahrenheit

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

class MetricToEnglishConverter:
    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * 0.621371


    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.60934


    @staticmethod
    def gallons_to_liters(gallongs):
        return gallongs * 3.78541


    @staticmethod
    def liters_to_gallons(liters):
        return liters * 0.264172

fraction1 = Fraction(4,8)
fraction2 = Fraction(1,2)
print(fraction1.sum_fraction(fraction2))
print(fraction1.sub_fraction(fraction2))
print(fraction1.mult_fraction(fraction2))
print(fraction1.diva_fraction(fraction2))

print(TemperatureConverter.celsius_to_fahrenheit(0))
print(TemperatureConverter.celsius_to_fahrenheit(100))
print(TemperatureConverter.celsius_to_fahrenheit(-40))
print(TemperatureConverter.fahrenheit_to_celsius(32))
print(TemperatureConverter.fahrenheit_to_celsius(212))
print(TemperatureConverter.fahrenheit_to_celsius(-40))

print(MetricToEnglishConverter.kilometers_to_miles(0))
print(MetricToEnglishConverter.kilometers_to_miles(100))
print(MetricToEnglishConverter.kilometers_to_miles(42.195))
print(MetricToEnglishConverter.miles_to_kilometers(0))
print(MetricToEnglishConverter.miles_to_kilometers(50))
print(MetricToEnglishConverter.miles_to_kilometers(26.2195))


print(MetricToEnglishConverter.gallons_to_liters(0))
print(MetricToEnglishConverter.gallons_to_liters(10))
print(MetricToEnglishConverter.gallons_to_liters(5.5))
print(MetricToEnglishConverter.liters_to_gallons(0))
print(MetricToEnglishConverter.liters_to_gallons(50))
print(MetricToEnglishConverter.liters_to_gallons(20.8194))