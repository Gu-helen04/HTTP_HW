import requests
from pprint import pprint
from yadisk import YaDisk

if __name__ == '__main__':
    token = ''
    yadisk = YaDisk(token)
    yadisk.upload_file('/backup/hw_.txt', 'hw_.txt')
