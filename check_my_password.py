# https://haveibeenpwned.com
# has an API
# hash the password and send only the first 5 characters of the hash
# returns all leaked passwords that start with those 5 characters
# then we check that list for our password

import requests

url = 'https://api.pwnedpasswords.com/range/' + 'cbfda'

res = requests.get(url)

print(res)
