'''
Author: Rick Morris
Repo: https://github.com/rmclimber/LionEyes

This file parses URLs for GBIF in order to download data.

References (for Rick):

'''

import asyncio
import sys

import httpx
import os
import urllib
import aiofiles
import pandas as pd
from async_getter import AsyncGetter

class GBIFGetter(AsyncGetter):
    TAB = '\t'
    COL_ID = 'references'
    COL_URL = 'identifier'

    def __init__(self, base_path: str='', download_file=None):
        # pass base path to base class
        super(GBIFGetter, self).__init__(base_path=base_path)
        self.download_file = download_file
        self.files = self.parse_download_file(self.download_file)

    def set_download_files(self, download_file: str=None):
        if download_file is None:
            print("No filename")
            return None

        self.download_file = download_file
        self.files = self.parse_download_file(self.download_file)

    def parse_download_file(self, download_file: str=None):
        if download_file is None:
            print("No filename")
            return None

        print(f'Parsing GBIF download file: {download_file}')

        # open TSV from GBIF
        df = pd.read_csv(download_file, sep=self.TAB)

        # create unique identifiers from references column values
        ids = list(df[self.COL_ID])
        id_codes = [str(id).split('/')[-1] for id in ids]

        # create dictionary with identifiers as key and URL as value
        return dict(zip(id_codes, df[self.COL_URL]))

    def make_filename(self, identifier, url):
        '''
        Builds a new filename based on the iNaturalist identifier, the base
        path, and the file extension.

        :param identifier: unique iNaturalist identifier for picture
        :param url: resource location
        :return: new filename
        '''

        if not url:
            raise ValueError("Empty URL")
        url_path = urllib.parse.urlsplit(url).path
        filename = identifier
        _, file_extension = os.path.splitext(url_path)
        filename += file_extension
        return self.base_path + filename

    def get_gbif_files(self):
        if self.files is None:
            print('Files not specified')
            return None

        targets = [{'identifier': k, 'url': v} for k, v in self.files.items()]
        self.run(targets=targets)


if __name__ == '__main__':
    args = sys.argv
    filename = args[1]
    getter = GBIFGetter(base_path='../data/img/', download_file=filename)
    getter.get_gbif_files()