import os
from optparse import OptionParser
from os import path

from ds_store import DSStore

DS_STORE = '.DS_Store'


def __generate_ds_store(base):
    with DSStore.open(path.join(base, DS_STORE), 'w'):
        pass


def __walk(base):
    for basePath, _, _ in os.walk(base):
        __generate_ds_store(basePath)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-d', '--dir', dest='dir', metavar='PATH')
    parser.add_option('-i',
                      '--ignore',
                      dest='ignore',
                      metavar='PATH',
                      action='append')
    (options, args) = parser.parse_args()
    __walk(options.dir)
