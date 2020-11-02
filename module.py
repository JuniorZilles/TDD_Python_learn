"""Um exemplo do módulo de python"""

import requests
from typing import List

def total(xs: List[float]) -> float:
    """Retorna a soma de xs"""
    result: float = 0.0
    # For each x float em xs, adiciona ao resultado
    result = sum(xs)
    return result

def join(xs: List[int], delimeter: str) -> str:
    """Retorna uma string com a união da lista de inteiros usando um delimitador"""
    result: str = ""
    result = delimeter.join(str(x) for x in xs)
    return result

def divide(x:int, y:int)->float:
    if y == 0:
        raise ValueError('Divide by zero')
    return x / y

def get(name:str)->str:
    r = requests.get(f'http://www.compania.com/{name}/')
    if r.status_code == 200:
        return r.text
    return 'Bad Request'