from bs4 import BeautifulSoup
import requests


def get_page(url):
    print('requesting webpage...')
    result = requests.get(url, headers={
                          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}, verify=True, timeout=10)

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
    soup = BeautifulSoup(src, 'html.parser')

    # return all of the img tags found by beautifulSoup
    return soup.find_all("img")


def get_product_urls(images, res, url):
    while True:
        for image in images:
            # for each image, verify that it's an image of a product, if it is, append it to our list
            if image['src'].find('productImages') != -1:
                res.append(image['src'])
            # break if we have enough images
            if len(res) == 100:
                return

        # build new url to traverse to next page, get the soup, extract the images
        print("Only collected ", len(res),
              " images, fetching from next page...")
        newUrl = str(url + '?Nao=' + str(len(res)))
        print('new url: ', newUrl)
        images = soupify(newUrl)


def fetch_from_file(filename):
    f = open(filename)
    return (f.readlines())


def get_all_images(urls, result):
    idx = 0
    for url in urls:
        # add a new subarray for each url
        result.append([])
        # get the image tags using beautifulSoup + requests
        images = soupify(url)
        # extract the urls for ONLY product images
        get_product_urls(images, result[idx], url)
        idx += 1
