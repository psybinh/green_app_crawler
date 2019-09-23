from green_app_lib import get_random_form, get_result, parse_content, to_json_record, write_2_file
from constants import FORM_1, FORM_2, URL
import requests
import time
import platform

FORM = FORM_1
RECORDS_PER_SESSION = 50
SESSIONS = 2

def get_filename():
    node_name = platform.node()
    date_time = time.strftime("%Y-%m-%d-%H-%M")
    filename = node_name + '-datetime-' + date_time + '.csv'
    return filename

if __name__ == '__main__':
    filename = get_filename()
    tic = time.time()
    for i in range(SESSIONS): 
        with open(filename, 'a', encoding='utf-8') as file:
            for i in range(RECORDS_PER_SESSION):
                form = get_random_form(FORM)
                
                try:
                    page = get_result(form)
                except Exception as e:
                    print(e)
                    
                result = None
                if page != None:
                    if page.ok:
                        result = parse_content(page)
                    else:
                        print(page)
                
                if result != None:
                    json_record = to_json_record(form, result)
                    write_2_file(file, json_record)
            file.close()
    toc = time.time()
    print('time: ' + str(toc - tic))
            