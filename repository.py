import ast

from pydantic import ValidationError

from models import ModelEmployee


class EmployeeRepository:
    def __init__(self, data: dict):
        self.data = data

    def get_junior_developer(self) -> dict:
        try:
            data_dict = ModelEmployee.parse_obj(self.data).dict()
            data_dict["salary"]["from"] = data_dict["salary"]["custom_from"]
            del data_dict["salary"]["custom_from"]
            data_dict['coordinates'] = {
                'latitude': data_dict["address"]["lat"],
                'longitude': data_dict["address"]["lng"]
            }
            data_dict["address"] = data_dict["address"]["value"]
            data_dict["salary_range"] = {
                "from": data_dict["salary"]["from"],
                "to": data_dict["salary"]["to"]
            }
            data_dict["salary"] = data_dict["salary"]["to"]
            data_dict["contacts"]["name"] = data_dict["contacts"]["fullName"]
            del data_dict["contacts"]["fullName"]
            data_dict["contacts"]["phone"] = {
                "city": data_dict["contacts"]["phone"][1:4],
                "country": data_dict["contacts"]["phone"][0],
                "number": f'{data_dict["contacts"]["phone"][4:7]}-{data_dict["contacts"]["phone"][7:9]}-{data_dict["contacts"]["phone"][9:11]}',
            }
            data_dict['schedule'] = {'id': data_dict['employment']}
            del data_dict['employment']
            return data_dict
        except ValidationError as e:
            return {"errors": e.errors()}

    @staticmethod
    def from_str(data: str):
        data = data.replace('\"from\"', '"custom_from"')
        data = data.replace('true,', 'True,')
        data = data.replace('false,', 'False,')
        data = ast.literal_eval(data)
        try:
            return EmployeeRepository(data=data)
        except ValidationError as e:
            return {"message": e}
