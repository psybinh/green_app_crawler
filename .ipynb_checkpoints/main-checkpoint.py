from green_app_lib import get_random_form, get_result, parse_content
from constants import FORM_1, FORM_2, URL
import requests
import time

if __name__ == '__main__':
    for i in range(10000):
        tic = time.time()
        form = get_random_form(FORM_1)
        page = get_result(form)
        if page != None:
            if page.ok:
                result = parse_content(page)
        if i % 50 == 0:
            print(i)
            print('time for a data point: {}'.format(time.time() - tic))