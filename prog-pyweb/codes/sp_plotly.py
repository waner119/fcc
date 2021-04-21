import requests
from bs4 import BeautifulSoup
import re


# get codes as a list
def getCodes(url, start, end):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    for i in range(start, end):
        base = "div.cell:nth-child(" + str(i) + ")"
        selector = base + " > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)"
        codes_raw = soup.select(selector)
        codes_clean = [fence.get_text().strip() for fence in codes_raw]
        all_codes.append(codes_clean)


# save codes to file
def saveCodes(file_path, method):
    pyf = open(file_path, method)
    for codes in all_codes:
        for code_true in codes:
            pyf.write('#%%\n')
            pyf.write(code_true)
            pyf.write('\n\n')
    pyf.close()


if __name__ == "__main__":
    all_codes = []
    url = 'https://plot.ly/python/'
    # parameters to set
    charts = 'heatmaps'
    start, end = 7, 25
    fspace = ''
    # run
    getCodes(url + charts, start, end)
    saveCodes(fspace + 'plotly_' + charts.replace('-', '_') + '.py', "a+")
