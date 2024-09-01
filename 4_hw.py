1.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(4, 5)
rect2 = Rectangle(6, 10)
rect3 = Rectangle(9, 3)

print(f"Прямоугольник 1 - Площадь: {rect1.area()}, Периметр: {rect1.perimeter()}")
print(f"Прямоугольник 2 - Площадь: {rect2.area()}, Периметр: {rect2.perimeter()}")
print(f"Прямоугольник 3 - Площадь: {rect3.area()}, Периметр: {rect3.perimeter()}")

2.
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(f"Результат сложения: {self.a + self.b}")

    def multiplication (self):
        print(f"Результат умножения: {self.a * self.b}")

    def division (self):
        print(f"Результат деления: {self.a / self.b}")

    def subtraction (self):
        print(f"Результат вычитания: {self.a - self.b}")

math = Math(20, 15)
math.addition()
math.multiplication()
math.division()
math.subtraction()

3. 
class Button:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"

button_text_box = Button("Text Box")
button_check_box = Button("Check Box")
button_radio_button = Button("Radio Button")
button_web_tables = Button("Web Tables")
button_buttons = Button("Buttons")

print(button_text_box.text)
print(button_check_box.text)
print(button_radio_button.text)
print(button_web_tables.text)
print(button_buttons.text)

print(button_text_box.click())
print(button_check_box.click())
print(button_radio_button.click())
print(button_web_tables.click())
print(button_buttons.click())
