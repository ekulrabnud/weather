def p_decorate(func):
	
	def func_wrapper():
		name = "ted"
		print name
	return func_wrapper


def get_text():
   return "luke"

print get_text()