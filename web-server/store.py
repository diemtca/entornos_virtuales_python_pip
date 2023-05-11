import requests

def get_categories():
    #
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    #Transformar el string a un formato iterable como una lista o un diccionario
    #Convertimos el texto a un formato JSON
    #El formato JSON lo transforma en una lista con diccionarios 
    categories = r.json()
    print(type(categories))
    for category in categories:
        print(category['name'])

