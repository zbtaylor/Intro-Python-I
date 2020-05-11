class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f'Name: {self.name} Lat: {self.lat} Lon: {self.lon}'


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f'Name: {self.name} Difficulty: {self.difficulty} Size: {self.size} Lat: {self.lat} Lon: {self.lon}'


waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint.__str__())

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.415561)
print(geocache)
