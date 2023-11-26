from manim import *
from manim_utils import DataScene, Provider


class MyProvider(Provider):
    data: dict = {}

    def get_data(self, time: int):
        return self.data[time]

    def push_data(self, data, time: int):
        self.data[time] = data


provider = MyProvider()


class InputScene(DataScene):
    provider = provider
    x_value: ValueTracker = ValueTracker(-7)

    def construct(self):
        number_line = NumberLine(
            x_range=[-7, 7, 1], length=config.frame_width - 1).add_numbers()
        dot = Dot(number_line.n2p(self.data))
        self.add(number_line, dot)
        dot.add_updater(lambda d: d.move_to(
            number_line.n2p(self.data)))
        self.play(self.x_value.animate.set_value(7), run_time=5)
        self.wait(frozen_frame=False)

    def push_data(self, time: float):
        self.provider.push_data(self.x_value.get_value(), time)


class OutputScene(DataScene):
    provider = provider

    def construct(self):
        nummber_line = NumberLine(
            x_range=[0, 50, 5], length=config.frame_width - 1).add_numbers()
        dot = Dot()
        self.add(nummber_line, dot)
        dot.add_updater(lambda d: d.move_to(
            nummber_line.n2p(self.data ** 2)))
        self.wait(6, frozen_frame=False)
