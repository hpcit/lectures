#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
RAW added from my other project with:
svn export https://github.com/pdonorio/irods2graph/trunk/irodsgraph/libs/bash.py
"""

"""
Centralized use of plumbum package:
http://plumbum.readthedocs.org/en/latest/index.html#
- use shell commands in a more pythonic way -
"""

from libs import get_logger
logger = get_logger(__name__)

class BashCommands(object):
    """ Wrapper for execution of commands in a bash shell """

    _shell = None

    def __init__(self):
        # Load my personal list of commands based on my bash environment
        from plumbum import local as myshell
        self._shell = myshell

        super(BashCommands, self).__init__()
        logger.debug("Internal shell initialized")

    def execute_command(self, command, parameters=[]):
        """ Pattern in plumbum library for executing a shell command """
        return self._shell[command](parameters)

    def execute_command_advanced(self, command, parameters=[], retcodes=()):
        """ Pattern in plumbum library for executing a shell command """
        # e.g. ICOM["list"][irods_dir].run(retcode = (0,4))
# TO FIX: does not work if parameters is bigger than one element
        comout = \
            self._shell[command][parameters].run(retcode=retcodes)
        ## comout is equal to (status, stdin, stdout)
        return comout

    ###################
    # BASE COMMANDS
    def create_empty(self, path, directory=False, ignore_existing=False):

        args = [path]
        if not directory:
            com = "touch"
        else:
            com = "mkdir"
            if ignore_existing:
                args.append("-p")
        # Debug
        self.execute_command(com, args)
        logger.debug("Created %s" % path)

    def remove(self, path, recursive=False, force=False):

        # Build parameters and arguments for this command
        com = "rm"
        args = []
        if force:
            args.append('-f')
        if recursive:
            args.append('-r')
        args.append(path)
        # Execute
        self.execute_command(com, args)
        # Debug
        logger.debug("Removed %s" % path)

    ###################
    # DIRECTORIES
    def create_directory(self, directory, ignore_existing=True):
        self.create_empty(directory, directory=True, ignore_existing=ignore_existing)

    def remove_directory(self, directory, ignore=False):
        self.remove(directory, recursive=True, force=ignore)
