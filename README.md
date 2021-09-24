# funny-experiments
It's not about WHY?, it's about WHY NOT! Don't expect any reproducable and useful code


# [Putting destructor into Python's class constructor](https://github.com/skelly37/funny-experiments/blob/main/constructor-destructor.py)
### Idea:
I wanted to create fancy data validation — ifs and exceptions are lame and boring :) 
### Solution:
Just use weak references from built-in `weakref` module! Weakref is able to kill itself, so you can destroy all the references and free up the memory. Very dirty hack, don't use it, kids :)

### Output:
`Destroying itself... FF`

`Destroying itself... BB`

`Traceback (most recent call last):`

`  File "/data/temp/./constructor-destructor.py", line 27, in <module>`

`    bar.say_something(11)`

`ReferenceError: weakly-referenced object no longer exists`


# [Lowkey aliases in Python Shell mode](https://github.com/skelly37/funny-experiments/blob/main/py-shell-aliases.py)
### Idea:
I wanted to quickly clear the screen, to exit Python, to quickly generate random numbers — things one normally does in Python Shell. 
### Solution:
Create some .py file, declare classes that will handle your tasks as the "aliases" and initialize objects with desired name. `self.__repr__()` is the method you summon when you enter the variable name in Python shell. Just make it do what you want to achieve and return it (or empty string to avoid errors). When the file is ready, make alias for python in your shell's config, e.g.:
`"alias python = python -i /home/skelly37/pyshutils.py"` (nushell)

# NOTE
I can't say it's fully my approach. It's just my ideas, my code refactoring, my ability to search, copy and paste AND OBVIOUSLY the community!

# Like the content?
Why don't you make a pull request (or issue) with your idea?
