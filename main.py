import json
import requests
from os import path, makedirs
from cuaca import Cuaca

weather = Cuaca(local_path="./sources/")

try:
    administration = weather.get_wilayah_data()
    for keys, id in administration.items():
        p, c = keys
        target_path = f"./sources/{p}/{c}/"
        # create administration directory
        if not path.exists(target_path):
            makedirs(target_path)
            print(f"{target_path} is created!\n")

        if path.exists(target_path):
            res = weather.get_cuaca_by_id(id=id)
            data = json.dumps(res, indent=4)
            with open(f"{target_path}/{id}.json", "w") as f:
                f.write(data)
except requests.exceptions.HTTPError as e:
    print (e.response.text)
