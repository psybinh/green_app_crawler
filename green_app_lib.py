import itertools
import random
import requests
from headers import HEADERS
from forms import URL
from columns import COLUMNS, HASHING_COLUMNS
from bs4 import BeautifulSoup
import json
from datetime import datetime

ElectricityConsumption = [i for i in range(12, 3366, 50)]

# cần viết lại theo đúng tỷ lệ random
def get_random_form(form_data):
    random_form = {}
    for key in form_data:
        random_form[key] = random.choice(form_data[key])
    # 60% for squared meters per person below 40, 40% for the rest
    if random_form["HouseholdViewModel.HouseholdSize"] == 8:
        random_form["HouseholdViewModel.HousingSize"] = random.randint(35, 300)
    else:
        prob = random.randint(1, 875)
        if prob <= 475:
            random_form["HouseholdViewModel.HousingSize"] = random.randint(35, random_form["HouseholdViewModel.HouseholdSize"] * 40)
        else:
            random_form["HouseholdViewModel.HousingSize"] = random.randint(random_form["HouseholdViewModel.HouseholdSize"] * 40, 300)
    # Electric consumtion
    if random_form["HouseholdViewModel.NotKnownElectricityConsumption"] == True:
        random_form["HouseholdViewModel.UsageLightbulbs"] = random.choice([True, False])
        random_form["HouseholdViewModel.UsageEnergyStar"] = random.choice([True, False])
        random_form["HouseholdViewModel.UsageThermostat"] = random.choice([True, False])
        random_form["HouseholdViewModel.UsageEnergySavingDevices"] = random.choice([True, False])
        random_form["HouseholdViewModel.UsageSolarWaterHeater"] = random.choice([True, False])
    else:
        random_form["HouseholdViewModel.ElectricityConsumption"] = random.choice(ElectricityConsumption)
    # Car
    if random.choice([True, False]):
        random_form["TransportViewModel.CarUsageList[0].SelectedFuelTypeOptionId"] = random.choice([15, 16, 17, 18])
        random_form["TransportViewModel.CarUsageList[0].AnnualMileage"] = random.randint(1, 250) * 200
        random_form["TransportViewModel.CarUsageList[0].AverageConsumption"] = random.randint(1, 11)
    #print(random_form)
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
    except Exception as e:
        print(e)
        total_annual = 0
        country_average = 0
        world_average = 0

    percent_bar = soup.find('div', {'class': 'fp-allocation-container row big-allocation-view'})
    try:
        household = percent_bar.find('div', {'class': 'household'}).find('div', class_='fp-allocation-text').text.strip()[:-1]
    except Exception as e:
        print(e)
        household = 0
    try:
        transport = percent_bar.find('div', {'class': 'transport'}).find('div', class_='fp-allocation-text').text.strip()[:-1]
    except Exception as e:
        print(e)
        transport = 0
    try:
        flights = percent_bar.find('div', {'class': 'flights'}).find('div', class_='fp-allocation-text').text.strip()[:-1]
    except Exception as e:
        print(e)
        flights = 0
    try:
        lifestyle = percent_bar.find('div', {'class': 'lifestyle'}).find('div', class_='fp-allocation-text').text.strip()[:-1]
    except Exception as e:
        print(e)
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
    # hashed_id
    hashing_values = []
    for column in HASHING_COLUMNS:
        if column in json_record:
            hashing_values.append(str(json_record[column]))
        else:
            hashing_values.append('')
    hashing_string = ','.join(hashing_values)
    json_record["hashed_id"] = str(hash(hashing_string))
    # datetime
    json_record["datetime"] = datetime.now()
    # square meter per person 
    json_record["square_meter_per_person"] = json_record['HouseholdViewModel.HousingSize'] / json_record['HouseholdViewModel.HouseholdSize']
    result_array = []
    for column in COLUMNS:
        if column in json_record:
            result_array.append(str(json_record[column]))
        else:
            result_array.append('')
    return ','.join(result_array)

def write_2_file(file, record):
    try:
        file.write(record + '\n')
    except Exception as e:
        print(e)

