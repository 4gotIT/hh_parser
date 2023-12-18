class ParsingError(Exception):
    def __str__(self):
        return "Ошибка подключения по API"