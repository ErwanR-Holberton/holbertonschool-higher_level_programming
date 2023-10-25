# Python - Almost a circle

<h2>Background Context</h2>

<p>In this project, you will review everything about Python:</p>

<ul>
<li>Import</li>
<li>Exceptions</li>
<li>Class</li>
<li>Private attribute</li>
<li>Getter/Setter</li>
<li>Class method</li>
<li>Static method</li>
<li>Inheritance</li>
<li>Unittest</li>
<li>Read/Write file</li>
</ul>

<p>You will also learn about:</p>

<ul>
<li><code>args</code> and <code>kwargs</code></li>
<li>Serialization/Deserialization</li>
<li>JSON</li>
</ul>

<video autoplay="" loop="">
<source type="video/mp4" src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/331/giphy.mp4">
</video>

<h2>Step by step</h2>

<ul>
<li>Write the first class Base</li>
<li>Write the class Rectangle that inherits from Base</li>
<li>Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)</li>
<li>Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance</li>
<li>Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here</li>
<li>Update the class Rectangle by overriding the str method so that it returns [Rectangle] instance</li>
<li>Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y</li>
<li>Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute</li>
<li>Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, kwargs) that assigns a key/value argument to attributes</li>
<li>Write the class Square that inherits from Rectangle</li>
<li>Update the class Square by adding the public getter and setter size</li>
<li>Update the class Square by adding the public method def update(self, *args, kwargs) that assigns attributes</li>
<li>Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle</li>
<li>Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square</li>
<li>Update the class Base by adding the class method def save<em>to</em>file(cls, list<em>objs): that writes the JSON string representation of list</em>objs to a file</li>
<li>Update the class Base by adding the static method def from<em>json</em>string(json<em>string): that returns the list of the JSON string representation json</em>string</li>
<li>Update the class Base by adding the class method def create(cls, dictionary): that returns an instance with all attributes already set</li>
<li>Update the class Base by adding the class method def load<em>from</em>file(cls): that returns a list of instances</li>
</ul>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/1VFpovKWOxo91RtP2lebZg" title="args/kwargs" target="_blank">args/kwargs</a> </li>
<li><a href="/rltoken/DfJsuOTXTv2t7ycPfEXZuw" title="JSON encoder and decoder" target="_blank">JSON encoder and decoder</a> </li>
<li><a href="/rltoken/_jqAzT_nImg88Bk36NHjMw" title="unittest module" target="_blank">unittest module</a> </li>
<li><a href="/rltoken/n7aJtd_G82AIQ9hxMg7nng" title="Python test cheatsheet" target="_blank">Python test cheatsheet</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/H-uthlOO7nk1vorFnZtI7A" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should be documented: <code>python3 -c 'print(__import__("my_module").__doc__)'</code></li>
<li>All your classes should be documented: <code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code></li>
<li>All your functions (inside and outside a class) should be documented: <code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code></li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>Python Unit Tests</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/_jqAzT_nImg88Bk36NHjMw" title="unittest module" target="_blank">unittest module</a> </li>
<li>All your test files should be python files (extension: <code>.py</code>)</li>
<li>All your test files and folders should start with <code>test_</code></li>
<li>Your file organization in the tests folder should be the same as your project: ex: for <code>models/base.py</code>, unit tests must be in: <code>tests/test_models/test_base.py</code></li>
<li>All your tests should be executed by using this command: <code>python3 -m unittest discover tests</code></li>
<li>You can also test file by file by using this command: <code>python3 -m unittest tests/test_models/test_base.py</code></li>
<li>We strongly encourage you to work together on test cases so that you don’t miss any edge case</li>
</ul>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. If it's not tested it doesn't work
</h3>

All your files, classes and methods must be unit tested and be PEP 8 validated. </p>

<pre><code>guillaume@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/$
</code></pre>

<p><em>Note that this is just an example. The number of tests you create can be different from the above example.</em></p>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>tests/</code></li>
</ul>
</div>

<h3 class="panel-title">
1. Base class
</h3>

Write the first class <code>Base</code>:</p>

<p>Create a folder named <code>models</code> with an empty file <code>__init__.py</code> inside - with this file, the folder will become a Python package</p>

<p>Create a file named <code>models/base.py</code>:</p>

<ul>
<li>Class <code>Base</code>:

<ul>
<li>private class attribute <code>__nb_objects = 0</code></li>
<li>class constructor: <code>def __init__(self, id=None):</code>:

<ul>
<li>if <code>id</code> is not <code>None</code>, assign the public instance attribute <code>id</code> with this argument value - you can assume <code>id</code> is an integer and you don’t need to test the type of it</li>
<li>otherwise, increment <code>__nb_objects</code> and assign the new value to the public instance attribute <code>id</code></li>
</ul></li>
</ul></li>
</ul>

<p>This class will be the “base” of all other classes in this project. The goal of it is to manage <code>id</code> attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)</p>

<pre><code>guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

b1 = Base()
print(b1.id)

b2 = Base()
print(b2.id)

b3 = Base()
print(b3.id)

b4 = Base(12)
print(b4.id)

b5 = Base()
print(b5.id)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/base.py, models/__init__.py</code></li>
</ul>
</div>

<h3 class="panel-title">
2. First Rectangle
</h3>

Write the class <code>Rectangle</code> that inherits from <code>Base</code>:</p>

<ul>
<li>In the file <code>models/rectangle.py</code></li>
<li>Class <code>Rectangle</code> inherits from <code>Base</code></li>
<li>Private instance attributes, each with its own public getter and setter:

<ul>
<li><code>__width</code> -> <code>width</code></li>
<li><code>__height</code> -> <code>height</code></li>
<li><code>__x</code> -> <code>x</code></li>
<li><code>__y</code> -> <code>y</code></li>
</ul></li>
<li>Class constructor: <code>def __init__(self, width, height, x=0, y=0, id=None)</code>:

<ul>
<li>Call the super class with <code>id</code> - this super call with use the logic of the <code>__init__</code> of the <code>Base</code> class</li>
<li>Assign each argument <code>width</code>, <code>height</code>, <code>x</code> and <code>y</code> to the right attribute</li>
</ul></li>
</ul>

<p>Why private attributes with getter/setter? Why not directly public attribute?</p>

<p>Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.</p>

<pre><code>guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)

guillaume@ubuntu:~/$ ./1-main.py
1
2
12
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/rectangle.py</code></li>
</ul>
</div>

<h3 class="panel-title">
3. Validate attributes
</h3>

Update the class <code>Rectangle</code> by adding validation of all setter methods and instantiation (<code>id</code> excluded):</p>

<ul>
<li>If the input is not an integer, raise the <code>TypeError</code> exception with the message: <code><name of the attribute> must be an integer</code>. Example: <code>width must be an integer</code></li>
<li>If <code>width</code> or <code>height</code> is under or equals 0, raise the <code>ValueError</code> exception with the message: <code><name of the attribute> must be > 0</code>. Example: <code>width must be > 0</code></li>
<li>If <code>x</code> or <code>y</code> is under 0, raise the <code>ValueError</code> exception with the message: <code><name of the attribute> must be >= 0</code>. Example: <code>x must be >= 0</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

try:
Rectangle(10, "2")
except Exception as e:
print("[{}] {}".format(e.__class__.__name__, e))

try:
r = Rectangle(10, 2)
r.width = -10
except Exception as e:
print("[{}] {}".format(e.__class__.__name__, e))

try:
r = Rectangle(10, 2)
r.x = {}
except Exception as e:
print("[{}] {}".format(e.__class__.__name__, e))

try:
Rectangle(10, 2, 3, -1)
except Exception as e:
print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be > 0
[TypeError] x must be an integer
[ValueError] y must be >= 0
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/rectangle.py</code></li>
</ul>
</div>

<h3 class="panel-title">
4. Area first
</h3>

Update the class <code>Rectangle</code> by adding the public method <code>def area(self):</code> that returns the area value of the <code>Rectangle</code> instance.</p>

<pre><code>guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(3, 2)
print(r1.area())

r2 = Rectangle(2, 10)
print(r2.area())

r3 = Rectangle(8, 7, 0, 0, 12)
print(r3.area())

guillaume@ubuntu:~/$ ./3-main.py
6
20
56
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/rectangle.py</code></li>
</ul>
</div>

<h3 class="panel-title">
5. Display #0
</h3>

Update the class <code>Rectangle</code> by adding the public method <code>def display(self):</code> that prints in stdout the <code>Rectangle</code> instance with the character <code>#</code> - you don’t need to handle <code>x</code> and <code>y</code> here.</p>

<pre><code>guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(4, 6)
r1.display()

print("---")

r1 = Rectangle(2, 2)
r1.display()

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####
####
####
---
##
##
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/rectangle.py</code></li>
</ul>
</div>

<h3 class="panel-title">
6. __str__
</h3>

Update the class <code>Rectangle</code> by overriding the <code>__str__</code> method so that it returns <code>[Rectangle] (<id>) <x>/<y> - <width>/<height></code></p>

<pre><code>guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(4, 6, 2, 1, 12)
print(r1)

r2 = Rectangle(5, 5, 1)
print(r2)

guillaume@ubuntu:~/$ ./5-main.py
[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/rectangle.py</code></li>
</ul>
</div>

<h3 class="panel-title">
7. Display #1
</h3>

Update the class <code>Rectangle</code> by improving the public method <code>def display(self):</code> to print in stdout the <code>Rectangle</code> instance with the character <code>#</code> by taking care of <code>x</code> and <code>y</code></p>

<pre><code>guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(2, 3, 2, 2)
r1.display()

print("---")

r2 = Rectangle(3, 2, 1, 0)
r2.display()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
$
$
##$
##$
##$
---$
###$
###$
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/rectangle.py</code></li>
</ul>
</div>

<h3 class="panel-title">
8. Update #0
</h3>

Update the class <code>Rectangle</code> by adding the public method <code>def update(self, *args):</code> that assigns an argument to each attribute:</p>

<ul>
<li>1st argument should be the <code>id</code> attribute</li>
<li>2nd argument should be the <code>width</code> attribute</li>
<li>3rd argument should be the <code>height</code> attribute</li>
<li>4th argument should be the <code>x</code> attribute</li>
<li>5th argument should be the <code>y</code> attribute</li>
</ul>

<p>This type of argument is called a “no-keyword argument” - Argument order is super important.</p>

<pre><code>guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(89)
print(r1)

r1.update(89, 2)
print(r1)

r1.update(89, 2, 3)
print(r1)

r1.update(89, 2, 3, 4)
print(r1)

r1.update(89, 2, 3, 4, 5)
print(r1)

guillaume@ubuntu:~/$ ./7-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/3
[Rectangle] (89) 4/10 - 2/3
[Rectangle] (89) 4/5 - 2/3
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/rectangle.py</code></li>
</ul>
</div>

<h3 class="panel-title">
9. Update #1
</h3>

Update the class <code>Rectangle</code> by updating the public method <code>def update(self, *args):</code> by changing the prototype to <code>update(self, *args, **kwargs)</code> that assigns a key/value argument to attributes:</p>

<ul>
<li><code>**kwargs</code> can be thought of as a double pointer to a dictionary: key/value

<ul>
<li>As Python doesn’t have pointers, <code>**kwargs</code> is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with</li>
</ul></li>
<li><code>**kwargs</code> must be skipped if <code>*args</code> exists and is not empty</li>
<li>Each key in this dictionary represents an attribute to the instance</li>
</ul>

<p>This type of argument is called a “key-worded argument”. Argument order is not important.</p>

<pre><code>guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(height=1)
print(r1)

r1.update(width=1, x=2)
print(r1)

r1.update(y=1, width=2, x=3, id=89)
print(r1)

r1.update(x=1, height=2, y=3, width=4)
print(r1)

guillaume@ubuntu:~/$ ./8-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (1) 10/10 - 10/1
[Rectangle] (1) 2/10 - 1/1
[Rectangle] (89) 3/1 - 2/1
[Rectangle] (89) 1/3 - 4/2
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/rectangle.py</code></li>
</ul>
</div>

<h3 class="panel-title">
10. And now, the Square!
</h3>

Write the class <code>Square</code> that inherits from <code>Rectangle</code>:</p>

<ul>
<li>In the file <code>models/square.py</code></li>
<li>Class <code>Square</code> inherits from <code>Rectangle</code></li>
<li>Class constructor: <code>def __init__(self, size, x=0, y=0, id=None):</code>:

<ul>
<li>Call the super class with <code>id</code>, <code>x</code>, <code>y</code>, <code>width</code> and <code>height</code> - this super call will use the logic of the <code>__init__</code> of the <code>Rectangle</code> class. The <code>width</code> and <code>height</code> must be assigned to the value of <code>size</code></li>
<li>You must not create new attributes for this class, use all attributes of <code>Rectangle</code> - As reminder: a Square is a Rectangle with the same width and height</li>
<li>All <code>width</code>, <code>height</code>, <code>x</code> and <code>y</code> validation must inherit from <code>Rectangle</code> - same behavior in case of wrong data</li>
</ul></li>
<li>The overloading <code>__str__</code> method should return <code>[Square] (<id>) <x>/<y> - <size></code> - in our case, <code>width</code> or <code>height</code></li>
</ul>

<p>As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.</p>

<pre><code>guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

s1 = Square(5)
print(s1)
print(s1.area())
s1.display()

print("---")

s2 = Square(2, 2)
print(s2)
print(s2.area())
s2.display()

print("---")

s3 = Square(3, 1, 3)
print(s3)
print(s3.area())
s3.display()

guillaume@ubuntu:~/$ ./9-main.py
[Square] (1) 0/0 - 5
25
#####
#####
#####
#####
#####
---
[Square] (2) 2/0 - 2
4
##
##
---
[Square] (3) 1/3 - 3
9



###
###
###
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/square.py</code></li>
</ul>
</div>

<h3 class="panel-title">
11. Square size
</h3>

Update the class <code>Square</code> by adding the public getter and setter <code>size</code></p>

<ul>
<li>The setter should assign (in this order) the <code>width</code> and the <code>height</code> - with the same value</li>
<li>The setter should have the same value validation as the <code>Rectangle</code> for <code>width</code> and <code>height</code> - No need to change the exception error message (It should be the one from <code>width</code>)</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

s1 = Square(5)
print(s1)
print(s1.size)
s1.size = 10
print(s1)

try:
s1.size = "9"
except Exception as e:
print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./10-main.py
[Square] (1) 0/0 - 5
5
[Square] (1) 0/0 - 10
[TypeError] width must be an integer
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/square.py</code></li>
</ul>
</div>

<h3 class="panel-title">
12. Square update
</h3>

Update the class <code>Square</code> by adding the public method <code>def update(self, *args, **kwargs)</code> that assigns attributes:</p>

<ul>
<li><code>*args</code> is the list of arguments - no-keyworded arguments

<ul>
<li>1st argument should be the <code>id</code> attribute</li>
<li>2nd argument should be the <code>size</code> attribute</li>
<li>3rd argument should be the <code>x</code> attribute</li>
<li>4th argument should be the <code>y</code> attribute</li>
</ul></li>
<li><code>**kwargs</code> can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)</li>
<li><code>**kwargs</code> must be skipped if *args exists and is not empty</li>
<li>Each key in this dictionary represents an attribute to the instance</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

s1 = Square(5)
print(s1)

s1.update(10)
print(s1)

s1.update(1, 2)
print(s1)

s1.update(1, 2, 3)
print(s1)

s1.update(1, 2, 3, 4)
print(s1)

s1.update(x=12)
print(s1)

s1.update(size=7, y=1)
print(s1)

s1.update(size=7, id=89, y=1)
print(s1)

guillaume@ubuntu:~/$ ./11-main.py
[Square] (1) 0/0 - 5
[Square] (10) 0/0 - 5
[Square] (1) 0/0 - 2
[Square] (1) 3/0 - 2
[Square] (1) 3/4 - 2
[Square] (1) 12/4 - 2
[Square] (1) 12/1 - 7
[Square] (89) 12/1 - 7
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/square.py</code></li>
</ul>
</div>

<h3 class="panel-title">
13. Rectangle instance to dictionary representation
</h3>

Update the class <code>Rectangle</code> by adding the public method <code>def to_dictionary(self):</code> that returns the dictionary representation of a <code>Rectangle</code>:</p>

<p>This dictionary must contain:</p>

<ul>
<li><code>id</code></li>
<li><code>width</code></li>
<li><code>height</code></li>
<li><code>x</code></li>
<li><code>y</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 12-main.py
#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(10, 2, 1, 9)
print(r1)
r1_dictionary = r1.to_dictionary()
print(r1_dictionary)
print(type(r1_dictionary))

r2 = Rectangle(1, 1)
print(r2)
r2.update(**r1_dictionary)
print(r2)
print(r1 == r2)

guillaume@ubuntu:~/$ ./12-main.py
[Rectangle] (1) 1/9 - 10/2
{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
<class 'dict'>
[Rectangle] (2) 0/0 - 1/1
[Rectangle] (1) 1/9 - 10/2
False
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/rectangle.py</code></li>
</ul>
</div>

<h3 class="panel-title">
14. Square instance to dictionary representation
</h3>

Update the class <code>Square</code> by adding the public method <code>def to_dictionary(self):</code> that returns the dictionary representation of a <code>Square</code>:</p>

<p>This dictionary must contain:</p>

<ul>
<li><code>id</code></li>
<li><code>size</code></li>
<li><code>x</code></li>
<li><code>y</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 13-main.py
#!/usr/bin/python3
""" 13-main """
from models.square import Square

if __name__ == "__main__":

s1 = Square(10, 2, 1)
print(s1)
s1_dictionary = s1.to_dictionary()
print(s1_dictionary)
print(type(s1_dictionary))

s2 = Square(1, 1)
print(s2)
s2.update(**s1_dictionary)
print(s2)
print(s1 == s2)

guillaume@ubuntu:~/$ ./13-main.py
[Square] (1) 2/1 - 10
{'id': 1, 'x': 2, 'size': 10, 'y': 1}
<class 'dict'>
[Square] (2) 1/0 - 1
[Square] (1) 2/1 - 10
False
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/square.py</code></li>
</ul>
</div>

<h3 class="panel-title">
15. Dictionary to JSON string
</h3>

JSON is one of the standard formats for sharing data representation.</p>

<p>Update the class <code>Base</code> by adding the static method <code>def to_json_string(list_dictionaries):</code> that returns the JSON string representation of <code>list_dictionaries</code>:</p>

<ul>
<li><code>list_dictionaries</code> is a list of dictionaries</li>
<li>If <code>list_dictionaries</code> is <code>None</code> or empty, return the string: <code>"[]"</code></li>
<li>Otherwise, return the JSON string representation of <code>list_dictionaries</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 14-main.py
#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(10, 7, 2, 8)
dictionary = r1.to_dictionary()
json_dictionary = Base.to_json_string([dictionary])
print(dictionary)
print(type(dictionary))
print(json_dictionary)
print(type(json_dictionary))

guillaume@ubuntu:~/$ ./14-main.py
{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
<class 'dict'>
[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
<class 'str'>
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/base.py</code></li>
</ul>
</div>

<h3 class="panel-title">
16. JSON string to file
</h3>

Update the class <code>Base</code> by adding the class method <code>def save_to_file(cls, list_objs):</code> that writes the JSON string representation of <code>list_objs</code> to a file:</p>

<ul>
<li><code>list_objs</code> is a list of instances who inherits of <code>Base</code> - example: list of <code>Rectangle</code> or list of <code>Square</code> instances</li>
<li>If <code>list_objs</code> is <code>None</code>, save an empty list</li>
<li>The filename must be: <code><Class name>.json</code> - example: <code>Rectangle.json</code></li>
<li>You must use the static method <code>to_json_string</code> (created before)</li>
<li>You must overwrite the file if it already exists</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 15-main.py
#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
Rectangle.save_to_file([r1, r2])

with open("Rectangle.json", "r") as file:
print(file.read())

guillaume@ubuntu:~/$ ./15-main.py
[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/base.py</code></li>
</ul>
</div>

<h3 class="panel-title">
17. JSON string to dictionary
</h3>

Update the class <code>Base</code> by adding the static method <code>def from_json_string(json_string):</code> that returns the list of the JSON string representation <code>json_string</code>:</p>

<ul>
<li><code>json_string</code> is a string representing a list of dictionaries</li>
<li>If <code>json_string</code> is <code>None</code> or empty, return an empty list</li>
<li>Otherwise, return the list represented by <code>json_string</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 16-main.py
#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

list_input = [
{'id': 89, 'width': 10, 'height': 4},
{'id': 7, 'width': 1, 'height': 7}
]
json_list_input = Rectangle.to_json_string(list_input)
list_output = Rectangle.from_json_string(json_list_input)
print("[{}] {}".format(type(list_input), list_input))
print("[{}] {}".format(type(json_list_input), json_list_input))
print("[{}] {}".format(type(list_output), list_output))

guillaume@ubuntu:~/$ ./16-main.py
[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
[<class 'str'>] [{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]
[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/base.py</code></li>
</ul>
</div>

<h3 class="panel-title">
18. Dictionary to Instance
</h3>

Update the class <code>Base</code> by adding the class method <code>def create(cls, **dictionary):</code> that returns an instance with all attributes already set:</p>

<ul>
<li><code>**dictionary</code> can be thought of as a double pointer to a dictionary</li>
<li>To use the <code>update</code> method to assign all attributes, you must create a “dummy” instance before:

<ul>
<li>Create a <code>Rectangle</code> or <code>Square</code> instance with “dummy” mandatory attributes (width, height, size, etc.)</li>
<li>Call <code>update</code> instance method to this “dummy” instance to apply your real values</li>
</ul></li>
<li>You must use the method <code>def update(self, *args, **kwargs)</code></li>
<li><code>**dictionary</code> must be used as <code>**kwargs</code> of the method <code>update</code></li>
<li>You are not allowed to use <code>eval</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 17-main.py
#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

r1 = Rectangle(3, 5, 1)
r1_dictionary = r1.to_dictionary()
r2 = Rectangle.create(**r1_dictionary)
print(r1)
print(r2)
print(r1 is r2)
print(r1 == r2)

guillaume@ubuntu:~/$ ./17-main.py
[Rectangle] (1) 1/0 - 3/5
[Rectangle] (1) 1/0 - 3/5
False
False
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/base.py</code></li>
</ul>
</div>

<h3 class="panel-title">
19. File to instances
</h3>

Update the class <code>Base</code> by adding the class method <code>def load_from_file(cls):</code> that returns a list of instances:</p>

<ul>
<li>The filename must be: <code><Class name>.json</code> - example: <code>Rectangle.json</code></li>
<li>If the file doesn’t exist, return an empty list</li>
<li>Otherwise, return a list of instances - the type of these instances depends on <code>cls</code> (current class using this method)</li>
<li>You must use the <code>from_json_string</code> and <code>create</code> methods (implemented previously) </li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 18-main.py
#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]

Rectangle.save_to_file(list_rectangles_input)

list_rectangles_output = Rectangle.load_from_file()

for rect in list_rectangles_input:
print("[{}] {}".format(id(rect), rect))

print("---")

for rect in list_rectangles_output:
print("[{}] {}".format(id(rect), rect))

print("---")
print("---")

s1 = Square(5)
s2 = Square(7, 9, 1)
list_squares_input = [s1, s2]

Square.save_to_file(list_squares_input)

list_squares_output = Square.load_from_file()

for square in list_squares_input:
print("[{}] {}".format(id(square), square))

print("---")

for square in list_squares_output:
print("[{}] {}".format(id(square), square))

guillaume@ubuntu:~/$ ./18-main.py
[139785912033120] [Rectangle] (1) 2/8 - 10/7
[139785912033176] [Rectangle] (2) 0/0 - 2/4
---
[139785911764752] [Rectangle] (1) 2/8 - 10/7
[139785911764808] [Rectangle] (2) 0/0 - 2/4
---
---
[139785912058040] [Square] (5) 0/0 - 5
[139785912061848] [Square] (6) 9/1 - 7
---
[139785911764976] [Square] (5) 0/0 - 5
[139785911765032] [Square] (6) 9/1 - 7
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>python-almost_a_circle</code></li>
<li>File: <code>models/base.py</code></li>
</ul>
</div>

</details>
