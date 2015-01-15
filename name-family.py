–
Design and implement a class named “Student” with three methods;
•
__
init
__(self, name, family)
•
addCourseMark
(self, course, mark)
•
average(self)
Then test the class with an instance. The details like member variables are up
to you. For example, you can use lists or dictionaries to implement the class.
You can utilize this code (that uses a dictionary) too:
class Student:
courseMarks
={}
name= ""
def
__
init
__(self, name, family):
...
def
addCourseMark
(self, course, mark):
self.courseMarks
[course] = mark
def
average(self
):
...
