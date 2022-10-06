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
    COL_TYPE = 'type'

    def __init__(self, base_path: str='', download_file=None):
        # pass base path to base class
        super(GBIFGetter, self).__init__(base_path=base_path)
        self.download_file = download_file
        self.files = self.parse_download_file(self.download_file)

    def set_download_files(self, download_file: str=None):
        """
        Can be called when a download file is not set in constructor.
        :param download_file: assumed to be TSV.
        :return:
        """
        if download_file is None:
            print("No filename")
            return None

        self.download_file = download_file
        self.files = self.parse_download_file(self.download_file)

    def parse_download_file(self, download_file: str=None):
        """
        Pulls the metadata necessary to download image data out of a GBIF TSV.

        :param download_file:
        :return:
        """
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
        """
        Runner for the ascynio download method in ASyncGetter.
        :return:
        """
        if self.files is None:
            print('Files not specified')
            return None

        targets = [{'identifier': k, 'url': v} for k, v in self.files.items()]
        self.run(targets=targets)

    def make_metadata_file(self, filename):
        # open TSV from GBIF
        df = pd.read_csv(self.download_file, sep=self.TAB)
        df = df.loc[df['type'] == 'StillImage', :]
        cols = [self.COL_TYPE, self.COL_ID, self.COL_URL]
        df = df.loc[:, cols]
        df.to_csv(filename, index=False)


if __name__ == '__main__':
    args = sys.argv
    command = args[1]
    input_filename = args[2]
    if len(args) > 2:
        output_filename = args[3]
    else:
        output_filename = None
    getter = GBIFGetter(base_path='../data/img/', download_file=input_filename)

    if command == 'get':
        getter.get_gbif_files()
    elif command == 'parse':
        getter.make_metadata_file(output_filename)