class Social_Network:
    def __init__(self, name: str, surname: str) -> None:
        """
        Инициализация базового класса для функиионала пользователя в социальных сетях.

        :param name (str): Имя пользователя.
        :param surname (str): Фамилия пользователя.
        """
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f"name - {self.name}, surname - {self.surname}"

    def __repr__(self) -> str:
        return f"Social_Network(name={self.name}, surname={surname}"

    def play_music(self, musician: str, name: str) -> None:
        """
        Метод включения музыки.

        :param musician (str): Имя музыканта.
        :param name (str): Название песни.

        :return: Играющая музыка.
        """

    def create_chat(self, user_data: str) -> None:
        """
        Метод создания чата.

        :param user_data (str): Данные о пользователе, с кем необходимо создать чат.

        :return: Созданный чат.
        """

    def load_photo(self, data: bytes) -> bool:
        """
        Метод загрузки фото.

        :param data (bytes): Байты фотографии.

        :return: Загружена ли фотография.
        """
        return true


class VK(Social_Network):
    def __init__(self, name: str, surname: str, mail: str) -> None:
        """
        Метод инициализации социальной сети VK.

        :param name (str): Имя пользователя.
        :param surname (str): Фамилия пользователя.
        :param mail (str): Адрес почты.
        """
        super.__init__(name, surname)
        self.mail = mail

    def __str__(self) -> str:
        return f"{super().__str__()}, mail - {self.mail}"

    def add_description(self) -> str:
        """
        Метод создания описания к фотографии.

        :param desc (str): Описание к фотографии.

        :return: Получившийся текст.
        """
        desc = "New photo"
        return f"Descriptions added - {desc}"

    def load_photo(self, data: bytes) -> str:
        """
        Перегруженный метод для загрузки фотографии.
        """
        add_description()
        return f"Photo with description loaded"

    def create_chat(self, user_data: str) -> str:
        """
        Перегруженный метод создания чата.
        """
        return f"Chat with user {user_data} created"


class Telegram(Social_Network):
    def __init__(self, name: str, surname: str, number: str) -> None:
        """
        Метод инициализации социальной сети Telegram.

        :param name (str): Имя пользователя.
        :param surname (str): Фамилия пользователя.
        :param number (str): Номер телефона.
        """
        super().__init__(name, surname)
        self.number = number

    def __str__(self):
        return f"{super().__str__()}, number - {self.number}"

    def create_chat(self, user_data: str) -> str:
        """
        Перегруженный метод создания чата.
        """
        return f"Chat with number {user_data} created"

    def create_secret_char(self, user_data: str) -> None:
        """
        Метод создания секретного.

        :param user_data (str): с кем необходимо создать чат.

        :return: Созданный секретный чат.
        """

if __name__ == "__main__":
    # Write your solution here
    pass
