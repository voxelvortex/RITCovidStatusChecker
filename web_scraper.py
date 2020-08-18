import requests
from lxml import html


def get_state():
    url = "https://www.rit.edu/ready/rit-covid-19-alert-levels"
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    span_xpath = '//*[@id="block-rit-bootstrap-subtheme-content"]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/p[1]/span[2]'
    req = requests.get(url, headers)

    tree = html.fromstring(req.content)
    span = tree.xpath(span_xpath)
    return str(span[0].text_content())


def parse_state(state):
    codes = ['Green', 'Yellow', 'Orange', 'Red']
    for i in range(len(codes)):
        if codes[i] in state:
            return i
    return -1
