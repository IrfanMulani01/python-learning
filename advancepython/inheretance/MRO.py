'''What is MRO in Inheritance?

When a class inherits from one or more parent classes, MRO decides the order
in which Python will look for methods or attributes.

जेव्हा एखादा क्लास एक किंवा अधिक पॅरेंट क्लासकडून वारसा घेतो, तेव्हा Python MRO वापरून 
method/attribute शोधायचा क्रम ठरवतो.

MRO म्हणजे Method Resolution Order. हे एक क्रम आहे ज्यामध्ये Python वर्गांच्या 
वंशावळीमध्ये method आणि attribute शोधतो.
जेव्हा एखाद्या ऑब्जेक्टवर method कॉल केला जातो, तेव्हा Python प्रथम त्या ऑब्जेक्टच्या
वर्गात तपासतो, नंतर पॅरेंट क्लासेसमध्ये विशिष्ट क्रमाने तपासतो जोपर्यंत तो method सापडत नाही 
किंवा तो अस्तित्वात नसल्यास त्रुटी निर्माण करत नाही.

MRO stands for Method Resolution Order. It is the order in which Python
looks for methods and attributes in a hierarchy of classes.
When a method is called on an object, Python checks the class of
the object first, then checks the parent classes in a specific order
until it finds the method or raises an error if it doesn't exist.
MRO is crucial in inheritance, especially in multiple inheritance 
scenarios, to determine which method to execute when there are methods 
with the same name in different classes.
The MRO is determined by the C3 linearization algorithm, which ensures
a consistent order of classes in the hierarchy.
How MRO Works
When a class is defined, Python creates a method resolution order for that class.
This order is a linearization of the class hierarchy, ensuring that
each class appears only once and that parent classes are checked before child classes.
You can view the MRO of a class using the `__mro__` attribute or
the `mro()` method.
For example, if you have a class `C` that inherits from classes `A` and `B`, the 
MRO will be `[C, A, B]` if `A` is the parent of `B`.
This means that when you call a method on an instance of `C`, Python
will first look in `C`, then in `A`, and finally in `B`.
How to View MRO
You can view the MRO of a class using the `__mro__` attribute or   the `mro()` method.



Why MRO is important?
If multiple inheritance is used and two or more parents have
same method name, Python must decide which one to call first.

In multilevel inheritance, MRO ensures the method is picked 
from the correct parent in the chain.


How Python decides the order?

Python 3 uses C3 Linearization Algorithm:

Search in current class first.

Then move left to right in the inheritance list.

Go up to parent classes in the same order.

Skip duplicates.


MRO म्हणजे Python ला method शोधायचा निश्चित क्रम.

Single, Multilevel, Multiple — सगळ्यांमध्ये MRO लागू होतं.

Python 3 मध्ये C3 Linearization वापरून हा क्रम ठरवला जातो.

डावीकडून उजवीकडे priority असते.

Duplicate class पुन्हा तपासला जात नाही.




'''