import numpy as np
#Вводим число которое необходимо отгадать программе
number = input('Введите число от 1 до 100: ') 
def find_number(number, int=1) -> int:
    """Угадываем число меньше чем за 20 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
#создаем границы диапазона и рандомим первое число в этих границах
    low = 1  
    high = 101 
    predict_number = np.random.randint(low, high) 
     

    while predict_number != number:
        count += 1
        if predict_number > number:
            high = predict_number # сужаем верхнюю границу диапазона в котором находится угадываемое число
        else:
            low = predict_number + 1  # увеличиваем нижнюю границу диапазонав в котором находится угадываемое число
        predict_number = np.random.randint(low, high)  # выбираем новое рандомное число
    return count
    
def score_game(random_predic) -> int:
    """за какое количество попыток в среднем за 1000 подходов угадывает наша функция

    Args:
        random_predic (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(random_predic(number))
    score = int(np.mean(count_ls))
    print(f'Ваш флгоритм угадывает число в среднем за: {score} попыток')
    return score
score_game(find_number)