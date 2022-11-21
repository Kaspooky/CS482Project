import requests

# Script to download all of our image urls


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

    # fetch the data and generate a name
    image_data = requests.get(url).content
    image_name = "image" + str(count)

    # save the image
    with open(image_name, "wb") as handler:
        handler.write(image_data)
    print("complete.")
    count += 1
