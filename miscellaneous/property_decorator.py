"""
	Class without getters and setters
"""
class Celsius:
    def __init__(self, temperature: float = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

def main1():
	human = Celsius()
	human.temperature = 37

	print(human.temperature)
	"""
		Whenever you assign or retrieve any object attribute like `temperature`,
		Python searches it in the object's built-in `__dict__` attribution:
	"""
	print(human.__dict__)
	# `human.temperature` was actually `human.__dict__[temperature]`

	print(human.to_fahrenheit())

"""
	Using setter and getter to set restriction
"""
class Celsius:
	def __init__(self, temperature: float = 0):
		self.set_temperature(temperature)

	def to_fahrenheit(self):
		return (self._temperature * 1.8) + 32

	def get_temperature(self):
		return self._temperature

	def set_temperature(self, temperature: float):
		if temperature < -273.15:
			raise ValueError('Temperature below -273.15 is not possible')
		self._temperature = temperature

def main2():
	human = Celsius(37)

	print(human.get_temperature())
	print(human.to_fahrenheit())

	human.set_temperature(-300)

	print(human.to_fahrenheit())

	"""
		There's no restriction in the use of underscore variable, `self._temperature`.
		It's just an indication that the variable is private
	"""
	human._temperature = -100
	human.get_temperature()

	"""
		You just updated the Celsius class and it will make all the classes using Celsius
		must change expressions such as `human.temperature` and `human.temperature = 10`
		to `human.get_temperature()` and `human.set_temperature(10)`, respectively.
	"""

"""
	The property class
"""
# using property class
class Celsius:
    def __init__(self, temperature: float = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    def set_temperature(self, value: float):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)

def main3():
	human = Celsius(37)
	print(80*'-')
	print(human.temperature)
	print(80*'-')
	print(human.to_fahrenheit())
	print(80*'-')
	print(human.__dict__)
	print(80*'-')
	human.temperature = -300
	print(80*'-')
	"""
		Now, the expressions `human.temperature` and `human.temerature = 10` will
		automatically call the getter and the setter.
	"""

"""
	The @property decorator

	The expression `temperature = property(get_temperature, set_temperature)` can be 
	broken down as:
					# make empty property
					temperature = property()
					# assign fget
					temperature = temperature.getter(get_temperature)
					# assign fset
					temperature = temperature.setter(set_temperature)
"""
class Celsius:
    def __init__(self, temperature: float = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        print("Setting value...")
        if not isinstance(value, float) and not isinstance(value, int):
        	raise ValueError('Temperature must be float or int') 	
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

def main4():
	human = Celsius(37)
	print(80*'-')
	print(human.temperature)
	print(80*'-')
	print(human.to_fahrenheit())
	print(80*'-')
	human.temperature = 10
	print(80*'-')
	coldest_thing = Celsius(-300)

"""
	You can also add restriction to the class setter
"""
class Cake:
	def __init__(self, name: str = None, color: str = None):
		self._name = name
		self._color = color

	@property
	def name(self):
		print('Getting name...')
		return self._name

	@property
	def color(self):
		print('Getting color...')
		return self._color

	@name.setter
	def name(self, value: str):
		print('Setting name...')
		if self._name is None:
			if not isinstance(value, str):
				raise ValueError('Name must be of'
								'type string')
			self._name = value
		else:
			raise AttributeError('You cannot change the name of the cake')

	@color.setter
	def color(self, value: str):
		print('Setting name...')
		if self.color is None:
			if not isinstance(value, str):
				raise ValueError('Color must be of'
								'type string')
			self._color = value
		else:
			raise AttributeError('You cannot change the color of the cake')	