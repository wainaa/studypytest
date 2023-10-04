import yaml


# def load_yaml_data(filepath):
#     with open(filepath,'r',encoding='utf8') as f:
#         data=yaml.safe_load(f)
#         data_v3=[]
#         for index in range(0,len(data)+1):
#             data_v2=(data["userinfo"][index]['username'],data["userinfo"][index]['password'],data["userinfo"][index]['expect'])
#             data_v3.append(tuple(data_v2))
#     return data_v3


def load_yaml_data(key):
    with open('./config/data.yaml', 'r', encoding='utf8') as f:
        data = yaml.safe_load(f)
        return data[key]


def dump_yaml_data(data):
    with open('./config/data.yaml', 'a+', encoding='uft8') as f:
        data = yaml.safe_dump(data=data, stream=f)
