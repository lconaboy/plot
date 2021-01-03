def get_cols(n, cmap='plasma'):
    """Returns a matplotlib colormap as a set of n colours in an
    array.

    :param n: (int) number of points to sample the colormap at
    :param cmap: (str) name of the colormap to sample

    :returns: sampled colormap

    :rtype: (array)
    """
    import matplotlib
    import numpy as np

    # Colourmap
    cmap = matplotlib.cm.get_cmap(cmap)
    cmap_points = np.linspace(0.0, 1.0, n)
    cols = cmap(cmap_points)

    return cols


def sq_fig():
    """Returns the Figure and Axes object for a square figure

    :returns: the Figure object and Axes object

    :rtype: (Figure, Axes)
    """
    
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    return fig, ax


def colorbar(mappable, loc='right'):
    "Taken from: https://joseph-long.com/writing/colorbars/"
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    import matplotlib.pyplot as plt

    if loc in ['left', 'right']:
        orientation = 'vertical'
    else:
        orientation = 'horizontal'
    
    last_axes = plt.gca()
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(loc, size="5%", pad=0.05)
    cbar = fig.colorbar(mappable, cax=cax, orientation=orientation)
    plt.sca(last_axes)
    
    return cbar
