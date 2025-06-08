from threading import Event
class Foo:
    def __init__(self):
        self.secondEvent = Event()
        self.thirdEvent = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.secondEvent.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.secondEvent.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.thirdEvent.set()
    def third(self, printThird: 'Callable[[], None]') -> None:
        self.thirdEvent.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
