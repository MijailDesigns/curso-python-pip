import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    # print(r.json())
    # print(type(r.json()))
    categories = r.json()
    print(type(categories))
    for category in categories:
        print(category['name'])

