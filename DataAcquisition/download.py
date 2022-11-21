import requests
import random
import shutil

# Script to download all of our image urls

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]


# Each index of the arr represents a url within the file
image_file = open("DataAcquisition/home-depot-output", "r")
lines = image_file.readlines()

# for each line, open the image by the url and download it
count = 1
for url in lines:
    # skip if we don't have a url
    if not url or 'https' not in url:
        print('Skipping this line')
        continue

    print("Downloading image # ", count, "...")
    url = url.replace("\n", "")  # strip newline from end of str
    print(url)
    # fetch the data and generate a name

    headers = {"User-Agent": random.choice(user_agent_list),
               "Upgrade-Insecure-Requests": "1",
               "DNT": "1",
               "Accept": "*/*",
               "Accept-Language": "Accept-Language: *",
               "Accept-Encoding": "gzip, deflate",
               "Content-Type": "text/html; img/png"
               }

    image_data = requests.get(
        url, stream=True, headers=headers, verify=True, )
    image_name = "image" + str(count) + ".jpg"

    # if successful
    if image_data.status_code == 200:

        # save the image
        with open(image_name, "wb") as handler:
            shutil.copyfileobj(image_data.raw, handler)

        print("Image download complete.\n")
        count += 1

    else:
        print('Error Fetching Image. STATUS CODE: ', image_data.status_code)
