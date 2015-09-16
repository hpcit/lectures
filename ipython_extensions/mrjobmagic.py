#!/usr/bin/env ipython3
# -*- coding: utf-8 -*-

""" Do the magic with IPython """

import plumbum
from IPython.core.magic import register_cell_magic

JOBFILE = "./automatic_script.py"
CONDA = "$CONDA_ACTIVATE"

class MrJobTemplate(object):
    """ Templating the file to write MrJob data """
    def __init__(self, filename=None):
        super(MrJobTemplate, self).__init__()

        if filename is not None:
            self.filename = filename
        else:
            self.filename = JOBFILE

        self.content = ""
        self.content += self.header()

    def header(self):
        self.head = \
            "#!/usr/bin/env python3\n" + \
            "# -*- coding: utf-8 -*-\n" + \
            "\"\"\" MapReduce easily with Python \"\"\"\n" + \
            "from mrjob.job import MRJob\n" + \
            "from mrjob.step import MRStep\n"
        return self.head

    def get_content(self):
        return self.content

# class job(MRJob):
#     def mapper(self, _, line):
#         pass
#     def reducer(self, key, line):
#         pass
#     def steps(self):
#         return [ \
#             MRStep(mapper=self.mapper, reducer=self.reducer), \
#         ]

# if __name__ == "__main__":
#     job.run()

@register_cell_magic
def mapreduce(line, cell):
    """
    Executes a MrJob run from a class definition
    """
    print("options", line.split())
    print("cell", cell)
    return 2 * 3

    # mrjob = MrJobTemplate()
    # return mrjob.get_content() + cell

def load_ipython_extension(ipython):
    """ This function is called when the extension is loaded """
    ipython.register_magic_function(mapreduce, 'cell')
