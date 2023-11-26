from manim import *
from manim_utils import scatter_matplotlib_to_manim
import matplotlib.pyplot as plt


class ConvertScene(Scene):
    def construct(self):
        fig, ax = plt.subplots()
        ax: plt.Axes  # To get autocomplete
        scatter = ax.scatter([1, 2, 3], [1, 2, 3])
        plt.savefig("scatter.png")
        plt.close(fig)

        img = ImageMobject("scatter.png")
        self.play(FadeIn(img))
        self.wait()

        self.play(img.animate.to_edge(LEFT))
        self.wait()

        manim_scatter, manim_axes = scatter_matplotlib_to_manim(
            scatter, axes=ax)
        VGroup(manim_scatter, manim_axes).scale(0.5).to_edge(RIGHT)
        for dot in manim_scatter:
            dot.scale_to_fit_height(0.16)
        self.play(Write(manim_axes), manim_scatter.create())
        self.wait()
