import requests # import the http requests library

'''GET'''

URL = "http://maps.googleapis.com/maps/api/geocode/json" # api-endpoint
location = "delhi technological university" # location given here
PARAMS = {'address': location} # defining a params dict for the parameters to be sent to the API

retrieve_data = requests.get(url = URL, params = PARAMS) # sending get request and saving the reponse as response object 
data = retrieve_data.json() # extracting data in json format

# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

# printing the output
print('Latitude:%s\nLongitude:%s\nFormatted Address:%s'
        %(latitude, longitude, formatted_address)) 

'''POST'''

API_ENDPOINT = "http://pastebin.com/api/api_post.php" # defining the api-endpoint
API_KEY = "XXXXXXXXXXXXXXXXX" # API key
source_code = '''

print('Hello World!)
a = 1
b = 2

print(a + b)
'''

#data to be sent to api
data = {'api_dev_key': API_KEY,
        'api-option':'paste',
        'api_paste_code': source_code,
        'api_paste_format':'python'}

# sending post request and saving response as response object
post_data = requests.post(url = API_ENDPOINT, data = data)

#extracting response text
pastebin_url = post_data.text
print("The pastebin URL is:%s"%pastebin_url)

