## 1. Method Overriding. Create a base class Animal with a method sound() that returns "Some sound". Override it in Dog, Cat, and Cow to return their specific sounds. Call sound() on a list of mixed animals.
# class animal():
#     def sound(self):
#         print( "some sound")
# class dog(animal):
#     def sound(self):
#         print( "dog can bark")
# class cat(animal):
#     def sound(self):
#         print( "cat can meoo")
# class cow(animal):
#     def sound(self):
#         print( "cow can mooo")
# a = animal()
# a.sound()
# d = dog()
# d.sound()
# c = cat()
# c.sound()
# co = cow()
# co.sound()

## 2. Operator Overloading. Create a Vector class with x and y attributes. Overload +, -, and * (scalar) operators. 
# Test with v1 + v2, v1 - v2, v1 * 3.
# class vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return vector(self.x + other.x, self.y + other.y)
#     def __sub__(self, other):
#         return vector(self.x - other.x, self.y - other.y)
#     def __mul__(self, other):
#         return vector(self.x * other.x, self.y * other.y)
#     def __str__(self):
#         return f"{self.x, self.y}"
# v = vector(5,7)
# v1 = vector(6,4)
# print(v + v1)
# print(v - v1)
# print(v * v1)

## 3. len() and str() Overloading. Build a Playlist class that holds songs. Overload __len__ to return song count and __str__ to print 
# all song names nicely.
# class paylist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []
#     def add_songs(self):
#         val = int(input("How many songs to add: "))
#         for i in range(val):
#             song = input(f"Enter song {i+1} name: ")
#             self.songs.append(song)
#     def __len__(self):
#         return len(self.songs)
#     def __str__(self):
#         result = f"\nPlaylist: {self.name}\n"
#         if len(self.songs) == 0:
#             print(f"Your playlist is empty")
#         else:
#             for i, song in enumerate(self.songs, 1):
#                 result += f"{i} {song}\n"
#             return result
# p = paylist("My favourites")
# p.add_songs()
# print(p)

## Duck Typing Polymorphism. Write a function process(obj) that calls obj.read(). 
# Create three unrelated classes — FileReader, DatabaseReader, APIReader — each with their own read() method. Pass all three to process() without any inheritance.
# class FileReader:
#     def read(self):
#         print("read the file")
#         return
# class DataBasereader:
#     def read(self):
#         return "database read"
# class APIReader:
#     def read(self):
#         return "api read"
# def process(obj):
#     obj.read()
# f = FileReader()
# d = DataBasereader()
# a = APIReader()
# process(f)
# process(d)
# process(a)

## 7. Method Overloading Simulation. Python doesn't support true method overloading. 
# Simulate it in an Calculator class where add() works with 2 integers, 3 integers, or a list of integers — using *args or singledispatch.
# class calculator:
#     def add(self, *args):
#         return f"{args}"
# class cal(calculator):
#     def add(self, *args):
#         return super().add()
# ca = cal()
# ca.add(1,2,3,4,5,6)

## Polymorphism Without Classes. Simulate polymorphism using only dictionaries of functions (no classes). Build a "strategy" dict 
# where keys are type names and values are handler functions. Show it's functionally equivalent to class-based polymorphism.
# def dog_speak():
#     print("Dog speak : bark")
#     return
# def cat_speak():
#     print("cat speak: meow")
#     return
# def cow_speak():
#     print("cow speak: mooo")
#     return

# strategy = {
#     "dog" : dog_speak(),
#     "cat" : cat_speak(),
#     "cow" : cow_speak()
# }

# strategy["dog"]
# strategy["cat"]
# strategy["cow"]


# ## Visitor Pattern
# Implement the Visitor design pattern:
# Shape hierarchy: Circle, Square, Triangle
# AreaVisitor and PerimeterVisitor compute values without modifying the shape classes
# Call shape.accept(visitor) polymorphically
# class shape:
#     def show(self):
#         print( "this is shape class")
# class circle(shape):
#     def show(self):
#         super().show()
#         print ("this is circle class\n")
# class square(shape):
#     def show(self):
#         super().show()
#         print ("this is square class\n")
# class triangle(shape):
#     def show(self):
#         super().show()
#         print ("this is triangle class\n")
# cc = circle()
# cc.show()
# s = square()
# s.show()
# t = triangle()
# t.show()