import random
import urllib.request
from bs4 import BeautifulSoup, GuessedAtParserWarning
import requests
import warnings
warnings.filterwarnings('ignore', category=GuessedAtParserWarning)


def download_web_image(image_url):
    print('=============================================================')
    print('Starting...')
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    print('Downloading...')
    urllib.request.urlretrieve(image_url, full_name)
    print('Done')


# download_web_image('https://ad.responservbzh.icu/images/delivery/8733fc28125e9dafafaf.jpg')


def download_stock_data(file_url):
    """
        This helps download any stock data in form of csv and reconstruct it into a pretty format of same csv file
    :param file_url:
    :return:
    """
    print('=============================================================')
    print('Starting...')
    response = urllib.request.urlopen(file_url)
    file = response.read()
    file_str = str(file)
    lines = file_str.split('\\n')
    dest_url = r'data.csv' # r here means raw and can accept any sort of destination path ie. C://owner/Documents/csv/
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()


# download_stock_data('https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1566225788&period2=1597848188&interval=1d&events=history')


def web_crawler_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.goodreads.com/author/list/25150.Gregg_Braden?page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soupify_text = BeautifulSoup(plain_text)
        print('===================================================================================')
        for link in soupify_text.find_all('a', {'class': 'bookTitle'}):
            href = 'https://www.goodreads.com' + link.get('href')
            title = link.text
            # print(href)
            get_single_item_data(href)
        page += 1
    print('===================================================================================')


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.find_all('h1', {'id': 'bookTitle'}):
        print(item_name.string)
    for link in soup.find_all('a'):
        href = 'https://www.goodreads.com' + str(link.get('href'))
        print(href)


web_crawler_spider(1)

