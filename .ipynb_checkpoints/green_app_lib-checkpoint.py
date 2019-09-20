import itertools
import random
import requests
from constants import HEADERS, HEADERS1, URL
from bs4 import BeautifulSoup

def get_random_form(form_data):
    random_form = {}
    for key in form_data:
        random_form[key] = random.choice(form_data[key])
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

    total_annual = soup.find('div', {'class': 'col-md-5 fp-total-annual-value'}).span.text
    country_average = soup.find('div', {'class': 'col-md-5 fp-total-average-value'}).span.text
    world_average = soup.find('div', {'class': 'col-md-5 fp-total-average-value'}).span.text

    percent_bar = soup.find('div', {'class': 'fp-allocation-container row big-allocation-view'})
    household = percent_bar.find('div', {'class': 'household'}).find('div', class_='fp-allocation-text').text
    transport = percent_bar.find('div', {'class': 'transport'}).find('div', class_='fp-allocation-text').text
    flights = percent_bar.find('div', {'class': 'flights'}).find('div', class_='fp-allocation-text').text
    lifestyle = percent_bar.find('div', {'class': 'lifestyle'}).find('div', class_='fp-allocation-text').text

    return {'total_annual': total_annual, 
           'country_average': country_average,
           'world_average': world_average,
           'household': household,
           'transport': transport,
           'flights': flights,
           'lifestyle': lifestyle}

def to_json_record(form, result):
    return {**form, **result}

def to_record(json_record):
    values = [val for val in json_record.values()]
    return ','.join(values)

def write_2_file(file, record):
    try:
        file.write(record + '\n')
    except Exception as e:
        print(e)

