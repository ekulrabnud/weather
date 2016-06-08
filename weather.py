import time
import requests
import json
import pickle



api_key = "df18e11e78b23f570319abb75cdac946"


# def json_print(f):

# 	def format(json_response):

# 		    if isinstance(json_response,list):
# 		        for i in json_response:
# 		            print json.dumps(i,sort_keys=False,separators=(',',':'))
# 		    elif isinstance(json_response,dict):
# 		        for k,v in json_response.items():
# 		            print k,v

# def json_print(response):

# 	def func_wrapper(city):
# 		json_response = response()
# 		if isinstance(json_response,list):
# 			for i in json_response:
# 				print json.dumps(i,sort_keys=False,separators=(',',':'))
# 		elif isinstance(json_response,dict):
# 			for k,v in json_response.items():
# 				print k,v
		
# 	return func_wrapper

def json_print(json_response):

	if isinstance(json_response,list):
		for i in json_response:
			print json.dumps(i,sort_keys=False,separators=(',',':'))
	elif isinstance(json_response,dict):
		for k,v in json_response.items():
			print k,v



class OpenWeatherAPI():

	
	def __init__(self,api_key,units="imperial",cityid="4904381"):

		self.api_key = api_key
		self.units = units
		self.cityid = cityid

		self.CURRENT_WEATHER = "http://api.openweathermap.org/data/2.5/weather"
		self.FORECAST = "http://api.openweathermap.org/data/2.5/forecast/city"
		
	def requester(self,url):

		params = {}
		params["APPID"] = self.api_key
		params["units"] = self.units
		params['id'] = self.cityid

		response = requests.get(url,params=params)
		return json.loads(response.content)

	def get_current_weather(self):

		url = self.CURRENT_WEATHER
		response = self.requester(url)

	def get_forecast(self):

		url = self.FORECAST
		response = self.requester(url)


		


w = OpenWeatherAPI(api_key)

filename = 'forecast.pkl'
# # file = open(filename, 'wb')

# with open(filename,'wb') as f:

# 	pickle.dump(w.get_forecast("4904381"),f)


forecast = open(filename,'r')

forecast = pickle.load(forecast)

print forecast['list'][0]['dt']

# for k,v in forecast.items():
# 	print k

for i in forecast['list']:
	print i['dt_txt'],i['weather']

json_print(w.get_current_weather())










