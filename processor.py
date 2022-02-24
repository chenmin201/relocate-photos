import csv
import os
import pathlib


class Processor:
    source_csv_file = None
    dest_folder = None
    des_column_name = None
    src_column_name = None

    def __init__(self, source_csv_file, dest_folder, des_column_name, src_column_name):
        if not source_csv_file:
            raise Exception("source can not be empty")
        self.source_csv_file = source_csv_file

        if not dest_folder:
            raise Exception("destination folder can not be empty")
        self.dest_folder = dest_folder

        if not des_column_name:
            raise Exception("dest column name can not be empty")
        self.des_column_name = des_column_name

        if not src_column_name:
            raise Exception("source column name can not be empty")
        self.src_column_name = src_column_name

    def move(self):
        with open(self.source_csv_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                if self.des_column_name not in row:
                    raise Exception(self.des_column_name +
                                    " colmun does not exist in the CSV file")
                if self.src_column_name not in row:
                    raise Exception(self.src_column_name +
                                    " column does not exist in the CSV file")
                if not os.path.exists(row[self.src_column_name]):
                    print(row[self.src_column_name] +
                          " does not exist. skipping")
                    continue

                dir_dest = os.path.join(
                    self.dest_folder, row[self.des_column_name])
                file_dest = os.path.join(
                    dir_dest, os.path.basename(row[self.src_column_name]))

                print("moving " +
                      row[self.src_column_name] + " to " + file_dest)
                pathlib.Path(dir_dest).mkdir(parents=True, exist_ok=True)
                os.rename(row[self.src_column_name], file_dest)
