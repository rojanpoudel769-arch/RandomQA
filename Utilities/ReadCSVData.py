from __future__ import annotations
import csv
import os


class ReadCSVData:

    @staticmethod
    def read_data_from_csv(filename):
        # create an empty list
        data_list = []

        # get project root directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # create full path to csv
        file_path = os.path.join(base_dir, filename)

        # open csv file
        with open(file_path, "r") as csv_data:

            # create CSV reader
            reader = csv.reader(csv_data)

            # skip header
            next(reader)

            # Add CSV rows to list
            for rows in reader:
                data_list.append(rows)

        return data_list