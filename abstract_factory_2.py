import abc


# start object
class UIObjects:
    def __init__(self, css: str):
        self.__css = css


class Button(UIObjects):
    def on_click(self) -> None:
        pass


class TextBox(UIObjects):
    pass


class Header(UIObjects):
    def on_mouse_hover(self) -> None:
        pass


class DarkButton(Button):
    def on_hover(self):
        print("I'm dark")


class DarkTextBox(TextBox):
    def on_mouse_out(self):
        print('oot')


class DarkHeader(Header):
    pass


class LightButton(Button):
    def on_hover(self):
        print("I'm not dark but light")


class LightTextBox(TextBox):
    def on_mouse_out(self):
        print('bye bye')


class LightHeader(Header):
    pass


# end object

# start factory
class Factory:
    @abc.abstractmethod
    def create_button(self) -> Button:
        pass

    @abc.abstractmethod
    def create_header(self) -> Header:
        pass

    @abc.abstractmethod
    def create_text_box(self) -> TextBox:
        pass


class DarkFactory(Factory):
    def create_button(self) -> Button:
        return DarkButton("dark_css")

    def create_header(self) -> Header:
        return DarkHeader("dark_css")

    def create_text_box(self) -> TextBox:
        return DarkTextBox("dark_css")


class LightFactory(Factory):
    def create_button(self) -> Button:
        return LightButton("dark_css")

    def create_header(self) -> Header:
        return LightHeader("dark_css")

    def create_text_box(self) -> TextBox:
        return LightTextBox("dark_css")


# end factory

LIGHT = False
factory = LightFactory() if LIGHT else DarkFactory()
