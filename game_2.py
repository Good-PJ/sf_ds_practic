import numpy as np
#test new
def random_predic(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
       count += 1
       predict_number = np.random.randint(1, 101) 
       if number == predict_number:
           break
    return(count)

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

if __name__ == "__main__":

    score_game(random_predic)