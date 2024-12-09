import os
from django.db import models
from .models import Pass

class DatabaseManager:
    def __init__(self):
        # Получение параметров подключения из переменных окружения
        self.host = os.environ.get('FSTR_DB_HOST')
        self.port = os.environ.get('FSTR_DB_PORT')
        self.user = os.environ.get('FSTR_DB_LOGIN')
        self.password = os.environ.get('FSTR_DB_PASS')

    def create_pass(self, data):
        # Создание объекта модели Pass с установленным значением status
        pass_data = {**data, 'status': 'new'}
        pass_instance = Pass(**pass_data)
        pass_instance.save()
        return pass_instance