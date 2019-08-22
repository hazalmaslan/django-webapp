import requests
import json
import os
import datetime
import io
import tarfile
key = '897ed6ea07a01b7582491a83d1209e10f2fe9af6ff5a6451881cf58190555837'


def file_scan(file, api_key=key):

    param = {'apikey': api_key}
    files = {'file': (file, open(file,'rb'))}
    response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=param)
    #print(response.json())
    hashes = response.json()["sha256"]
    print(hashes)
    print("\n")
    if not os.path.exists(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes):
        os.mkdir(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes)
    jasonmomoa = str(response.json()).replace(',', ',\n').replace('[', '\n[').replace('\n[]', '[]')
    kratos = open(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3] + '/' + hashes +'/'+ 'SCAN_' + datetime.datetime.now().strftime('%d' + '-' + '%m' + '-' + '%y' + '_' + '%X') + '.json', 'a')
    kratos.write(jasonmomoa)
    return response.json()


def file_report(hashes, api_key=key):#last hash as default

    param = {'apikey': api_key, 'resource': hashes}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=param)
    if not os.path.exists(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes):
        os.mkdir(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes)
    jasonmomoa = str(response.json()).replace(',', ',\n').replace('[', '\n[').replace('\n[]', '[]')
    kratos = open(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3] + '/' + hashes +'/'+ 'REPORT_' + datetime.datetime.now().strftime('%d' + '-' + '%m' + '-' + '%y' + '_' + '%X') + '.json', 'a')
    kratos.write(jasonmomoa)
    return response.json()


def file_rescan(hashes, api_key=key):

    param = {'apikey': api_key, 'resource': hashes}
    response = requests.post('https://www.virustotal.com/vtapi/v2/file/rescan', params=param)
    if not os.path.exists(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes):
        os.mkdir(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes)
    jasonmomoa = str(response.json()).replace(',', ',\n').replace('[', '\n[').replace('\n[]', '[]')
    kratos = open(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3] + '/' + hashes +'/'+ 'RESCAN_' + datetime.datetime.now().strftime('%d' + '-' + '%m' + '-' + '%y' + '_' + '%X') + '.json', 'a')
    kratos.write(jasonmomoa)
    return response.json()


def file_upload_url(file, api_key=key): #4 bigger than 32MB smaller than 200MB file scan

    param = {'apikey': api_key}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/scan/upload_url', params=param)
    upload_url_json = response.json()
    upload_url = upload_url_json['upload_url']
    files = {'file': (file, open(file, 'rb'))}
    response = requests.post(upload_url, files=files)
    print(response.text+"\n")
    return response.json()


def file_download_sample(hashes, api_key=key):

    param = {'apikey': api_key, 'hash': hashes}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/download', params=param)
    downloaded_file = response.content
    if not os.path.exists(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes):
        os.mkdir(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes)
    if not os.path.exists(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes+'/'+hashes):
        print('we require more files')
        file_name = os.path.join(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes, hashes)
        with open(file_name,'wb') as f:
            f.write(downloaded_file)
            f.flush()



def file_behaviour(hashes, api_key=key): #there are no guarantees about a report being generated for a given file in VT dataset.

    param = {'apikey': api_key,'hash': hashes}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/behaviour', params=param)
    if not os.path.exists(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes):
        os.mkdir(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes)
    jasonmomoa = str(response.json()).replace(',', ',\n').replace('[', '\n[').replace('\n[]', '[]')
    kratos = open(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3] + '/' + hashes +'/'+ 'BEHAVIOUR_' + datetime.datetime.now().strftime('%d' + '-' + '%m' + '-' + '%y' + '_' + '%X') + '.json', 'a')
    kratos.write(jasonmomoa)
    return response.json()


def file_network_traffic(hashes, api_key=key):

    param = {'apikey': api_key,'hash': hashes}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/network-traffic', params=param)
    if not os.path.exists(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes):
        os.mkdir(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]+'/'+hashes)
    jasonmomoa = str(response.json()).replace(',', ',\n').replace('[', '\n[').replace('\n[]', '[]')
    kratos = open(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3] + '/' + hashes +'/'+ 'NETWORK_DUMP_REPORT_' + datetime.datetime.now().strftime('%d' + '-' + '%m' + '-' + '%y' + '_' + '%X') + '.json', 'a')
    kratos.write(jasonmomoa)
    return response.json()


def file_cluster(date, api_key=key): #date format YYYY-MM-DD       this clustering works only on PE, PDF, DOC and RTF files

    param = {'apikey': api_key, 'date': date}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/clusters', params=param)
    print(str(response.json()).replace(',', ',\n').replace('[', '\n[').replace('\n[]', '[]'))


def file_search(query, api_key=key):

    params = {'apikey': api_key, 'query': query}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/search', params=params)
    print(response.json())
    with io.BytesIO(response.content) as f:
        with tarfile.open(fileobj=f, mode="r:bz2") as t:
            url_infos = [[json.loads(line) for line in t.extractfile(compressed_file)] for compressed_file in t]
            print(url_infos)





# TODO: makedir -leri mkdir olarak değiştir.




#file_rescan('d0b1965aa0c7f9792ee1922f18b1c4e67a45f014fbd324c18dda0dd280605ec4')
#file_search('imphash:7fa974366048f9c551ef45714595665e')
#file_scan('/Users/fcek/PycharmProjects/deneme/text_try.txt')
#file_report('7c1b6b963982548890c5ba835c133e3d81bb8b63071d8d7935607fb97422ae96')
#file_cluster('2018-07-18')
#file_network_traffic('d0b1965aa0c7f9792ee1922f18b1c4e67a45f014fbd324c18dda0dd280605ec4')

"""
if not os.path.exists(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3]):
    os.makedirs(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3])
jasonmomoa = str(response.json()).replace(',', ',\n').replace('[', '\n[').replace('\n[]', '[]')
kratos = open(hashes[0] + '/' + hashes[1] + '/' + hashes[2] + '/' + hashes[3] + '/' + hashes + '_behaviour_' + datetime.datetime.now().strftime('%d' + '-' + '%m' + '-' + '%y' + '_' + '%X') + '.json', 'a')
kratos.write(jasonmomoa)
"""
#search_options = 'type:peexe size:90kb+ positives:5+ behaviour:"taskkill"'
