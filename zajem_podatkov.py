import requests
import re
import os
import csv

#url glavne strani:
dirke_fp_url = 'https://www.motorsportmagazine.com/database/races'
#mapa:
dirke_mapa = 'avto-moto dirke'
#mapa csv-jev:
dirke_mapa_csv = 'avto-moto dirke csvji'
# mapa za prvo stran:
frontpage_filename = "dirke_0.html"
#csv datoteka:
csv_filename = "dirke.csv"


def download_url_to_string(url):
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("failed to connect to url " + url)
        return
    if r.status_code == requests.codes['ok']:
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


def save_page():
    text_fp = download_url_to_string(dirke_fp_url)
    save_string_to_file(text_fp, dirke_mapa, frontpage_filename)
    for stran in range(1, 258):
        url_strani = dirke_fp_url + '?page=' + str(stran)
        text = download_url_to_string(url_strani)
        filename = 'dirke_' + str(stran) + '.html'
        save_string_to_file(text, dirke_mapa, filename)
    return None


##########################################################################


def read_file_to_string(directory, filename):
    ''' Vrne vsebino v nizu'''
    path = os.path.join(directory, filename)
    with open(path, 'r') as file_in:
        return file_in.read()


def page_to_lines(page):
    '''iz strani potegne vrstice (seznam nizov)'''
    rx = re.compile(r'tr class=(.*?)</tr>',
                    re.DOTALL)
    lines = re.findall(rx, page)
    return lines


def race_without_a_winner(sez):
    '''Če dirka nima zmagovalca ji nastavimo, da ni zmagovalca'''
    for i in range(len(sez)):
        if 'database/drivers/' not in sez[i]:
            sez[i] += 'database/drivers/.">Ni zmagovalca</a>'
    return sez


def get_dict_from_line_block(block):
    '''iz vrstice (niza) vrne slovar s podatki'''
    rx = re.compile(r'database/races/(.*?)">(?P<ime>.*?)</a><br>(?P<dirkalisce>.*?)\s*</td>'
                    r'.*?class="(.*?)"(.*?)\s*(?P<drzava>[A-Z]{3})'
                    r'.*?content=".*?">(?P<datum>.{10})<'
                    r'.*?database/championships/.*">(?P<prvenstvo>.*?)</a>'
                    r'.*?database/drivers/.*">(?P<zmagovalec>.*?)</a>',
                    re.DOTALL)
    data = re.search(rx, block)
    line_dict = data.groupdict()
    return line_dict


def lines_from_file(filename, directory):
    '''iz strani potegne podatke in jih zapiše v seznam slovarjev'''
    page = read_file_to_string(filename, directory)
    blocks = race_without_a_winner(page_to_lines(page))
    lines = [get_dict_from_line_block(block) for block in blocks]
    return lines


def lines_page(stran):
    return lines_from_file(dirke_mapa, stran)


#######################################################################


def write_csv(fieldnames, rows, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None


def write_lines_to_csv():
    lines = []
    for stevilka in range (258):
        lines += lines_page('dirke_{}.html'.format(str(stevilka)))
    write_csv(lines[0].keys(), lines, dirke_mapa, csv_filename)


def write_lines_to_csv_ij(i=0, j=258):
    '''Enaka funkcija kot zgoraj, le da lahko naredi tudi manjše csvje, za lepši pregled'''
    lines = []
    for stevilka in range (i, j):
        lines += lines_page('dirke_{}.html'.format(str(stevilka)))
    write_csv(lines[0].keys(), lines, dirke_mapa_csv, 'dirke_{0}-{1}.csv'.format(i, j))