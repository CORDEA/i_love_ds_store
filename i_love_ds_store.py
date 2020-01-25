from ds_store import DSStore

DS_STORE = '.DS_Store'

if __name__ == '__main__':
    with DSStore.open('./' + DS_STORE, 'w+') as dsStore:
        pass
