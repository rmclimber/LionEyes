'''
Author: Rick Morris
Repo: https://github.com/rmclimber/LionEyes

This file handles multithreading for data downloads from GBIF.

References (for Rick):
https://realpython.com/python-concurrency/
'''

import asyncio
import httpx
import os
import urllib

class AsyncGetter(object):
    def __int__(self, base_path: str='', sites: list=None):
        self.sites = sites
        self.base_path = base_path

    async def download_site(self, session, url):
        pass

    async def download_all_sites(self):
        pass

    def run(self):
        pass

    def make_filename(self, url: str=''):
        '''
        Use this to extract the filename from a URL.

        :param url:
        :return filename:
        '''

        if not url:
            raise ValueError("Invalid URL: please enter a URL with a valid filename")
        url_path = urllib.parse.urlparse(url).path
        filename = os.path.basename(url_path)
        if not filename:
            raise ValueError("Invalid URL: please enter a URL with a valid filename")
        return self.base_path + filename