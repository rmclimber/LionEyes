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

    def __init__(self, download_file=None):
        super().__init__()
        self.download_file = download_file
        self.files = self.parse_download_file(self.download_file)

    def parse_download_file(self, download_file: str=None):
        if download_file is None:
            print("No filename")
            return None

        df = pd.read_csv(download_file, sep=self.TAB)

        # TODO: create unique identifiers (from iNat column) for ID.jpg
        # TODO: take identifier column as URL and references column final portion as filename basis


