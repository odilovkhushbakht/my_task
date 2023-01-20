import ast

from repository import EmployeeRepository

data = ''' {
    "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
    "employment": "fullDay",
    "address": {
        "region": "Кировская",
        "city": "Киров",
        "street_type": "",
        "street": "",
        "house_type": "",
        "house": "",
        "value": "г Киров, ул Володарского, д 157",
        "lat": 58.593565,
        "lng": 49.672739
    },
    "name": "Junior Backend-developer",
    "salary": {
        "from": 30000,
        "to": 70000,
        "currency": "RUR",
        "gross": False
    },
    "contacts": {
        "fullName": "Журавлев Илья",
        "phone": "79536762399",
        "email": "ilya.zhuravlev@hrb.software"
    }
}
'''

data_bad = ''' {
    "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
    "employment": "fullDay",
    "address": {
        "region": "Кировская",
        "city": "Киров",
        "street_type": "",
        "street": "",
        "house_type": "",
        "house": "",
        "value": "г Киров, ул Володарского, д 157",
        "lat": 58.593565,
        "lng": 49.672739
    },    
    "salary": {
        "from": 30000,
        "to": 70000,
        "currency": "RUR",
        "gross": False
    },
    "contacts": {
        "fullName": "Журавлев Илья",
        "phone": "79536762399",
        "email": "ilya.zhuravlev@hrb.software"
    }
}
'''

result = '''{
    "address": "г Киров, ул Володарского, д 157",
    "allow_messages": True,
    "billing_type": "packageOrSingle",
    "business_area": 1,
    "contacts": {
        "email": "ilya.zhuravlev@hrb.software",
        "name": "Журавлев Илья",
        "phone": {
            "city": "953",
            "country": "7",
            "number": "676-23-99"
        }
    },
    "coordinates": {
        "latitude": 58.593565,
        "longitude": 49.672739
    },
    "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
    "experience": {
        "id": "noMatter"
    },
    "html_tags": True,
    "image_url": "https://img.hhcdn.ru/employer-logo/3410666.jpeg",
    "name": "Junior Backend-developer",
    "salary": 70000,
    "salary_range": {
        "from": 30000,
        "to": 70000
    },
    "schedule": {
        "id": "fullDay"
    }
}
'''


def test_model_developer_good():
    employee_repository = EmployeeRepository.from_str(data=data)
    employee_info = employee_repository.get_junior_developer()
    _result = ast.literal_eval(str(result))
    assert isinstance(employee_info, dict)
    assert employee_info['address'] == _result['address']
    assert employee_info['allow_messages'] == _result['allow_messages']
    assert employee_info['billing_type'] == _result['billing_type']
    assert employee_info['business_area'] == _result['business_area']
    assert employee_info['description'] == _result['description']
    assert employee_info['html_tags'] == _result['html_tags']
    assert employee_info['image_url'] == _result['image_url']
    assert employee_info['name'] == _result['name']
    assert employee_info['salary'] == _result['salary']
    assert employee_info['contacts']['email'] == _result['contacts']['email']
    assert employee_info['contacts']['name'] == _result['contacts']['name']
    assert employee_info['contacts']['phone']['city'] == _result['contacts']['phone']['city']
    assert employee_info['contacts']['phone']['country'] == _result['contacts']['phone']['country']
    assert employee_info['contacts']['phone']['number'] == _result['contacts']['phone']['number']
    assert employee_info['coordinates']['latitude'] == _result['coordinates']['latitude']
    assert employee_info['coordinates']['longitude'] == _result['coordinates']['longitude']
    assert employee_info['experience']['id'] == _result['experience']['id']
    assert employee_info['salary_range']['to'] == _result['salary_range']['to']
    assert employee_info['salary_range']['from'] == _result['salary_range']['from']
    assert employee_info['schedule']['id'] == _result['schedule']['id']


def test_model_developer_feild_name_error():
    employee_repository = EmployeeRepository.from_str(data=data_bad)
    employee_info = employee_repository.get_junior_developer()
    assert isinstance(employee_info, dict)
    assert employee_info == {'errors': [{'loc': ('name',), 'msg': 'field required', 'type': 'value_error.missing'}]}
