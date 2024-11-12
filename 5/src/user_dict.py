from collections import UserDict

class NutritionalInformation(UserDict):
    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            pass
        for alias in self.get_aliases(key):
            try:
                return self.data[alias]
            except KeyError:
                pass
        raise KeyError(f"{key}もその別名も存在しません")
    
inf = NutritionalInformation()
inf["name"] = "arugula"
inf["calories_per_serving"] = 5

print(f"inf = {inf}")