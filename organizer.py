#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__    = "nagracks"
__date__      = "14-07-2016"
__license__   = "MIT"
__copyright__ = "Copyright © 2016 nagracks"

import argparse
import collections
import os
import shutil

# Shortcut for os.path.join#
joinp = os.path.join

def parse_args():
    """Parse args with argparse
    :returns: args

    """
    parser = argparse.ArgumentParser(description="Organizer")
    parser.add_argument('-d',
                        '--directory',
                        dest='directory',
                        metavar='/full/directory/path',
                        action='store',
                        help="directory you want to organize")
    args = parser.parse_args()
    return args
    
class Organizer(object):
    """Organizer"""

    def __init__(self, path):
        self.path = path
        self.home_dir = os.path.expanduser('~')

    def filetype_dict(self):
        """Make dictionary of {[key=file-extension]:[value=files..]}
        :returns: dictionary, default dictionary class

        """
        # Make defaultdict #
        filetypes = collections.defaultdict(list)

        # Iterate over path #
        for ele in os.listdir(self.path):
            if os.path.isfile(joinp(self.path, ele)):
                # Get file-extension without dot #
                file_ext = os.path.splitext(ele)[-1].split('.')[-1]
                # Make dictionary pairs #
                filetypes[file_ext].append(ele)

        return filetypes

    def make_dirs(self):
        """Make require directories if they don't exist
        :returns: None

        """
        # Iterate on dictionary keys #
        # Make directories of present keys #
        # With condition, if dirs exists then pass on #
        # Else make directories #
        # path is /home/user/Organizer/keys.. #
        for dir_name in self.filetype_dict().keys():
            dir_path = joinp(self.home_dir, 'Organizer', dir_name)
            if os.path.exists(dir_path):
                pass
            else:
                os.mkdir(dir_path)

    def organize_files(self):
        """Organize/move all files to corresponding directories
        :returns: None

        """
        for k, v in self.filetype_dict().items():
            # Iterate over dictionary value #
            for files in v:
                # Make source and destination paths #
                src_path = joinp(self.path, files) 
                dst_path = joinp(self.home_dir, 'Organizer', k)
                # Move them #
                shutil.move(src_path, dst_path)

if __name__ == "__main__":
    # Commandline args #
    args = parse_args()

    org = Organizer(args.directory)
    org.make_dirs()
    org.organize_files()
