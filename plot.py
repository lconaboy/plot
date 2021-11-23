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


def inset_cb(fig, ax, im, cb_label, scale=False, box=None, cb_color='white', cb_fontsize='small', bar_fontsize='x-small'):
    """
    Example

    fig, ax = plt.subplots(1, 1, figsize=[4, 4])
    im = ax.imshow([[1, 2], [2, 3]], extent=(0., 1., 0., 1.))
    cb_color = 'white'
    cb_fontsize = 'small'
    bar_fontsize = 'x-small'
    cb_label = 'v$_{{\\sf bc}}$ (km s$^{{-1}}$)'
    box=100.

    fig, ax = inset_cb(fig, ax, im, cb_label, scale=True, box=box,
                   cb_color=cb_color, cb_fontsize=cb_fontsize,
                   bar_fontsize=bar_fontsize)

    plt.show()
    """
    
    axins = inset_axes(ax,
                       width="50%",  # width = 50% of parent_bbox width
                       height="5%",  # height : 5%
                       loc='upper center')

    ax.axis('off')
    cb = fig.colorbar(im, cax=axins, orientation="horizontal", ticks=[1, 2, 3])
    axins.xaxis.set_ticks_position("bottom")
    cb.set_label(cb_label, color=cb_color,
                 fontsize=cb_fontsize)
    cb.ax.tick_params(color=cb_color, which='both', labelcolor=cb_color,
                      labelsize=cb_fontsize)
    cb.outline.set_edgecolor(cb_color)
    
    if scale:
        xy_bar = (0.05, 0.05)
        h_bar = 0.001
        w_bar = 0.25
        bar = patches.Rectangle(xy_bar, w_bar, h_bar, facecolor=cb_color,
                                edgecolor=cb_color)

        ax.add_patch(bar)
        ax.text(xy_bar[0], xy_bar[1] + (20 * h_bar),
                f'{w_bar * box:.0f} Mpc h$^{{-1}}$', color=cb_color,
                fontsize=bar_fontsize)

    return fig, ax
