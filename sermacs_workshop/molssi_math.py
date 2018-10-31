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

    # check for list
    if not isinstance(num_list,list):
        raise TypeError('Function expects a list but got %s'%type(num_list))
    # check for empty list
    elif len(num_list) < 1:
        raise ZeroDivisionError('List is empty')
    else:
        m = 0.0
        for c, i in enumerate(num_list):
            if not (isinstance(i,float) or isinstance(i,int)):
                raise TypeError('Element %s is a %s but should be a float or int'%(c,type(i)))
            else:
                m += i
        return m/len(num_list)

#       try:
#           return sum(num_list)/len(num_list)
#       except TypeError: #does this trigger only on a TypeError...?
#           raise TypeError('Values should be a float or int')

if __name__ == "__main__":
    # Do something if this file is invoked on its own
#   print(canvas())
    num_list = [1,2,3,4,5]
#   num_list = [1.0,2.0,3.0,4.0,5.0]
#   num_list = [1.0,2,3.0,4.0,5.0]
    num_list = [1.0,'2',3.0,4.0,5.0]
#   num_list = []
    print(mean(num_list))
