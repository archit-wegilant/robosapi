import sys
import os


class Analyzer:
    """

    This is the starting point of the CSV-analyzer.
    
    """

    def __init__(self, remote_json_file_path):
        self.remote_path_to_json = remote_json_file_path
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
