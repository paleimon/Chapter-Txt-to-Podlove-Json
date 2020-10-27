# Python skript to convert Reaper (Ultraschall) Podcast Chapter Outputs into JSON Format for Podlove Webplayer
# txt File to json
# by Simon Gruner

import json


# the file to be converted
filename = "raw.txt"

# resultant array
chapters = []

# fields in the sample file
fields = ['start', 'title']

with open(filename) as txt:

    for line in txt:

        # reading line by line from the text file
        # split String after first white space (seperates time data from chapter title)
        # e.g. 00:00:00.000 Intro und Einfuehrung ->     {"start": "00:00:00.000", "title": "Intro", "href": "", "image": ""}
        description = list(line.strip().split(" ", 1))

        # loop variable
        i = 0

        data = {}
        while i < len(fields):

            # creating dictionary for each chapter
            data[fields[i]] = description[i]
            i = i + 1

        # Appending missing href and image field
        data['href'] = ''
        data['image'] = ''

        print(data)

        # appending the data of each chapter to the main array
        chapters.append(data)

# creating json file
with open('output.json', 'w') as outfile:
    json.dump(chapters, outfile, indent=4, ensure_ascii=False)
