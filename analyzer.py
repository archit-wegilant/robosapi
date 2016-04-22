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
    This application is initiated by passing in a commond line argument which corresponds to
    the file path of the json file present at the calling PHP Server.
    
    """

    def __init__(self, remote_file_path_to_json):
        self.remote_path_to_json = remote_file_path_to_json
        self.local_path_to_json = None


    def fetch_json_from_remote(self):
        pass


    def fetch_csv_from_remote(self):
        pass


    def parse_json(self):
        pass


    def compare_python_server_id(self):
        pass


    def compare_csv_checksum(self):
        pass


def set_logging_context:
    ## TODO: Set logging context
    pass


def main():

    if len(sys.argv) < 1:
        print "Usage: <cmd> <remote_file_path_to_json_file> "

        ## TODO call Watchdog to update Error Message in the Db before exiting.
        sys.exit()  ## Check if multiple objects are instantiated as the same time, will it kill all the objects?

    remote_file_path_to_json = sys.argv[1]

    json_file_fetched_successfully = False
    try:
        ## Try to fetch the remote json file present at the file path given by remote_file_path_to_json

        if remote_file_path_to_json is not None:    ## Double checking whether remote_file_path_to_json is not None!
            analyzer_object = Analyzer(remote_file_path_to_json)    ## Instantiating the Analyzer object
            json_file_fetched_successfully = analyzer_object.fetch_json_from_remote()
            ## If the json file is fetched, then before leaving the try-except block, set json_file_fetched_successfully to True
            ## json_file_fetched_successfully = True

        pass
        
    except Exception as e:
        print e
        ## TODO call Watchdog to update Error Message in the Db before exiting.
        sys.exit()  ## Check if multiple objects are instantiated as the same time, will it kill all the objects?
    
    if json_file_fetched_successfully:
        ## TODO list:
        ## 1. Parse the fetched json file, which is present locally, by calling parse_json method,
        ## 2. Match python server id by calling compare_python_server_id method,
        ## 3. Fetch the csv file from remote by calling fetch_csv_from_remote method,
        ## 4. Compare the checksum of the csv file, by calling compare_csv_checksum method
        
## Boiler-plate
if __name__ == "__main__":
    main()
