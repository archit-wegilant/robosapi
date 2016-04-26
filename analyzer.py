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
import requests
import httplib2


class Analyzer:
    """

    This is the starting point of the CSV-analyzer application.
    This application is initiated by passing in a commond line argument which corresponds to
    the file path of the json file present at the calling PHP Server.
    
    """

    def __init__(self, remote_url_path_to_json):
        self.remote_url_path_to_json = remote_url_path_to_json

        self.fetched_json = None

        self.customer_id = None
        self.job_id = None
        self.sub_job_id = None
        self.batch_size = None
        self.thread_count = None
        self.file_location = None
        self.record_count = None
        self.file_checksum = None
        self.file_type = None
        self.time_stamp = None
        self.expire_validation = None
        self.python_server_id = None
        self.app_url = None
        self.request_type = None

    def fetch_json_from_remote(self):
        """

        This method fetches the json file from the PHP Server by making a GET request call to the remote url provided.
        Currently, it fetches the json file using the request method present in the httplib2 module. In future, replace this with get method of requests module.
        Then, if the response code is greater than or equal to 400, then the Watchdog is updated with proper error message/code and False is returned.
        If the JSON file is fetched successfully, then True is returned otherwise False.
        The fetched JSON is stored in fetched_json instance variable of this class.

        Return values: True/False

        """
        
        try:
            http_object = httplib2.Http()
            url = self.remote_url_path_to_json

            # Fetching the JSON by making a GET Request to the PHP Server.
            response, content = http_object.request(url,'GET')

            if response.status >= 400:  # When the json is not fetched due to some reason
                # Update Watchdog with Error message
                return False
            
            result_as_json = json.loads(content)

            self.fetched_json = result_as_json
            return True
        
        except Exception as e:
            print e # TODO: Remove print statement and log the error in the log file including in it the error object 'e'
            return False


    def fetch_csv_from_remote(self):
        pass


    def parse_json(self):
        """

        This method parses the fetched JSON. The JSON file should contain the following keys with their values:
        1. customer_id
        2. job_id
        3. sub_job_id
        4. batch_size
        5. thread_count
        6. file_location
        7. record_count
        8. file_checksum
        9. file_type
        10. time_stamp
        11. expire_validation
        12. python_server_id
        13. app_url
        14. request_type

        Return values: True/False

        """
        try:
            self.customer_id = self.fetched_json['customer_id']
            self.job_id = self.fetched_json['job_id']
            self.sub_job_id = self.fetched_json['sub_job_id']
            self.batch_size = self.fetched_json['batch_size']
            self.thread_count = self.fetched_json['thread_count']
            self.file_location = self.fetched_json['file_location']
            self.record_count = self.fetched_json['record_count']
            self.file_checksum = self.fetched_json['file_checksum']
            self.file_type = self.fetched_json['file_type']
            self.time_stamp = self.fetched_json['time_stamp']
            self.expire_validation = self.fetched_json['expire_validation']
            self.python_server_id = self.fetched_json['python_server_id']
            self.app_url = self.fetched_json['app_url']
            self.request_type = self.fetched_json['request_type']

            return True
        
        except KeyError:
            print "JSON file fetched does not contains some of the keys." # TODO: Log this error in the Log file and remove the print statement. 
            return False

        except Exception as e:
            print e
            return False

    def compare_python_server_id(self):
        """

        This method is used to check whether the request has been made to the correct Python server. In future, there could be multiple Python servers.
        To make sure that the PHP Server has made the request to the correct Python server, a python_server_id is compared.
        The fetched JSON contains a python_server_id which is a Numerical value. Then the python_server_id for this current machine/server is retrieved
        from the Database/config file. As of now, it is defaulted to 1.
        
        """
        # TODO: Write the logic to fetch python server ID from the Db
        python_server_id_for_this_machine = 1
        
        return (python_server_id_for_this_machine == self.python_server_id)


    def compare_csv_checksum(self):
        pass


def set_logging_context():
    ## TODO: Set the logging context
    pass


def main():

    # Set logging context and start logging messages.
    set_logging_context()

    if len(sys.argv) < 1:
        print "Usage: <cmd> <remote_file_path_to_json_file> "

        ## TODO call Watchdog to update Error Message in the Db before exiting.
        sys.exit()  ## Check if multiple objects are instantiated as the same time, will it kill all the objects?

    remote_url_path_to_json = sys.argv[1]

    json_file_fetched_successfully = False
    try:
        ## Try to fetch the remote json file present at the file path given by remote_file_path_to_json

        if remote_url_path_to_json is not None:    ## Double checking whether remote_file_path_to_json is not None!

            analyzer_object = Analyzer(remote_url_path_to_json)    ## Instantiating the Analyzer object
            json_file_fetched_successfully = analyzer_object.fetch_json_from_remote()   ## json_file_fetched_successfully is set according depending on whether the json file is fetched from the PHP Server or not.
        
    except Exception as e:
        print e
        ## TODO call Watchdog to update Error Message in the Db before exiting.
        sys.exit()  ## Check if multiple objects are instantiated as the same time, will it kill all the objects?
    
    if json_file_fetched_successfully:
        json_file_parsed_successfully = analyzer_object.parse_json()    ## 1. Parse the fetched json file, which is present locally, by calling parse_json() method

        if json_file_parsed_successfully:
            python_server_id_matched = analyzer_object.compare_python_server_id()   ## 2. Match python server id by calling compare_python_server_id method,

            if python_server_id_matched:
                ## TODO list:
                ## 3. Fetch the csv file from remote by calling fetch_csv_from_remote method,
                ## 4. Compare the checksum of the csv file, by calling compare_csv_checksum method
                pass

        else:
            ## TODO call Watchdog to update Error Message in the Db before exiting.
            sys.exit()  ## Check if multiple objects are instantiated as the same time, will it kill all the objects?
            
        
## Boiler-plate
if __name__ == "__main__":
    main()
