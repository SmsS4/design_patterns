from typing import List


class Observer:
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """

    def __init__(self, callback):
        self._observer_state = None
        self._callback = callback

    def update(self, new_state):
        self._observer_state = new_state
        self._callback(new_state)


class Subject:
    """
    Know its observers. Any number of Observer objects may observe a
    subject.
    Send a notification to its observers when its state changes.
    """

    def __init__(self):
        self._observers: List[Observer] = []
        self._subject_state: int = 0

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)

    def change_subject_state(self):
        self._subject_state += 1
