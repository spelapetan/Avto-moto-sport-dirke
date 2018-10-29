import requests
import re
import os
import csv

#url glavne strani:
dirke_fp_url = 'https://www.motorsportmagazine.com/database/races'
#mapa:
dirke_mapa = 'avto-moto dirke'
# mapa za prvo stran:
frontpage_filename = 'dirke_fp.html'
#csv datoteka:
csv_filename = 'dirke.csv'


def download_url_to_string(url):
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("failed to connect to url " + url)
        return
    if r.status_code == requests.codes.ok:
        return r.text
    else:
        print("failed to download url " + url)
        return


def save_string_to_file(text, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None


def save_frontpage():
    text = download_url_to_string(dirke_fp_url)
    save_string_to_file(text, dirke_mapa, frontpage_filename)
    return None


def read_file_to_string(directory, filename):
    path = os.path.join(directory, filename)
    with open(path, 'r') as file_in:
        return file_in.read()

