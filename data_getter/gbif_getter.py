'''
Author: Rick Morris
Repo: https://github.com/rmclimber/LionEyes

This file parses URLs for GBIF in order to download data.

References (for Rick):

'''

import asyncio
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

        # open TSV from GBIF
        df = pd.read_csv(download_file, sep=self.TAB)

        # create unique identifiers from referenes column values
        ids = list(df[self.COL_ID])
        id_codes = [id.split('/')[-1] for id in ids]

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



