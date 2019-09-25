from green_app_lib import get_random_form, get_result, parse_content, to_record, write_2_file
from constants import FORM
import requests
import time
import platform
from multiprocessing import Pool, cpu_count
import os
from s3_lib import S3Uploader

RECORDS_PER_SESSION = 100
SESSIONS = 1
NBR_CPU = cpu_count()

def get_filename():
    node_name = platform.node()
    date_time = time.strftime("%Y-%m-%d-%H-%M")
    filename = node_name + '-datetime-' + date_time + '.csv'
    return filename

def get_form():
    return get_random_form(FORM)

def get_record(form):
    try:
        page = get_result(form)
    except Exception as e:
        print(e)
        page = None
    result = None
    if page != None:
        if page.ok:
            result = parse_content(page)
        else:
            print(page)
    
    record = None
    if result != None:
        record = to_record(form, result)
    return record
            

if __name__ == '__main__':
    filename = get_filename()
    tic = time.time()
    s3_uploader = S3Uploader()
    for i in range(SESSIONS):
        forms = [get_form() for i in range(RECORDS_PER_SESSION)]
        with open(filename, 'a', encoding='utf-8') as file:
            with Pool(NBR_CPU * 2) as pool:
                records = pool.map(get_record, forms)
            for record in records:
                if record != None:
                    write_2_file(file, record)
            file.close()
    s3_uploader.upload(filename, Key=filename)
    toc = time.time()
    print('time: ' + str(toc - tic))
            
