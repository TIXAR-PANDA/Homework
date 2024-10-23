# Дополнительное практическое задание по модулю: "Классы и объекты."
# Задание "Свой YouTube"


class User:
    """
    Класс User. Атрибуты: nickname (имя пользователя, строка),
    password (в хэшированном виде, число), age (возраст, число)
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname




class Video:
    """
    Класс Video. Атрибуты: title (заголовок, строка),
    duration (продолжительность, секунды),
    time_now (секунда остановки (изначально 0)),
    adult_mode (ограничение по возрасту, bool(False по умолчанию))
    """
    def __init__(self,  title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        if not bool(self.adult_mode) :
            return f'Видео: "{self.title}"'
        else:
            return f'Видео: "{self.title}",!!! до 18 лет'




class UrTube:
    """
    Класс UrTube. Атрибуты: users (список объектов User),
    videos (список объектов Video),
    current_user (текущий пользователь, User)
    """
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = User
        self.current_user = None



    def log_in(self, nickname,password):
        """
        Метод log_in, который принимает на вход аргументы: nickname, password
        и пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        """
        if nickname in self.users.keys() :
            user = self.users[nickname]
        else:
            print(' Пользователь не найден. Зарегистрируйтесь.')
            return

        if user.password == hash(password):
            self.current_user = user
            print(f' {self.current_user}, добро пожаловать!')
        else:
            print(' Пароль неверный ')



    def register(self, nickname, password, age):
        """
        Метод register, который принимает три аргумента:
        nickname, password, age, и добавляет пользователя в список,
        если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран:
        "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.

        """

        user_n = User(nickname, hash(password), age)

        if nickname not in self.users.keys():
            self.users[nickname] = user_n
            self.current_user = user_n
            print (f'---{nickname} , добро пожаловать!---')
        else:
            print(f'\n--Пользователь {nickname} уже зарегистрирован--')


    def log_out(self):
        """
        Метод log_out для сброса текущего пользователя на None.
        """
        self.current_user = None
        return

    def add_video(self, *video):
        """
        Метод add, который принимает неограниченное кол-во объектов класса Video
        и все добавляет в videos, если с таким же названием видео ещё не существует.
        В противном случае ничего не происходит.
        Если, задан объект другого класса - система сообщает, что это не видио
        :param video:
        :return:
        """
        for movie in video:
            if isinstance(movie, Video):
                if not movie.title in self.videos.keys():
                    self.videos[movie.title] = movie
            else:
                print(f' "{movie}" - это не видео')

        return self.videos

    def watch_video(self, video):
        """
        Метод watch_video, который принимает любую строку и ищет
        похожие названия видео.
        Ведётся отчёт в консоль на какой секунде просмотр.
        В конце текущее время просмотра данного видео сбрасывается.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре.
        """
        print(f'\n_______запускаем просмотр видео______')
        ss = str(video)
        video = self.get_videos(ss)
        n = len(video)
        import time
        if n == 1:
            v = video[0]
            video1 = self.videos[v]
            if self.current_user is None :
                print(f'------Войдите в аккаунт, чтобы смотреть видео-----\n')
                return
            if  self.current_user.age < 18 and  bool(v1.adult_mode) :
                print(f'   вам нет 18 лет\n=====просмотр видео не рекомендуется=====\n')
                return
            else:
                print('_____Смотрим видео  ', end=' ')
                for i in range(0,  video1.duration+1):
                    print(i, end=' ')
                    v1.time_now = video1.time_now + 1
                    time.sleep(1)

                v1.time_now = 0
            print('  Конец видео______')
            return video1.time_now

        if n == 0:
            print ('Выбрать другое видео?-----\n')
            return
        if n > 1:
            print(f'Выбрать видео из списка-----')
            return



    def get_videos(self, search_word):
        """
         Метод get_videos, который принимает поисковое слово (search_word) и
        возвращает список названий всех видео,
        содержащих поисковое слово(не учитывает регистр).
        :param search_word:
        :return:
        """

        result = []
        for keys in self.videos.keys():
            if search_word.lower() in keys.lower():
                result.append(keys)
        if len(result) == 0 :
            print(' Видео не найдено ')
            return result
        else:
            print(f'по запросу  "{search_word}" нашли:\n{result}\n')
            return result

    def watch_video2(self, title):
        """
        Метод watch_video, который принимает название фильма,
        если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится,
        если же находит - ведётся отчёт в консоль на какой секунде просмотр.
        В конце текущее время просмотра данного видео сбрасывается.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре.
        :param title:
        :return:
        """
        import time
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        if title in self.videos.keys():
            video = self.videos[title]
            if video.adult_mode == True and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста, покиньте страницу')
            else:
                print('_____Смотрим видео  ', end=' ')
                for i in range(1,video.duration + 1):
                    time.sleep(1)
                    print(i, end=' ')
                    video.time_now = video.time_now + 1

                video.time_now = 0
                print('Конец видео____')
                return video.time_now
        else:
            print('____видео не найдено____')



ur=UrTube()

v1 = Video('Лучший язык программирования 2024 года', 2, )
v2 = Video('Для чего девушкам парень программист?', 4, adult_mode=True)
ur.watch_video2('Лучший язык программирования 2024 года!')
v3 = 'Лучший язык программирования'
# Добавление видео
ur.add_video(v1, v2, v3)

print(f'Добавление видео')
print (ur.videos)
# Проверка поиска
ur.get_videos('лучший')
ur.get_videos('ПРОГ')
ur.watch_video('ПРОГ')
# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.watch_video('Лучший язык программирования 2024 года')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video2('Для чего девушкам парень программист?')


# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)


# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')