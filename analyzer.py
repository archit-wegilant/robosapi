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
import logging


class Analyzer:
    """

    This is the starting point of the CSV-analyzer application.
    This application is initiated by passing in a commond line argument which corresponds to the file path of the json file present at the calling PHP Server.
    
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


def set_logging_context:
    ## Todo: Set logging context
    pass


def main():

    if len(sys.argv) < 1:
        print "Usage: <cmd> <remote_file_path_to_json_file> "

        ## Todo call Watchdog to update Error Message in the Db before exiting.
        sys.exit()  ## Check if multiple objects are instanciated as the same time, will it kill all the objects?

    remote_file_path_to_json = sys.argv[1]

    try:
        ## Try to fetch the remote json file present at the file path given by remote_file_path_to_json
        pass
        
    except Exception as e:
        print e
        ## Todo call Watchdog to update Error Message in the Db before exiting.
        sys.exit()  ## Check if multiple objects are instanciated as the same time, will it kill all the objects?
    


## Boiler-plate
if __name__ == "__main__":
    main()
