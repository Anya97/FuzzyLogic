from math import pow, exp

# define constants start #

VLN = 180 # Очень большое отрицательное
NL  = 135 # Большое отрицательное
NM  = 90 # Среднее отрицательное
NS  =  45 # Малое отрицательное
Z  = 0 # Нулевое
PS  = 225 # Малое положительное
PM  = 270 # Среднее положительное
PL  = 315 # Большое положительное
VLP = 360 # Очень большое положительное 

# разница позиций по X ("ошибка")
LEFT = 500
LEFT_C = 100
XCENTER = 0 
RIGHT_C = -100
RIGHT = -500

# разница позиций по Y
UP = 500
UP_C = 100
YCENTER = 0
DOWN_C = -100
DOWN = -500

# define constants end #


# operators start #
AND = 0
# operators end #
# base of rules
RULES = []

#A is a rule
def mu(x, A):
    return exp(-(pow(x-A, 2) / (2 * pow(30, 2))))

class Rule():
    fozzy_error = None # ошибка по х
    operator = AND
    fozzy_de = None # разница по y
    output = None # угол, который на выходе

    def __init__(self, fe, op, fde, output):
        """
        Parameters
        ----------
        fe : int
            ошибка по х
        op : int
            Правило два (AND или OR)
        fde : int
            ошибка по y
        output : int
            Результат
        """        
        self.fozzy_error = fe
        self.operator = op
        self.fozzy_de = fde
        self.output = output

        RULES.append(self) 


def processRules(e, de):
    """processRules Запускает обработку значений с помощью правил.
    закидываем ошибку по х и по y
    Parameters
    ----------
    e : float
        Первое значение
    de : float
        Второе значение

    Returns
    -------
    float
        угол направления
    """    
    summ_alpha_c = 0 #будем сюда суммировать все результаты мю функций, которые нам подходят
    summ_alpha = 0 #

    for i in range(len(RULES)): # Перебираем, исходя из справил, подходящие нам правила отдельно для x и y (true or false)
        alpha = 0
        mue = mu(e, RULES[i].fozzy_error) 
        mude = mu(de, RULES[i].fozzy_de)
        if RULES[i].operator == AND:
            alpha = min(mue, mude)
        else:
            alpha = max(mue, mude)

        summ_alpha_c += alpha * RULES[i].output #результаты суммируем(доля от выхода)
        summ_alpha += alpha #суммируем
    
    return summ_alpha_c / summ_alpha
    
    

def fuzzy_init():
    """fuzzy_init Инициализирует правила контроллера
    нечёткой логики.
    """
    Rule(LEFT, AND, UP, NS) # слева и сверху
    Rule(LEFT, AND, UP_C, NS) # слева по центру (чуть выше)
    Rule(LEFT, AND, YCENTER, VLP) # слева по центру по y
    Rule(LEFT, AND, DOWN_C, PL) # снизу около центра 
    Rule(LEFT, AND, DOWN, PL) # слева снизу
    
    Rule(LEFT_C, AND, UP, NS) # слева чуть ближе к центру
    Rule(LEFT_C, AND, UP_C, NS) # 
    Rule(LEFT_C, AND, YCENTER, VLP)
    Rule(LEFT_C, AND, DOWN_C, PL)
    Rule(LEFT_C, AND, DOWN, PL)
    
    Rule(XCENTER, AND, UP, NM) # центр по х и сверху по y
    Rule(XCENTER, AND, UP_C, NM) 
    Rule(XCENTER, AND, DOWN_C, PM)
    Rule(XCENTER, AND, DOWN, PM)

    Rule(RIGHT, AND, UP, NL)
    Rule(RIGHT, AND, UP_C, NL)
    Rule(RIGHT, AND, YCENTER, VLN)
    Rule(RIGHT, AND, DOWN_C, PS)
    Rule(RIGHT, AND, DOWN, PS)
    
    Rule(RIGHT_C, AND, UP, NL)
    Rule(RIGHT_C, AND, UP_C, NL)
    Rule(RIGHT_C, AND, YCENTER, VLN)
    Rule(RIGHT_C, AND, DOWN_C, PS)
    Rule(RIGHT_C, AND, DOWN, PS)

