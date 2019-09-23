import itertools
import random
import requests
from constants import HEADERS, URL, COLUMNS
from bs4 import BeautifulSoup
import json
import datetime

def get_random_form(form_data):
    random_form = {}
    for key in form_data:
        random_form[key] = random.choice(form_data[key])
    # 60% for squared meters per person below 40, 40% for the rest
    prob = random.randint(1, 100)
    if prob <= 60:
        random_form["HouseholdViewModel.HousingSize"] = random.randint(25, random_form["HouseholdViewModel.HouseholdSize"] * 40)
    else:
        random_form["HouseholdViewModel.HousingSize"] = random.randint(random_form["HouseholdViewModel.HouseholdSize"] * 40, 1000)
    # Electric consumtion
    if random_form["HouseholdViewModel.NotKnownElectricityConsumption"] == True:
        random_form["HouseholdViewModel.ElectricityConsumption"] = ''
        
        random_form["HouseholdViewModel.UsageLightbulbs"] = random.choice([True, False])
        random_form["HouseholdViewModel.UsageEnergyStar"] = random.choice([True, False])
        random_form["HouseholdViewModel.UsageThermostat"] = random.choice([True, False])
        random_form["HouseholdViewModel.UsageEnergySavingDevices"] = random.choice([True, False])
        random_form["HouseholdViewModel.UsageSolarWaterHeater"] = random.choice([True, False])
    else:
        random_form["HouseholdViewModel.UsageLightbulbs"] = ''
        random_form["HouseholdViewModel.UsageEnergyStar"] = ''
        random_form["HouseholdViewModel.UsageThermostat"] = ''
        random_form["HouseholdViewModel.UsageEnergySavingDevices"] = ''
        random_form["HouseholdViewModel.UsageSolarWaterHeater"] = ''
    # public transport
    intercity_subway_tram = 9
    random_form["TransportViewModel.Intercity"] = random.randint(0, 8)
    subway_tram = 9 - random_form["TransportViewModel.Intercity"]
    random_form["TransportViewModel.Subway"] = random.randint(0, subway_tram)
    bus_citybus = 3
    random_form["TransportViewModel.Bus"] = random.randint(0, bus_citybus)
    citybus = 3 - random_form["TransportViewModel.Bus"]
    random_form["TransportViewModel.CityBus"] = random.randint(0, citybus)
    tram = subway_tram - random_form["TransportViewModel.Subway"]
    random_form["TransportViewModel.Tram"] = random.randint(0, tram)
    random_form["TransportViewModel.BikeWalk"] = random.randint(7, 14)
    # timestamp
    random_form["datetime"] = datetime.datetime.now()
    return random_form

def get_result(form_data):
    headers = random.choice(HEADERS)
    try:
        page = requests.post(URL, data=form_data, headers=headers)
    except Exception as e:
        page = None
        print(e)
    return page

def parse_content(page):
    soup = BeautifulSoup(page.content, "html.parser")
    try:
        total_annual = soup.find('div', {'class': 'col-md-5 fp-total-annual-value'}).span.text.strip()
        country_average = soup.find('div', {'class': 'col-md-5 fp-total-average-value'}).span.text.strip()
        world_average = soup.find('div', {'class': 'col-md-5 fp-total-average-value'}).span.text.strip()
    except:
        total_annual = 0
        country_average = 0
        world_average = 0

    percent_bar = soup.find('div', {'class': 'fp-allocation-container row big-allocation-view'})
    try:
        household = percent_bar.find('div', {'class': 'household'}).find('div', class_='fp-allocation-text').text.strip()
    except:
        household = 0
    try:
        transport = percent_bar.find('div', {'class': 'transport'}).find('div', class_='fp-allocation-text').text.strip()
    except:
        transport = 0
    try:
        flights = percent_bar.find('div', {'class': 'flights'}).find('div', class_='fp-allocation-text').text.strip()
    except:
        flights = 0
    try:
        lifestyle = percent_bar.find('div', {'class': 'lifestyle'}).find('div', class_='fp-allocation-text').text.strip()
    except:
        lifestyle = 0

    return {'total_annual': total_annual, 
           'country_average': country_average,
           'world_average': world_average,
           'household': household,
           'transport': transport,
           'flights': flights,
           'lifestyle': lifestyle}

def to_json_record(form, result):
    return {**form, **result}

def to_record(form, result):
    json_record = to_json_record(form, result)
    result_array = []
    for column in COLUMNS:
        result_array.append(str(json_record[column]))
    return ','.join(result_array)

def write_2_file(file, record):
    try:
        file.write(record + '\n')
    except Exception as e:
        print(e)

