from typing import Optional

import matplotlib.pyplot as plt
import numpy as np

from utils.plot.common import PlotNames, prepare_figure


def scatter(x: np.ndarray, y: np.ndarray, names: Optional[PlotNames] = None) -> plt.Figure:
    fig, ax = prepare_figure(names=names)
    _ = ax.scatter(x, y)

    return fig