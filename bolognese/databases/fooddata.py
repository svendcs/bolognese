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

        food = Food(food_name)
        food.servings.update(['100g'])

        macro_table = page.xpath('//th[text()="Makronæringstoffer m.m."]/ancestor::table/tbody')[0]
        food.nutrients['protein'] = Fooddata.__get_attr(macro_table, 4)
        food.nutrients['carbs'] = Fooddata.__get_attr(macro_table, 7)
        food.nutrients['sugar'] = Fooddata.__get_attr(macro_table, 8)
        food.nutrients['fat'] = Fooddata.__get_attr(macro_table, 10)
        food.nutrients['alcohol'] = Fooddata.__get_attr(macro_table, 11)
        food.nutrients['fiber'] = Fooddata.__get_attr(macro_table, 9)

        mineral_table = page.xpath('//th[text()="Mineraler og uorganisk"]/ancestor::table/tbody')[0]
        food.nutrients['sodium'] = Fooddata.__get_attr(mineral_table, 1)

        fat_table = page.xpath('//th[text()="Fedtsyrer, summer"]/ancestor::table/tbody')
        food.nutrients['saturated_fat'] = Fooddata.__get_attr(fat_table[0], 0) if fat_table else 0
        
        return food

