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

I will use the following libraries:
- csv for writing query results in a csv file.
- time for suspending execution between queries
- datetime for transforming the UNIX-type calendar date into a standard one that can be read and interpreted by humans
- PySpark for data set manipulation and processing
- matplotlib for displaying a graph

The query through the API returns only 168 records, and considering that the records are made at one hour, a UNIX time interval of 601200 will result.
For students, data can only be obtained for the last year from the present time, so that - i made successive queries and writes in the CSV file.

The query through the API returns only 168 records, and considering that the records are made at one hour, a UNIX time interval of 601200 will result. For students, data can only be obtained for the last year from the present time, so that - they made successive queries and writes in the CSV file.

![image](https://github.com/TrifanLucian/WeatherAPI/assets/111199896/699f0d27-afae-456c-b2a1-95836a5c51c0)

![image](https://github.com/TrifanLucian/WeatherAPI/assets/111199896/9f6957bc-90d2-4d06-8e64-bcf23c4c06d7)

![image](https://github.com/TrifanLucian/WeatherAPI/assets/111199896/4a36ff21-0864-4bfd-af91-fdb4f2bc0c75)

![image](https://github.com/TrifanLucian/WeatherAPI/assets/111199896/1363224c-e8a7-41a2-8b46-d75cd0070c21)

![image](https://github.com/TrifanLucian/WeatherAPI/assets/111199896/72c663b6-fe1d-4ba1-9d3b-c1e987b95fe3)

![Figure_1](https://github.com/TrifanLucian/WeatherAPI/assets/111199896/6e154165-78e7-441d-93fc-9e43a9270bac)





SparkSession was used for reading data, executing queries and working with the dataframe and dataset.

Later, the csv method from PySpark was used to read the previously created CSV file and create a dataframe.

