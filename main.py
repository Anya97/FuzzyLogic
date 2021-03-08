from drone_logic import *
from fozzy_control import *

def main():
    fuzzy_init() #инициализирует правила контр-ра
    dr = Game() #инициализирует модель(всё поле)
    dr.run() #запускает

if __name__ == "__main__":
    main()