from bs4 import BeautifulSoup as bs
import requests


url = "https://www.rit.edu/ready/rit-covid-19-alert-levels"
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
req = requests.get(url, headers)
