"""
Освоить различные методы форматирования строк в Python.
Научиться применять эти методы в контексте описания соревнования.
История: соперничество двух команд - Мастера кода и Волшебники данных.
"""

team1 = '  Мастера кода   '
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return f'Победа команды {team1}!'
    if score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return f'Победа команды {team2}!'
    else:
        return f'Ничья!'

# Использование %
print('В команде -%s- участников: %s !' % (team1,team1_num))
print('В команде -%s- участников: %s !' % (team2,team2_num))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
#  Использование  format():
print('Команда -{}- решила задач: {} !'.format(team1, score_1))
print('Команда -{0}- решила задач: {1} !'.format(team2, score_2))
print('-{1}- решили задачи за {0} с !'.format(round(team1_time,1),team1))
print('-{1}- решили задачи за {0} с !'.format(round(team2_time,1),team2))
#Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задачи.')
print(f'Сегодня было решено {score_1+score_2} задач, '
      f'в среднем по {round( (team1_time + team2_time) / (score_1 + score_2), 1 )} секунды на задачу!')
print(challenge_result())

