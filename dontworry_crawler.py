import os
import requests
from bs4 import BeautifulSoup 

url = 'https://toot.mantyke.icu/@dontworry'

templist = []
originlist = []

def search(url):
    global templist
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    _list = [i.string for i in soup.find_all('p')[1:-2]]
    
    for i in _list:
        templist.append(i.replace('。','') + '\n')
    try:
        next_url = soup.find('a', class_='load-more', string='Show older')['href']
        search(next_url)
    except:
        return
    
if __name__ == '__main__':
    if os.path.exists('dontworry.txt'):
        with open('dontworry.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                originlist.append(line)

    search(url)
    out = filter(lambda x: x.startswith('没关系') and len(x) > 4, iter(set(templist + originlist)))

    with open('dontworry.txt', 'w') as f:
        f.writelines(out)
    os.system('cp dontworry.txt dontworry_$(date "+%Y%m%d").txt')