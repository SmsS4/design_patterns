from typing import List


class Broker:
    def __init__(self):
        self._history: List[int] = []
        self._subscribers: List[Subscriber] = []

    def update(self, event) -> None:
        self._history.append(event)
        for sub in self._subscribers:
            sub.update(event)

    def attach(self, observer) -> None:
        self._subscribers.append(observer)


class Publisher:
    def __init__(self, broker: Broker):
        self._subject_state = 0
        self._broker = broker

    def publish(self) -> None:
        self._broker.update(self._subject_state)

    def change_subject_state(self) -> None:
        self._subject_state += 1


class Subscriber:
    def __init__(self, callback):
        self._callback = callback

    def update(self, new_value) -> None:
        self._callback(new_value)
