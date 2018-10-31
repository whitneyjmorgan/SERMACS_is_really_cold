"""
molssi_math.py
Sample repo for MolSSI

Handles the primary functions
"""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


def mean(num_list):
    """
    Computes the mean of a list.
    
    Parameters
    ----------
    num_list: list
        List to calculate mean of

    Returns
    -------
    mean: float
        Mean of list of numbers
    """
    if len(num_list) < 1:
        raise ValueError('List is empty')
#   m = 0.0
#   for i in num_list:
#       m += i
#   return m/len(num_list)
    return sum(num_list)/len(num_list)

if __name__ == "__main__":
    # Do something if this file is invoked on its own
#   print(canvas())
    num_list = [1,2,3,4,5]
    num_list = []
    print(mean(num_list))
