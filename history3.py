import json, requests
import csv
import time
import datetime
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, month, avg
import pandas as pd
import matplotlib.pyplot as plt

APPID = 'bc64a8d5ad742224b1d2bc2e995a9b23'

location = 'Bucharest,RO'

outputFile = open('output4.csv', 'w', newline='')
headers = ['dt','datetime', 'temp', 'feels_like','pressure', 'humidity', 'temp_min', 'temp_max', 'wind_speed', 'wind_deg', 'clouds_all', 'weather_id', 'weather_main', 'weather_description', 'weather_icon']
outputDictWriter = csv.DictWriter(outputFile, headers)
outputDictWriter.writeheader()

# 601200 reprezinta intervalul maxim de timp corelat cu numarul maxim de inregistrari care se pot obtine dintr-o interogare
unix_time_start = 1667277588
unix_time_end = 1667277588+601200

while unix_time_end < 1698727188:
    url = 'https://history.openweathermap.org/data/2.5/history/city?q=%s&type=hour&start=%s&end=%s&appid=%s' % (location, str(unix_time_start), str(unix_time_end), APPID)
    response = requests.get(url)
    response.raise_for_status()
    weatherData = json.loads(response.text)
    w = weatherData['list']
    print(f'se scriu inregistrarile din intervalul de timp intre {datetime.datetime.fromtimestamp(unix_time_start)} si {datetime.datetime.fromtimestamp(unix_time_end)}')
    for data in w:
        outputDictWriter.writerow({'dt': data['dt'],
                               'datetime': datetime.datetime.fromtimestamp(data['dt']),
                               'temp': data['main']['temp']-273.15,
                               'feels_like': data['main']['feels_like']-273.15,
                               'pressure': data['main']['pressure'],
                               'humidity': data['main']['humidity'],
                               'temp_min': data['main']['temp_min']-273.15,
                               'temp_max': data['main']['temp_max']-273.15,
                               'wind_speed': data['wind']['speed'],
                               'wind_deg': data['wind']['deg'],
                               'clouds_all': data['clouds']['all'],
                               'weather_id': data['weather'][0]['id'],
                               'weather_main': data['weather'][0]['main'],
                               'weather_description': data['weather'][0]['description'],
                               'weather_icon': data['weather'][0]['icon']})
    unix_time_start = unix_time_start + 601200 + 1
    unix_time_end = unix_time_end + 601200 + 1
    time.sleep(2)
outputFile.close()

spark=SparkSession.builder.appName("test_pyspark").getOrCreate()
data = spark.read.csv(r'C:\Users\Lucian\PycharmProjects\BDA\output4.csv', header=True, inferSchema=True)
data.show()

# se afiseaza zilele si orele cu temperaturi mai mari de 30 de grade
print('se afiseaza zilele si orele cu temperaturi mai mari de 30 de grade')
selected_data = data.select("datetime", "temp").filter(col("temp") > 30)
selected_data.show()

# se afiseaza temperatura medie pentru toate inregistrarile orare (din ultimul an)
print('se afiseaza temperatura medie pentru toate inregistrarile orare (din ultimul an)')
average_value = data.selectExpr("avg(temp)").collect()[0][0]
print(f"Average temperature - column 'temp': {average_value}")

# se calculeaza media temperaturilor pentru fiecare luna in parte
print('se calculeaza media temperaturilor pentru fiecare luna in parte')
for i in range(12):
    selected_data = data.select("datetime", "temp").filter(month(col("datetime")) == i+1).selectExpr("avg(temp)").collect()[0][0]
    print('temperatura pentru luna a', i+1, ' este ', selected_data)

# se contorizeaza numarul total de zile pentru fiecare stare a vremii din an
print('se contorizeaza numarul total de zile pentru fiecare stare a vremii din an')
selected_data = data.groupby('weather_description').count().show()
print(selected_data)

# se afiseaza un grafic cu distributia temperaturilor in functie de luna
print('se afiseaza un grafic cu distributia temperaturilor in functie de luna')
average_temperatures = data.groupBy(month("datetime").alias("Month")).agg(avg("temp").alias("AverageTemperature"))
collected_data = average_temperatures.collect()
months = [row["Month"] for row in collected_data]
average_temperatures = [row["AverageTemperature"] for row in collected_data]
plt.bar(months, average_temperatures)
plt.xlabel('Luna')
plt.ylabel('Temperatura Medie')
plt.title('Distribuția Temperaturilor pe Lună')
plt.show()

spark.stop()

