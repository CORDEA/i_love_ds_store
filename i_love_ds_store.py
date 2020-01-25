import os
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
    __walk('./')
