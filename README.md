# RIT Covid Status Checker
Uses the codes provided by RIT to determine and display how safe it is to circulate on campus. This project uses serial as an output so that the information can be displayed by an Arduino (although I've tried to make the code easy to adapt to other uses).

The current implementation of this uses requests, re, and BeautifulSoup4 to webscrape [this page](https://www.rit.edu/ready/rit-covid-19-alert-levels)