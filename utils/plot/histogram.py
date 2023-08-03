from typing import Optional

import matplotlib.pyplot as plt
import numpy as np

from utils.plot.common import PlotNames, prepare_figure


def histogram(x: np.ndarray, bins: int, names: Optional[PlotNames] = None) -> plt.Figure:
    fig, ax = prepare_figure(names=names)
    _ = ax.hist(x=x, bins=bins)

    return fig