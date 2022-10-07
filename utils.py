from clasess import HH, Superjob, Vacancy
from bs4 import BeautifulSoup


def load_vacancy(data: list):
    with open('vacancy.txt', 'a', encoding='utf-8') as file:
        for dat in data:
            file.write(dat.__repr__() + '\n')


def hh_data() -> list:
    hh = HH()
    vacanc = []
    print('Начинаем сбор информации с HH\n')
    for page in range(10):
        print(f'Парсим страницу {page + 1}')
        result = hh.get_request(page).json()
        res = result['items']
        for i in res:
            name = i['name']
            url = i['alternate_url']
            description = i['snippet']['responsibility']
            source = 'HeadHunter'
            if i["salary"] != None:
                salary = i['salary']
                if i["salary"]["from"] != None:
                    salary = i["salary"]["from"]
                    if i["salary"]["to"] != None:
                        salary = i["salary"]["to"]
            else:
                salary = 'По договорённости'
            vacanc.append(Vacancy(source, name, url, salary, description))
    print('Информация с HH собрана\n')
    return vacanc


HOST = 'https://russia.superjob.ru/'


def sj_data() -> list:
    sj = Superjob()
    vac = []
    vacancy = []
    print('Начинаем сбор информации с Superjob\n')
    for page in range(1, 4):
        print(f'Парсим страницу {page}')
        r = sj.get_request(page)
        response = r.text
        soup = BeautifulSoup(response, 'html.parser')
        items = soup.find_all('div', class_='_2lp1U _2J-3z _3B5DQ')
        for item in items:
            name = item.find('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc').get_text(strip=True)
            url = HOST + item.find('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc').find('a').get('href')
            salary = item.find('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi').get_text().replace('\xa0', ' ')
            description = item.find('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky').get_text(strip=True)
            source = 'Superjob'
            vac.append(Vacancy(source, name, url, salary, description))
        vacancy.extend(vac)
    print('Информация с Superjob собрана\n')
    return vacancy


def combine() -> list:
    combined_list = []
    with open('vacancy.txt', 'r', encoding='utf-8') as file:
        for i in file.readlines():
            combined_list.append(i)
        return combined_list
