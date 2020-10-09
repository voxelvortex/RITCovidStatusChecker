"""
Author: Michael Scalzetti (github.com/voxelvortex)
web_scraper.py

This file contains helper functions that allow the program
to pull alert information from RIT's website and digest that
information into something we can use easily.
"""
import requests
from lxml import html
import re
from bs4 import BeautifulSoup as bs


def get_state_xml():
    """
    -----DEPRECATED-----
    Gets the current alert level at RIT by webscraping an official
    RIT website using lxml. This approach doesn't work properly and
    will likely be removed in a commit in the near future

    :return: String representing the current alert level at RIT
             obtained by web scraping
    """
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
    """
    Gets the current alert level at RIT by webscraping an official
    RIT website using BeautifulSoup and regex. This approach is
    a bit convoluted and isn't guaranteed to work when the site is
    updated, but I have more confidence in this than in the xml approach

    :return: String representing the current alert level at RIT
             obtained by web scraping
    """
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
    """
    :param state: String representing the current alert level at RIT
             obtained by web scraping using a get_state function
    :return: int ranging from 0 to 3 (inclusive to inclusive)
              which represents the current alert level at RIT
    """
    codes = ['Green', 'Yellow', 'Orange', 'Red']
    for i in range(len(codes)):
        if re.search(codes[i], state):
            return i
    return -1
