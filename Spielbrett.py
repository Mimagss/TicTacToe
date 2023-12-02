class Spielbrett:
    def __init__(self):
        self.__feld = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.__anzReihen = 3
        self.__anzSpalten = 3
    
    def setze(self, reihe : int, spalten : int, wert : str):
        self.__feld[reihe*self.__anzReihen + spalten] = wert
    
    def gib(self, reihe : int, spalten : int):
        return self.__feld[reihe*self.__anzReihen + spalten]
    
    def __str__(self):
        return '|'.join(self.__feld[0:3]) + '\n' + '|'.join(self.__feld[3:6]) + '\n' + '|'.join(self.__feld[6:9]) 
        
if __name__ == "__main__":
    brett = Spielbrett()
    brett.setze(1,1,"X")
    brett.setze(2,2,"O")
    print(brett)