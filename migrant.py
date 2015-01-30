import argparse
import binascii
import datetime
import gzip
import json

import magic
import os
import pymongo
import sys


def read_gzip(filename):
    with gzip.open(filename) as file:
        content = file.read()
    return content


def read_plain(filename):
    with open(filename) as file:
        content = file.read()
    return content


readers = {
    b'application/x-gzip': read_gzip,
    b'text/plain': read_plain,
}


def read(filename):
    type = magic.from_file(filename, mime=True)
    return readers[type](filename).decode()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', help='path to moita configuration file',
                        dest='moita', metavar='MOITA', required=True)
    parser.add_argument('filename', nargs='+')
    args = parser.parse_args()

    sys.path.append(os.path.dirname(args.moita))
    import config

    connection = pymongo.MongoClient()
    collection = connection[config.DATABASE].timetables

    for file in args.filename:
        content = json.loads(read(file))

        identifier = binascii.unhexlify(
            os.path.basename(file).split('.', 1)[0]).decode()
        content['_id'] = identifier

        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        content['updated_at'] = mtime

        collection.save(content)

