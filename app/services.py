#additional classes and functions put my function definition in here.
# We don't need the function call here.

#we must install the requests package in our venv to use it
from re import X
from unicodedata import name
import requests as r

def getDrinkRecs():
    response = r.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail')
    if response.status_code == 200:
        data = response.json()
    else: 
        return response.status_code 
    drinkrecs = []
    for data in data['drinks']:
        if data['strDrinkThumb']:
            drinkrecs.append((data['strDrink'], data['strDrinkThumb']))
            # print(data['strDrink'], data['strDrinkThumb'])
            # print(drinkrecs)
    
    return drinkrecs