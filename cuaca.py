import requests

class Cuaca:
    def __init__(self, local_path):
        self.local_path = local_path
        self.provinces = [
            "DKIJakarta",
            "DIYogyakarta",
            "JawaBarat",
            "Bali",
            "KalimantanSelatan"
        ]
        self.wilayah_url = "https://ibnux.github.io/BMKG-importer/cuaca/wilayah.json"
        self.wilayah_data = []
        self.wilayah_id_map = {}
        self.weather_data = []
    
    def get_wilayah_data(self):
        response = requests.get(self.wilayah_url)
        self.wilayah_data = response.json()
        for wilayah in self.wilayah_data:
            key = (wilayah["propinsi"], wilayah["kota"])
            if key[0] in self.provinces:
                self.wilayah_id_map[key] = wilayah["id"]
        return self.wilayah_id_map
