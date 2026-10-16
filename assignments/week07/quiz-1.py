"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        area = self.length * self.width
        return f"area of Rectangle = {area}"

    # Method to get the perimeter
    def get_perimeter(self):
        perimeter = (self.length + self.width) * 2
        return f"perimeter of Rectangle = {perimeter}"


rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30

"""
เขียนคลาส วงกลม
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.141592653589

    # Method to get the area
    def get_area(self):
        area = self.pi * (self.radius * self.radius)
        return f"area of Circle = {area:.2f}"

    # Method to get the perimeter
    def get_perimeter(self):
        perimeter = (2 * self.pi) * self.radius
        return f"perimeter of Circle = {perimeter:.2f}"


myCircle = Circle(10)
print(myCircle.get_area())
print(myCircle.get_perimeter())