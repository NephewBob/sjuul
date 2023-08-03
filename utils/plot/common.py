from typing import Tuple

from dataclasses import dataclass
from typing import Optional

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


@dataclass
class PlotNames:
    x_name: Optional[str] = None
    y_name: Optional[str] = None
    title: Optional[str] = None

    def set_in_axes(self, axes: plt.axes) -> None:
        if self.x_name:
            axes.set_xlabel(self.x_name)
        if self.y_name:
            axes.set_ylabel(self.y_name)
        if self.title:
            axes.set_title(self.title)


def prepare_figure(names: Optional[PlotNames]) -> Tuple[Figure, Axes]:
    figure = plt.figure()
    axes = figure.add_subplot()
    if names:
        names.set_in_axes(axes=axes)

    return figure, axes
