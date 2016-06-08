import requests
import json
import pickle
import datetime

api_key = "df18e11e78b23f570319abb75cdac946"
HOME = "4904381"

class API(object):

	def __init__(self,api_key,base_url):

		self.api_key = api_key
		self.base_url = base_url

	def key(self):
		return self.api_key

	def url(self):
		return self.base_url

class APIResponder():

	def get_json(self,response):

		return json.loads(response)


class Address():

	def __init__(self,city,zip,country):

		self.city = city
		self.zip = zip
		self.country = country
		
class OpenWeatherAPI(API):

	def __init__(self,api_key,base_url,address,units="imperial"):
		API.__init__(self,api_key,base_url)

		self.units = units
		self.address = address
		self.forecast = None
		
	def api_get(self,path,**params):

		params = params
		params['APPID'] = self.api_key
		params["units"] = self.units
		url = self.base_url + path

		response = requests.get(url,params=params)
		json_response = json.loads(response.content)

		return json_response

	def get_weather(self):

		query = "%s,%s" % (self.address.zip,self.address.country)
		path = "weather"
		weather = self.api_get(path,q=query)
		
		return weather

	def get_forecast(self):

		query = "%s,%s" % (self.address.city,self.address.country)
		path = "forecast"
		forecast = self.api_get(path,q=query)
		
		return forecast


class Forecaster():

	def __init__(self,forecast):

		self.forecast = forecast
		self.today = datetime.date.today()

		for i in self.forecast['list']:
			i['time'] = datetime.datetime.strptime(i['dt_txt'],"%Y-%m-%d %H:%M:%S")

	def basic(self):
		f = self.forecast

		for k,v in f.items():
			print k


	def get_today(self):

		for i in self.forecast['list']:
			if i['time'].date() == self.today:
				print i['main']

	def get_tomorrow(self):

		print "get_tomorrow"

		for i in self.forecast['list']:
			if i['time'].date() == self.today + datetime.timedelta(days=1):
				print i['main']

	def get_day_after_tomorrow(self):

		print "get_day_after_tomorrow"

		for i in self.forecast['list']:
			if i['time'].date() == self.today + datetime.timedelta(days=2):
				print i['main']

	def get_location(self):

		print self.forecast['city']








address = Address("oak park","60302","us")
weather = OpenWeatherAPI(api_key,"http://api.openweathermap.org/data/2.5/",address)
current_weather = weather.get_weather()
print weather.address.zip

# forecast = ow.get_forecast()s
# filename = 'forecaster.pkl'
# output = open(filename,'rb')
# forecast = pickle.load(output)
# forecaster = Forecaster(forecast)
# # forecaster.basic()
# forecaster.get_today()
# forecaster.get_tomorrow()
# forecaster.get_day_after_tomorrow()
# forecaster.get_location()













# print ow.url()

# print (ow.get("weather",zip="60302,us")).content

# print ow.get_weather(cityid="4934381")

# print type((ow.get("weather",cityid=HOME)).content)

# weather_api = API(api_key,"http://api.openweathermap.org/data/2.5/")

# print weather_api.get("weather",city="60302,us")







