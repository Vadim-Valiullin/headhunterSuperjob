from utils import *

def main():

    while True:
        user_input = input('Выберите действие:\n1. Сформировать файл с вакансиями с HH и Superjob\n2. Вывести список '
                           'из вакансий c HH\n3. Вывести список вакансии с SJ\n4. Очистить файл\nВвод: ')
        if int(user_input) == 1:
            vacancy_1 = hh_data()
            load_vacancy(vacancy_1)
            vacancy_2 = sj_data()
            load_vacancy(vacancy_2)
            print('Файл загружен!')
        if int(user_input) == 2:
            count = 0
            combined_list = combine()
            for vac in combined_list:
                if 'HeadHunter' in vac and count < 5:
                    print('>' * 50, f'Вакансия # {count + 1}', '<' * 50, '\n')
                    print(vac)
                    count += 1
        if int(user_input) == 3:
            count = 0
            combined_list = combine()
            for vac in combined_list:
                if 'Superjob' in vac and count < 5:
                    print('>' * 50, f'Вакансия # {count+1}', '<' * 50, '\n')
                    print(vac)
                    count += 1
        if int(user_input) == 4:
            f = open('vacancy.txt', 'r+')
            f.truncate(0)
            print('Файл очищен!')


if __name__ == '__main__':
    main()






