import numpy as np
#new test


number = np.random.randint6(1, 101)
count = 0
while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 100: '))
    if predict_number > number:
        print('Число  должно быть меньше!')
    elif predict_number < number:
        print('Чтсло должно быть больше!')
    else:
        print(f'Вы угадали число! Это число = {number}, за {count} попыток')
        break