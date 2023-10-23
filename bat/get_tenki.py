#get_tenki.py
import requests

save_file = './天気.txt'
api_url = 'https://api.aoikujira.com/tenki/week.php?fmt=ini&city=319'
tenki = requests.get(api_url).text

with open(save_file, 'wt', encoding='utf-8') as f:
    f.write(tenki)