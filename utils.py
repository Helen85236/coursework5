import requests


def get_employers_data():
     employers_id = [78191, 1122462, 906391, 4934, 1740, 3529, 5060211, 5928535, 1711204, 1776381]
     all_employers = []
     for id in employers_id:
          url = f"https://api.hh.ru/employers/{id}"
          params = {
               'page': 0,
               'per_page': 10
          }
          response = requests.get(url, params=params)
          employers_data = response.json()
          all_employers.append(employers_data)
          employers_data_clean = []

     for i in all_employers:
          name = i['name']
          id = i["id"]
          employers_data_clean.append([id, name])
     return  employers_data_clean



def get_data_vacancies():
     vacancies_url = f"https://api.hh.ru/vacancies"
     params = {
          "employer_id": [78191, 1122462, 906391, 4934, 1740, 3529, 5060211, 5928535, 1711204, 1776381],
          "page": 0,
          "per_page": 100
     }
     response = requests.get(vacancies_url, params=params)
     vacancies_data = response.json()

     vacancies_data_clean = []
     for vacancy in vacancies_data.get('items'):
               name = vacancy['name']
               employer = vacancy['employer']['name']
               if vacancy['salary'] is None:
                   continue
               if vacancy['salary'] == '':
                    continue
               else:
                    salary = vacancy.get('salary').get('from')
               employer_id = vacancy['employer']['id']
               link = vacancy['url']
               vacancies_data_clean.append([name, employer, salary, employer_id, link])

     return vacancies_data_clean
