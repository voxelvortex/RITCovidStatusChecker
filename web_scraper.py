import requests
from lxml import html
import re
from bs4 import BeautifulSoup as bs


def get_state_xml():
    #depricated get_state that uses xml paths
    url = "https://www.rit.edu/ready/rit-covid-19-alert-levels"
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    span_xpath = '//*[@id="block-rit-bootstrap-subtheme-content"]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/p[1]/span[2]'
    req = requests.get(url, headers)

    tree = html.fromstring(req.content)
    span = tree.xpath(span_xpath)
    return str(span[0].text_content())


def get_state_bsre():
    # new get_state function that uses beautifulsoup and regex
    codes = {
      "11754": "Green (Low Risk with Vigilance)",
      "11773": "Yellow (Low to Moderate Risk)",
      "11776": "Orange (Moderate Risk)",
      "11779": "Red (High Risk)"
    }
    url = "https://www.rit.edu/ready/rit-covid-19-alert-levels"
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    req = requests.get(url, headers)
    soup = bs(req.text, 'html.parser')
    divs = soup.find_all('div', {"class": "single-column-container"})

    for div in divs:
        reg = re.search("<div class=\"single-column-container single-column-container-[0-9]{5} page-row position-relative border-bottom-0 black-jumbo (?!d-none)", str(div))
        if not reg:
            continue

        code = re.search("[0-9]{5}", reg[0])[0]
        return codes[code]


def parse_state(state):
    codes = ['Green', 'Yellow', 'Orange', 'Red']
    for i in range(len(codes)):
        if codes[i] in state:
            return i
    return -1
