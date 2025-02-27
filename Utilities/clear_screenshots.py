import datetime
import os

import Screen


class Clear():
    """ Method save only 5 last screenshots """

    def clear_screenshots(self):
        screen_path = "C:\\Users\\G_GoodLike\\PycharmProjects\\SeleniumLessonFinalProject\\Screen"
        files = os.listdir(screen_path)
        if len(files) > 6:
            files.sort(key=lambda x: os.path.getctime(os.path.join(screen_path, x)))
            while len(files) > 6:
                os.remove(os.path.join(screen_path, files[0]))  # Удаляем самый старый
                files.pop(0)  # Убираем его из списка


    """ Method save only 5 last loggs """

    def clear_loggs(self):
        logs_path = "C:\\Users\\G_GoodLike\\PycharmProjects\\SeleniumLessonFinalProject\\logs"
        files = os.listdir(logs_path)
        if len(files) > 6:
            files.sort(key=lambda x: os.path.getctime(os.path.join(logs_path, x)))
            while len(files) > 6:
                os.remove(os.path.join(logs_path, files[0]))  # Удаляем самый старый
                files.pop(0)  # Убираем его из списка

