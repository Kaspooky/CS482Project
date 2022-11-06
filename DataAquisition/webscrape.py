from bs4 import BeautifulSoup
import requests


headerlist = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}


def get_page(url):
    print('requesting webpage...')
    result = requests.get(url, headers=headerlist, verify=True, timeout=10)

    if(result.status_code == 200):
        print("Request returned status 200")
        return result.content
    else:
        print("Status err: ", result.status_code)


def soupify(url):
    # get the page using the request library
    src = get_page(url)
    print('webpage retrieved.')

    # use beautifulSoup + the lxml html parser to make the data usable
    soup = BeautifulSoup(src, 'lxml')

    # return all of the img tags found by beautifulSoup
    return soup.find_all("img")


def get_product_urls(images, res):
    for image in images:
        # for each image, verify that it's an image of a product, if it is, append it to our list
        if image['src'].find('productImages') != -1:
            res.append(image['src'])


# home depot urls
urls = [
    'https://www.homedepot.com/b/Bath-Toilets-Two-Piece-Toilets/N-5yc1vZcb8n',
    'https://www.homedepot.com/b/Bath-Bathroom-Vanities-Bathroom-Vanity-Tops/N-5yc1vZcfvf',
    'https://www.homedepot.com/b/Bath-Bathroom-Vanities-Bathroom-Vanities-with-Tops/Single-Sink/N-5yc1vZcfw5Z1z1pms9',
    'https://www.homedepot.com/b/Bath-Bathroom-Faucets-Bathroom-Sink-Faucets-Centerset-Bathroom-Faucets/N-5yc1vZbrhk',
    'https://www.homedepot.com/b/Lighting-Wall-Sconces/N-5yc1vZc7pi',
    'https://www.homedepot.com/b/Bath-Bathroom-Storage-Bathroom-Cabinets-Linen-Cabinets/N-5yc1vZcfv2',
    'https://www.homedepot.com/b/Bath-Bathtubs-Freestanding-Tubs/N-5yc1vZbz9d',
    'https://www.homedepot.com/b/Bath-Showers-Shower-Doors-Shower-Enclosures/N-5yc1vZcbn2',
    'https://www.homedepot.com/b/Bath-Bathroom-Faucets-Bathtub-Faucets-Bathtub-Shower-Faucet-Combos/N-5yc1vZcd09',
    'https://www.homedepot.com/b/Bath-Bathroom-Storage/Special-Values/N-5yc1vZcfvmZ7',
]


result = []
idx = 0

# loop through each homedepot url
for url in urls:
    # add a new subarray for each url
    result.append([])

    # get the image tags using beautifulSoup + requests
    images = soupify(url)

    # extract the urls for ONLY products
    get_product_urls(images, result[idx])
    idx += 1

print("RESULTS: ", len(result), result)
