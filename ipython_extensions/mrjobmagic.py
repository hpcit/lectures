#!/usr/bin/env ipython3
# -*- coding: utf-8 -*-

""" Do the magic with IPython """

import os
from IPython.core.magic import register_cell_magic

JOBDIR = "jobs"
JOBFILE = "script"

class MrJobTemplate(object):
    """ Templating the file to write MrJob data """

    head = ""
    tail = ""
    content = ""

    def __init__(self, content="", filename=None):
        super(MrJobTemplate, self).__init__()

        if filename is not None:
            self.filename = filename
        else:
            import random
            randnum = random.randint(1, 99999)
            randpad = str(randnum).zfill(9)
            self.filename = os.path.join(JOBDIR, JOBFILE +'_'+ randpad + '.py')
        print("Saving", self.filename)

        # Create the class
        self.add_content(self.header())
        self.add_content(self.wrap_mr(content))
        self.add_content(self.footer())

        # Create the file
        self.write_job()

    def header(self):
        self.head = \
            "#!/usr/bin/env python3\n" + \
            "# -*- coding: utf-8 -*-\n\n" + \
            "\"\"\" MapReduce easily with Python \"\"\"\n" + \
            "from mrjob.job import MRJob\n" + \
            "from mrjob.step import MRStep\n"
        return self.head

    def footer(self):
        self.tail = \
            "\nif __name__ == '__main__':\n" + \
            "\tjob.run()"
        return self.tail

    @staticmethod
    def wrap_mr(content):

## Empty content should be
#     def mapper(self, _, line):
#         pass
#     def reducer(self, key, line):
#         pass

# TO FIX:
# content has to be shifted with one tab per line
        newcontent = ""
        for line in content.split('\n'):
            newcontent += '\t' + line + '\n'

        return \
            "\nclass job(MRJob):\n" + \
            "\n\t'''MrJob library template'''\n" + \
            newcontent + "\n" + \
            "\tdef steps(self):\n" + \
            "\t\treturn [ MRStep(mapper=self.mapper, reducer=self.reducer) ]\n"

    def add_content(self, content):
        self.content += content

    def get_content(self):
        return self.content

    def get_file(self):
        return self.filename

    def write_job(self):
        if not os.path.exists(JOBDIR):
            os.makedirs(JOBDIR)
        with open(self.filename, 'w') as out:
            out.write(self.content + '\n')

@register_cell_magic
def mapreduce(line, cell):
    """
    Executes a MrJob run from a class definition
    """

    destination = 'inline'
    # Split options
    options = line.split()
    #print(options)
    if len(options) < 1:
        raise Exception("Provide at least one line option as Input File")
    finput = options[0]
    print("Input file is %s" % finput)
    if 1 in options:
        destination = options[1]
    # Create file
    template = MrJobTemplate(cell)
    # Command for MapReduce
    args = ['python3', template.get_file(), '-r', destination, finput]
    # Execute the command
    cmd = " ".join(args)
    print("Executing", cmd)

    ###################################
    # The best way to call python inside an ipython extension
    from IPython import get_ipython
    ip = get_ipython()
    # ip.ex('import os')
    # ip.magic('%cd -b relfiles')
    # ip.system('ls -F')
    ###################################

# Note: save to output file
# Note bis: get the output file

    ip.system(cmd)
    return "Done"

def load_ipython_extension(ipython):
    """ This function is called when the extension is loaded """
    ipython.register_magic_function(mapreduce, 'cell')
