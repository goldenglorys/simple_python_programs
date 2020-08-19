import random
import urllib.request


def download_web_image(image_url):
    print('=============================================================')
    print('Starting...')
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    print('Downloading...')
    urllib.request.urlretrieve(image_url, full_name)
    print('Done')


download_web_image('https://ad.responservbzh.icu/images/delivery/8733fc28125e9dafafaf.jpg')
