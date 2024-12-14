#  программа для нахождения самого дешевого товара по запросу в Мвидео. Через requests не стал, потому что все сайты уже защищены от такого вида запросов.
#  Создавал функционал для телеграм-бота для себя
#  Для проверки работоспособности введите условно xiaomi 14

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

query = input('Введите запрос: ')
print()

mvid_query = query.replace(' ', '+')
url = f'https://www.mvideo.ru/product-list-page?q={mvid_query}'
service = webdriver.ChromeService()
driver = webdriver.Chrome(service=service)

driver.get(url)
sleep(5)


soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

data = []


for item in soup.find_all('div', class_='product-card-wrapper'):
    name = item.find('a', class_='product-title__text').text
    price = int(item.find('span', class_='price__main-value').text.replace('\xa0', '').replace('₽', '').replace(' ', ''))

    data.append([name, price])


data.sort(key=lambda x: x[1])

data_fr = {}

data_fr['Name'] = [i[0] for i in data]
data_fr['Price'] = [i[1] for i in data]

df = pd.DataFrame(data=data_fr)

df.sort_values(by='Price', ascending=False)

if len(data) == 0:
    print('По вашему запросу ничего не найдено.')
else:
    res = f'В Мвидео ближайший по запросу {data[0][0]} стоит минимум: {data[0][1]}'
    print(res)
    quest = input('Показать весь список из Мвидео? (Y/N): ')
    print()

    if quest.upper() == 'Y':
        print(df)