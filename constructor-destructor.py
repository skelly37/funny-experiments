import weakref

class Foo:
	refs = []

	def __new__(cls, *args, **kwargs):
		ref = super().__new__(cls)
		Foo.refs.append(ref)

		cls.__init__(ref, *args, **kwargs)
		return weakref.proxy(ref)

	def __init__(self, ID):
		self.id = ID
		print("Destroying itself...", self.id)
		self.kill()

	def say_something(self, num):
		print("I'm alive!", self.id, num)

	def kill(self):
		Foo.refs.remove(self)


foo = Foo("FF")
bar = Foo("BB")
bar.say_something(11)
bar.kill()
foo.say_something(22)


