#!/usr/bin/env python
#

import argparse
import logging
import processor


def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    source_csv_file = args.src
    dest_folder = args.dest
    des_column_name = args.dest_col_name
    src_column_name = args.src_col_name

    csvProcessor = processor.Processor(
        source_csv_file, dest_folder, des_column_name, src_column_name)
    csvProcessor.move()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Relocate photos.')
    parser.add_argument('--src',
                        help='Source CSV location file of the photos')
    parser.add_argument('--dest',
                        help='Destination directory of the folders')
    parser.add_argument('--src-col-name',
                        help='Indicate the source column name of the CSV file')
    parser.add_argument('--dest-col-name',
                        help='Indicate the destination column name of the CSV file')
    parser.add_argument('-v',
                        '--verbose',
                        help='increase output verbosity',
                        action='store_true')

    args = parser.parse_args()

    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO

    main(args, loglevel)
