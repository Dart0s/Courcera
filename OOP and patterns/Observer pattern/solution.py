from abc import ABC, abstractmethod


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()  # При инициализации множество подписчиков задается пустым

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)  # Для того чтобы подписать пользователя,
        # он добавляется во множество подписчиков

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)  # Удаление подписчика из списка

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)  # Отправка уведомления всем подписчикам


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self, name='ShortNotificationPrinter'):
        self.__name = name
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message.get("title"))
        print(self.achievements)


class FullNotificationPrinter(AbstractObserver):
    def __init__(self, name='FullNotificationPrinter'):
        self.__name = name
        self.achievements = list()

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)
        print(self.achievements)


if __name__ == '__main__':
    a = ShortNotificationPrinter()
    b = FullNotificationPrinter("b")
    c = ObservableEngine()

    c.subscribe(a)
    c.subscribe(b)

    c.notify({"title": "abc", "text": "Дается при выполнении всех заданий в игре"})