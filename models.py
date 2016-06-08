class Weather():

	def __init__(self,**kwargs):

		self.param_defaults={}


	def __str__(self):
		return self



class Forecast(Weather):

	def __init__(self,**kwargs):
		self.param_defaults = {
		'temp':None,
		'wind':None
		}

		for (param, default) in self.param_defaults.items():
			setattr(self, param, kwargs.get(param, default))



f = Forecast(temp="50",wind="56")

def kwargs(*args):
	return args


print kwargs(1,2)