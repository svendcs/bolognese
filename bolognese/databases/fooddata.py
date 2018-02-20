import requests
from lxml import html

from bolognese.core.food import Food

class Fooddata:
    URL = 'http://frida.fooddata.dk/ShowFood.php?foodid={}'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}

    def __get_attr(table, row):
        s = table.xpath('./tr[{}]/td[2]/text()'.format(row+1))[0]
        return float(s.strip().replace(',', '.'))

    def get_food(food_name, food_id):
        r = requests.get(Fooddata.URL.format(food_id), headers = Fooddata.HEADERS)
        page = html.fromstring(r.content)
        table = page.xpath('//table[@class="pure-table"][2]/tbody')[0]

        food = Food(food_name)
        food.nutrients.protein = Fooddata.__get_attr(table, 3)
        food.nutrients.carbs = Fooddata.__get_attr(table, 7)
        food.nutrients.fat = Fooddata.__get_attr(table, 10)
        food.nutrients.alcohol = Fooddata.__get_attr(table, 11)
        return food

