import requests
from settings import DEFAULT_LINK

response = requests.get(DEFAULT_LINK, stream=True)
if response.status_code == 200:
    with open('image.png', 'wb') as f:
        for chunk in response:
            f.write(chunk)
else:
    print(DEFAULT_LINK)
    print(response.status_code)
    print(response.content)
