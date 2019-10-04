from green_app_lib import get_random_form, get_result, parse_content, to_record, write_2_file
from forms import FORM
import requests
import time
import platform
from multiprocessing import Pool, cpu_count
import os
from s3_lib import S3Uploader

RECORDS_PER_SESSION = 100
SESSIONS = 50
NBR_PROCESSOR = cpu_count()

def get_filename():
    node_name = platform.node()
    date_time = time.strftime("%Y-%m-%d-%H-%M")
    filename = date_time + '-datetime-' + node_name + '.csv'
    return filename

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
    multiple = 2
    for i in range(SESSIONS):
        nbr_processor = multiple * NBR_PROCESSOR
        print('run with {} processor(s)'.format(nbr_processor))
        req_per_sess = RECORDS_PER_SESSION
        if multiple == 2:
            req_per_sess = int(RECORDS_PER_SESSION / 5)
        forms = [get_random_form(FORM) for i in range(req_per_sess)]
        tic_sess = time.time()
        with open(filename, 'a', encoding='utf-8') as file:
            with Pool(nbr_processor) as pool:
                records = pool.map(get_record, forms)
                pool.close()
                pool.join()
            for record in records:
                if record != None:
                    write_2_file(file, record)
            file.close()
        toc_sess = time.time()
        time_per_req = (toc_sess - tic_sess) / req_per_sess
        print(time_per_req)
        if time_per_req > 0.5:
            multiple *= int(time_per_req / 0.5)
            if multiple > 6:
                multiple = 6
        if time.time() - tic > 20 * 60:
            print('timeout!')
            break
    s3_uploader.upload(filename, filename)
    toc = time.time()
    print('time: ' + time.strftime("%Y-%m-%d-%H-%M") + ' -- ' + str(toc - tic))
            
