class Auto:
    """
    Базовый класс для машин.
    """
    def __init__(self, name: str, description: str):
        """
        Конструктор базового класса.

        :param name: Название машины.
        :param description: Описание машины.
        """
        self._name = name
        self.description = description

    def __str__(self) -> str:
        """
        Магический метод для строкового представления объекта.

        :return: Строковое представление объекта.
        """
        return f"{self.__class__.__name__}('{self._name}')"

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта.

        :return: Представление объекта.
        """
        return f"{self.__class__.__name__}('{self._name}', '{self.description}')"


class Car(Auto):
    """
    Дочерний класс для автомобилей.
    """
    def __init__(self, name: str, description: str, model: str):
        """
        Конструктор дочернего класса.

        :param name: Название автомобиля.
        :param description: Описание автомобиля.
        :param model: Модель автомобиля.
        """
        super().__init__(name, description)
        self._model = model

    def start_engine(self, ignition_key: bool) -> str:
        """
        Метод для запуска двигателя.

        :param ignition_key: Состояние ключа зажигания.
        :return: Результат запуска двигателя.
        """
        if ignition_key:
            return f"{self._name}'s engine started."
        else:
            return f"Insert the ignition key for {self._name}."

    def __str__(self) -> str:
        """
        Перегрузка метода __str__.

        :return: Строковое представление объекта.
        """
        return f"{super().__str__()}, Model: {self._model}"
