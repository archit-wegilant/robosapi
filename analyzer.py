'''
#=============================================================================
#     FileName: analyzer.py
#       Author: Archit Kapoor
#        Email: archit.imsec10@gmail.com
#=============================================================================
'''

import sys
import os
import json


class Analyzer:
    """

    This is the starting point of the CSV-analyzer application.
    
    """

    def __init__(self, remote_file_path_to_json):
        self.remote_path_to_json = remote_file_path_to_json
        self.local_path_to_json = None


    def fetch_json_from_remote(self):
        pass


    def parse_json(self):
        pass


    def compare_python_server_id(self):
        pass


    def fetch_csv(self):
        pass


    def compare_csv_checksum(self):
        pass


def main():

    if len(sys.argv) < 1:
        print "Usage: <cmd> <remote_file_path_to_json_file> "

        ## Todo call Watchdog to update Error Message in the Db before exiting.
        sys.exit()

    remote_file_path_to_json = sys.argv[1]



## Boiler-plate
if __name__ == "__main__":
    main()
