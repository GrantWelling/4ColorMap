#Country class and Map class that stores a countries name, color, and neighbors
class Country:
    def __init__(self, name, neighbors, color = 'white'):
        self.name = name
        self.color = color
        self.neighbors = neighbors

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def getName(self):
        return self.name

    def getNeighbors(self):
        return self.neighbors
    
    def isColored(self):
        return self.color != 'white'
    
    def isSafe(self, color):
        for neighbor in self.neighbors:
            if neighbor.getColor() == color:
                return False
        return True

class Map:
    def __init__(self, countries):
        self.countries = countries
        self.colors = ['red', 'green', 'blue', 'yellow']
        
    def __str__(self):
        return str([str(country) for country in self.countries])
    
    def getCountry(self, name):
        for country in self.countries:
            if country.getName() == name:
                return country
        return None
    
    def colorCountry(self, name, color):
        country = self.getCountry(name)
        if country != None:
            country.setColor(color)
    
    def getCountryColor(self, name):
        country = self.getCountry(name)
        if country != None:
            return country.getColor()
        return None
    
    def getCountryNeighbors(self, name):
        country = self.getCountry(name)
        if country != None:
            return country.getNeighbors()
        return None
    
    def isColored(self):
        for country in self.countries:
            if not country.isColored():
                return False
        return True
    
    def isSafe(self, name, color):
        country = self.getCountry(name)
        if country != None:
            for neighbor in country.getNeighbors():
                if self.getCountryColor(neighbor) == color:
                    return False
        return True
    
    def colorMap(self):
        stack = []

        #Push the first country and color it
        stack.append(self.countries[0])
        stack[-1].setColor(self.colors[0])

        #While the map is not fully colored
        while not self.isColored():

            #Get the current country
            current = stack[-1]

            #Check if the current country has a neighbor that is safe to color, if so color it and push it to the stack
            for neighbor in current.getNeighbors():
                if not self.getCountry(neighbor).isColored():
                    for color in self.colors:
                        if self.isSafe(neighbor, color):
                            self.colorCountry(neighbor, color)
                            stack.append(self.getCountry(neighbor))
                            break

            #If the current country has no safe neighbors, backtrack
            if current == stack[-1]:
                stack.pop()
                print('Backtracked')

        return [country.getName() + " " + country.getColor() for country in self.countries]
    
#Map represented as a list of countries, each country has a name and a list of neighbors (First country is the name, the rest are neighbors)
countries = [
    ['Argentina', 'Brasil', 'Bolivia', 'Chile', 'Paraguay', 'Uruguay'],
    ['Brasil', 'Argentina', 'Bolivia', 'Colombia', 'Guyana', 'Guyane (Fr)', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela'],
    ['Bolivia', 'Argentina', 'Brasil', 'Chile', 'Paraguay', 'Peru'],
    ['Chile', 'Argentina', 'Bolivia', 'Peru'],
    ['Colombia', 'Brasil', 'Ecuador', 'Peru', 'Venezuela'],
    ['Ecuador', 'Colombia', 'Peru'],
    ['Guyana', 'Brasil', 'Suriname', 'Venezuela'],
    ['Guyane (Fr)', 'Brasil', 'Suriname'],
    ['Paraguay', 'Argentina', 'Brasil', 'Bolivia'],
    ['Peru', 'Brasil', 'Bolivia', 'Chile', 'Colombia', 'Ecuador'],
    ['Suriname', 'Brasil', 'Guyana', 'Guyane (Fr)'],
    ['Uruguay', 'Argentina', 'Brasil'],
    ['Venezuela', 'Brasil', 'Colombia', 'Guyana']
]

countryList = []
for country in countries:
    countryList.append(Country(country[0], country[1:]))

map = Map(countryList)

print(map.colorMap())