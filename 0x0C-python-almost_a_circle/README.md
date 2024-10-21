This function is the first class Base.

This function is the class Rectangle that inherits from Base.

This function updates the class Rectangle by adding validation of all setter methods and instantiation (id excluded).

This function updates the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

This function updates the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # without handling x and y.

This function updates the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.

This function updates  the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y.

This function updates the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:
1st argument should be the id attribute
2nd argument should be the width attribute
3rd argument should be the height attribute
4th argument should be the x attribute
5th argument should be the y attribute

This function updates the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.

This function writes the class Square that inherits from Rectangle.

This function updates the class Square by adding the public getter and setter size.

This function updates  the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

*args is the list of arguments - no-keyworded arguments
1st argument should be the id attribute
2nd argument should be the size attribute
3rd argument should be the x attribute
4th argument should be the y attribute

This function updates Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:
This dictionary contains:
id
width
height
x
y

This function updates Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:
This dictionary contains:
id
size
x
y

This function updates the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries.

This function updates the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file.

This function updates the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string.

This function updates the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set.


