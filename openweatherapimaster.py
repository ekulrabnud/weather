import requests
import json
import pickle
import datetime

api_key = "df18e11e78b23f570319abb75cdac946"
base_url = "http://api.openweathermap.org/data/2.5/"
	


HOME = "4904381"

class OpenWeatherException(Exception):

	def __init__(self,response):

		self.http_status = response.http_status
		self.msg = response.content

	def __str__(self):
		return "http_status = %s and message = %s ".format(self.http_status,self.msg)

class Address():

	def __init__(self,city,zip,country):

		self.city = city
		self.zip = zip
		self.country = country

class OpenWeatherAPI():

	def __init__(self,api_key,base_url,address,units="imperial"):
		
		self.api_key = api_key
		self.base_url = base_url
		self.units = units
		self.address = address
	
	def _get(self,path,**params):

		params = params
		params['APPID'] = self.api_key
		params["units"] = self.units
		url = self.base_url + path

		try:
			r = requests.get(url,params=params)
			print "good"
			json_response = json.loads(r.content)
		except:
			print "fail"


		return json_response

	def get_weather(self):

		query = "%s,%s" % (self.address.zip,self.address.country)
		path = "weather"
		weather = self._get(path,q=query)
		
		return weather

	def get_forecast(self):

		query = "%s,%s" % (self.address.city,self.address.country)
		path = "forecast"
		forecast = self._get(path,q=query)
		
		return forecast


class Forecaster():

	def __init__(self,forecast=None,weather=None):

		self.forecast = forecast
		self.weather = weather
		self.today = datetime.date.today()

		for i in self.forecast['list']:
			i['time'] = datetime.datetime.strptime(i['dt_txt'],"%Y-%m-%d %H:%M:%S")

	def current_weather(self):

		if self.weather:
			print self.weather['main']
		else:
			print "no weather"

	def days(self,days):
		days = days - 1
		futuredate = self.today + datetime.timedelta(days=days)

		for i in self.forecast['list']:
			if i['time'].date() <= futuredate:
				print i['time'],i['weather']
		
	def rain(self,days=1):
		if not days:
			if self.weather['weather'][0]['main'] == 'Rain':
				print "Raining"
			return

		days = days - 1
		futuredate = self.today + datetime.timedelta(days=days)
		raincount = 0
		for i in self.forecast['list']:
			if i['time'].date() <= futuredate:
				if i['weather'][0]['main'] == 'Rain':
					raincount += 1
		return raincount

	def get_location(self):

		print self.forecast['city']


def pick(forecast):
	filename = 'forecaster3.pkl'
	with open(filename,'wb') as f:
		pickle.dump(forecast,f)
def unpick():
	filename = 'forecaster3.pkl'
	with open(filename,'r') as f:
		return pickle.load(f)

address1 = Address("Oak Park","60302","us")
ow = OpenWeatherAPI(api_key,base_url,address1)



forecast = unpick()
f = Forecaster(forecast,ow.get_weather())

print f.rain(1),f.rain(5)



















