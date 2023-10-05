<h1>Python - Everything is object</h1>
<p>In Python everything is an object, which means every entity has some 
metadata (called attributes) and associated functionality (called methods). 
These attributes and methods are accessed via the dot syntax.</p>
<p>For example, numerical types have a real and imag attribute that returns 
the real and imaginary part of the value, if viewed as a complex number:</p>
<pre><code>
x = 4.5
print(x.real, "+", x.imag, 'i')
</code></pre>
<p>4.5 + 0.0 i</p>
<p>Methods are like attributes, except they are functions that you can call using 
opening and closing parentheses. For example, floating point numbers have a method 
called is_integer that checks whether the value is an integer:</p>
<pre><code>
x = 4.5
x.is_integer()
</code></pre>
<p>False</p>
<h2>Background Context</h2>
<p>Now that we understand that everything is an object and have a little bit of knowledge,
let’s pause and look a little bit closer at how Python works with different types of objects.</p>
</br>
<p>BTW, have you ever modified a variable without knowing it or wanting to? I mean:</p>
<pre><code>
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
</code></pre>
<p>OK. But what about this?</p>
<pre><code>
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
</code></pre>
<p>This project is a little bit different than the usual projects. The first part is only questions 
about Python’s specificity like “What would be the result of…”. You should read all documentation 
first (as usual :)), then take the time to think and brainstorm with your peers about what you think 
and why. Try to do this without coding anything for a few hours.</p>
<p>Trying examples in the Python interpreter will give you most of the answers without having to think 
about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test 
in the interpreter.</p>
<p>All your answers should be only one line in a file. No space before or after the answer.</p>
