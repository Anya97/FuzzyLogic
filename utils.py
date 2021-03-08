from math import sqrt, cos, sin
from pygame.math import Vector2

def get_direction(rads):
    """
    Получает направление в виде кортежа.

    Parameters
    ----------
    rads : float
        Угол направления в радианах.

    Returns
    -------
    tuple
        Возвращает вектор направления.
    """
    return (round(cos(rads)), round(sin(rads)))

def mult_tuple(tup, mul):
    """
    Умножает кортеж на число.

    Parameters
    ----------
    tup : tuple
        Умножаемый кортеж
    mul : float
        Множитель

    Returns
    -------
    tuple
        Произведение в виде кортежа
    """
    return (tup[0] * mul, tup[1] * mul)

def v2_to_tuple(vector):
    """
    Конвертирует pygame.Vector2() в tuple()

    Parameters
    ----------
    vector : Vector2
        Вектор

    Returns
    -------
    tuple
        Кортеж со значениями x и y 
    """    
    return (int(vector.x), int(vector.y))

def isVector2Equals(v1, v2):
    """
    Сравнивает, равны ли два вектора.

    Parameters
    ----------
    v1 : Vector2
    v2 : Vector2

    Returns
    -------
    bool
    """
    return (v1.x == v2.x) and (v1.y == v2.y)

