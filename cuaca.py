import requests


class Cuaca:
    def __init__(self, local_path):
        self.local_path = local_path
        self.provinces = [
            "DKIJakarta",
            "DIYogyakarta",
            "JawaBarat",
            "Bali",
            "KalimantanSelatan",
        ]
        self.prefix_url = "https://ibnux.github.io/BMKG-importer"
        self.wilayah_url = f"{self.prefix_url}/cuaca/wilayah.json"
        self.wilayah_data = []
        self.wilayah_id_map = {}
        self.weather_data = []

    def get_wilayah_data(self) -> dict:
        response = requests.get(self.wilayah_url)
        self.wilayah_data = response.json()
        for wilayah in self.wilayah_data:
            key = (wilayah["propinsi"], wilayah["kota"])
            if key[0] in self.provinces:
                self.wilayah_id_map[key] = wilayah["id"]
        return self.wilayah_id_map

    def get_cuaca_by_id(self, id: int) -> list:
        response = requests.get(f"{self.prefix_url}/cuaca/{id}.json")
        self.weather_data = response.json()
        return self.weather_data
