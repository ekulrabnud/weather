from openweatherapimaster import *

api_key = "df18e11e78b23f570319abb75cdac946"




address = Address("oak park","60302","us")
api  = OpenWeatherAPI(api_key,"http://api.openweathermap.org/data/2.5/",address)
weather = api.get_weather()

filename = 'forecaster.pkl'
output = open(filename,'rb')
forecast = pickle.load(output)

forecaster = Forecaster(forecast=forecast,weather=weather)

forecaster.get_today()
forecaster.current_weather()



# print dir(weather)
# weather.current_weather()