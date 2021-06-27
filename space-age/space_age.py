class SpaceAge:
    secsPerYear = {"Earth": 31557600, "Mercury":(31557600*0.2408467), "Venus":(31557600*0.61519726), "Mars":(31557600*1.8808158), "Jupiter":(31557600*11.862615), "Saturn":(31557600*29.447498), "Uranus":(31557600*84.016846), "Neptune":(31557600*164.79132)}
    
    def __init__(self, seconds):
        self.age = seconds
        
    def on_earth(self):
        return round(self.age/SpaceAge.secsPerYear["Earth"],2)

    def on_mercury(self):
        return round(self.age/SpaceAge.secsPerYear["Mercury"],2)
    
    def on_venus(self):
        return round(self.age/SpaceAge.secsPerYear["Venus"],2)

    def on_mars(self):
        return round(self.age/SpaceAge.secsPerYear["Mars"],2)

    def on_jupiter(self):
        return round(self.age/SpaceAge.secsPerYear["Jupiter"],2)

    def on_saturn(self):
        return round(self.age/SpaceAge.secsPerYear["Saturn"],2)

    def on_uranus(self):
        return round(self.age/SpaceAge.secsPerYear["Uranus"],2)

    def on_neptune(self):
        return round(self.age/SpaceAge.secsPerYear["Neptune"],2)
