from manim import *
from manim_utils import Table, ScatterPlot
import pandas as pd


class DataVisualizationScene(Scene):
    def construct(self):
        df = pd.DataFrame(
            {
                "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan"],
                "Age": [20, 25, 30, np.nan, 90, 12, 45, 50, 60],
                "Height": [170, 175, 180, 185, 190, 187, 180, 170, 160],
            }
        )
        table = Table.from_dataframe(df.head(), include_index=True)
        self.play(table.create())
        self.wait()

        self.play(FadeOut(table))
        self.wait()

        scatter_plot = ScatterPlot.from_dataframe(df, "Age", "Height")
        self.play(scatter_plot.create())
        self.wait()
