""" A program that stores and updates a counter using a Python pickle file"""
import os.path
import sys
import pickle


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    file_exists = os.path.exists(file_name)
    if reset == True:
        file_exists == False
    if file_exists == False:
        f = open(file_name, 'wb')
        pickle.dump(1, f)
        f.close()
    else:
        f = open(file_name, 'rb+')
        loaded = pickle.load(f)
        f.close
        f = open(file_name, 'wb')
        pickle.dump(loaded+1, f)
        f.close
    f = open(file_name, 'rb+')
    counter = pickle.load(f)
    return counter

update_counter('meh.txt', True)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(str(update_counter('blah.txt')))
