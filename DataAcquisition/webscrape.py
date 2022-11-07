import sys
from webscrape_functions import fetch_from_file, get_all_images

result = []

# read urls from input file
urls = fetch_from_file(sys.argv[1])

# fetch 100 images from each url in the list, store in result
get_all_images(urls, result)

# open output file for writing
output_filename = sys.argv[2] if sys.argv[2] else "ouputfile"
f = open(output_filename, "w")

# write each url to the output file
for i in result:
    for j in i:
        f.write((j + "\n"))
    f.write("\n\n")
