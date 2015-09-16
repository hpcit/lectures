# -*- coding: utf-8 -*-

""" Do the magic with IPython """

from IPython.core.magic import register_cell_magic

@register_cell_magic
def mymagic(line, cell):
    print("line", line)
    print("cell", cell)
    return True

@register_cell_magic
def mapreduce(line, cell):
    """
    Executes a MrJob run from a class definition
    """
    print("line", line.split())
    print("cell", cell)
    return True

def load_ipython_extension(ipython):
    """ This function is called when the extension is loaded """

    ipython.register_magic_function(mymagic, 'cell')
    ipython.register_magic_function(mapreduce, 'cell')
