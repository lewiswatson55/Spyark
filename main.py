# Spyark
# Developed by @lewiswatson55
# URL: https://lnwatson.co.uk

import requests
import csv
import cfscrape

def getDataARKK():
    scraper = cfscrape.create_scraper()
    url = 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv'
    cfurl = scraper.get(url).content
    name = url.split('/')[-1]
    with open(name, 'wb') as f:
        f.write(cfurl)

    #pdf = requests.get(url, allow_redirects=True)
    #open('tmp/arkk.csv', 'wb').write(pdf.content)

if __name__ == '__main__':
    getDataARKK()

    with open('./ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
         print(row['date'], row['fund'], row['company'], row['ticker'], row['cusip'], row['shares'], row['market value($)'], row['weight(%)'])

