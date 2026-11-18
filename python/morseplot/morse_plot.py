"""
Adds support for plotting in Morse with Matplotlib

Upon loading, this module will patch Matplotlib's `Axes` class and `pyplot` 
API with a new `morse_plot()` method/function.
"""


# Matplotlit modules that will be expanded
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


# Morseplot code
from morseplot.text_to_dashes import text_to_dashes
from morseplot.durations import durations_default, durations_shortened, parse_durations_multi_type




"""
New function to add to the Axes class
"""

# The self argument will come from the Axes class, after we add this function
# as a method to Axes
def morse_plot_axes(self, *args, morse_text, morse_durations='default', **kwargs):
    """
    Plot with Morse code.
    
    This function is a wrapper around Matplotlib's `plot()` function. This
    means that all of the arguments from `plot()` are supported. See `plot`'s
    documentation for more details.
    
    Other than that, there are two new arguments `morse_text` for the text to 
    encode and `morse_durations`, which is optional, and can be used to adjust
    the lengths of the dots, dashes and pauses.
    

    Parameters
    ----------
    *args :
        The usual plot arguments (x,y, ...).
    morse_text : str
        Text to encode in Morse in the plot
    morse_durations : None, string, dict or list[float|int], optional. 
        Default value is 'default'.
        Durations for the different Morse symbols and pauses.
        Can either be :
            - None for the default durations
            - 'default' or 'shortened'
            - A dict that respects the spec (see `durations_default` from 
             `morseplot.durations`)
            - A list of ints/float, corresponding to the durations of (in the 
            following order): dot, dash, intersymbol pause, interletter pause
            and interword pause.
            
    **kwargs :
        The usual plot arguments

    Returns
    -------
    line : list[Line2D]
        A list of lines. See the docs from `plot()` for more details.

    """
    
    # Parse the durations
    morse_durations = parse_durations_multi_type(morse_durations)
    
    # Get the durations coresponding to the text in Morse
    dashes = text_to_dashes(text=morse_text, durations=morse_durations)
    
    # Plot on the axis
    return(self.plot(*args, dashes=dashes, **kwargs))


# Add this function as a method to the Axes class
Axes.morse_plot = morse_plot_axes
    




"""
Function for the pyplot API
(Needed, because this API is slightly different from the one using Axes)
"""




def morse_plot_pyplot(*args, morse_text='', morse_durations='default', **kwargs):
    
    # For the docs, we will copy the one from `Axes.morse_plot()` afterwards.
    # But just in case, we add some placeholder
    """See `Axes.morse_plot()` for the documentation"""
    
    # In pyplot we don't know the axes, so we have to retrieve them
    ax = plt.gca()
    
    # Once we got the axes, we can just use the `morse_plot()` method we added to the Axes
    return(ax.morse_plot(*args, morse_text=morse_text, morse_durations=morse_durations, **kwargs))


# Add docs
# Might only appear after running the code once and not from a static "analyzer"
morse_plot_pyplot.__doc__ = Axes.morse_plot.__doc__


# Add this function to the pyplot API
plt.morse_plot = morse_plot_pyplot