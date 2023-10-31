# WeatherAPI
Using an API for creating a data set and using the Pyspark library for data processing in the context of Big Data

OpenWeatherMap (OWM) is a widely used online weather data provider and API service that offers weather data, forecasts, and current conditions for locations worldwide. It provides a variety of weather-related information, including temperature, humidity, wind speed, precipitation, and more.

For students, the OpenWeatherApi provides current weather and forecasts and historical weather collection for one year back and 50,000 calls/day

![image](https://github.com/TrifanLucian/WeatherAPI/assets/111199896/058464e2-d0db-472b-b090-7838a83f1fe9)

To generate the data set, I use the History API from the openweathermap platform, which provides historical hourly weather data for any location on the globe.
The fields in the API response that are used to create the data set are:
<pre>
'dt'
'main': {'temp',
        'feels_like',
        'pressure',
        'humidity',
        'temp_min',
         'temp_max'}
'wind': {'speed',
        'deg' }
'clouds': {'all'}
'weather': [{'id',
          'main': 'Clear',
          'description',
           'icon'}]
</pre>
