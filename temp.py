import json

# Path to the JSON file
filename = 'api/questions.json'

# Open the file and load the data
with open(filename, 'r') as file:
    data = json.load(file)

# Now 'data' is a Python dictionary containing the data from the JSON file
print(data)


print(["""Regarding the physical characteristics of India, please examine the following statements:
1.The geological structure of the Himalayas is characterized by its youth, weakness, and flexibility, in contrast to the stiff and solid Peninsular Block.
2. Bhabar is a limited region characterized by the emergence of streams and rivers without a well-defined channel, resulting in the formation of marshy and swampy areas.
3. The Brahmaputra lowlands are renowned for its fluvial islands and sandbars.
How many of the above statements are correct?"""])