import platform
import abc


class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class SendButton(Button): pass


class ExitButton(Button): pass


class AbstractFactory:
    @abc.abstractmethod
    def create_send(self):
        pass


class LinuxOSFactory(AbstractFactory):
    def create_send(self):
        return SendButton(0, 0)

    def create_exit(self):
        return SendButton(100, 100)


class WindowsOSFactory(AbstractFactory):
    def create_send(self):
        return SendButton(0, 100)

    def create_exit(self):
        return SendButton(0, 0)


if platform == "linux":
    factory = LinuxOSFactory()
elif platform == "win32":
    factory = WindowsOSFactory()
else:
    raise NotImplementedError("factory only support linux and win32")

exit_button = factory.create_exit()
