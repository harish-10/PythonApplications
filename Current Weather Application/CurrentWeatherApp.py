import requests, json 

# Enter your API key here 
api_key = "cd447735926da3a60029f6772bc80eef"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name = input("Enter city name : ") 

# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"]==200: 
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 

    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"]- 273.15

    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 

    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 

    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 

    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z 
    weather_description = z[0]["description"] 

    # print following values 
    print("Temperature (in degree celsius unit) = {temp:1.2f}\natmospheric pressure (in hPa unit) ={atmp} \nhumidity (in percentage) = {hum}\ndescription ={des} "
          .format(temp=current_temperature,atmp=current_pressure,hum=current_humidiy,des=weather_description))
    
elif x["cod"] == 404: 
    print(" City Not Found ") 

else:
    print("{cod} ERROR : {msg}".format(cod=x["cod"],msg=x["message"]))
    

