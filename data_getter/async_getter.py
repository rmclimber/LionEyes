'''
Author: Rick Morris
Repo: https://github.com/rmclimber/LionEyes

This file handles multithreading for data downloads from GBIF.

References (for Rick):
https://realpython.com/python-concurrency/
https://codereview.stackexchange.com/questions/259112/async-download-of-files
https://www.twilio.com/blog/working-with-files-asynchronously-in-python-using-aiofiles-and-asyncio

'''

import asyncio
import httpx
import os
import urllib
import aiofiles

class AsyncGetter(object):
    def __int__(self, base_path: str='', sites: list=None):
        self.sites = sites
        self.base_path = base_path

    async def download_site(self, client, url):
        '''
        Downloads a single binary file from the url..

        :param client:
        :param url:
        :return:
        '''
        async with client.get(url) as response:
            filename = self.make_filename(url=url)
            async with aiofiles.open(filename, mode='w') as file:
                async for data in response.content.iter_raw():
                    await file.write(data)

    async def download_all_sites(self):
        client = httpx.Client()
        async with client:
            tasks = []
            for url in self.sites:
                task = asyncio.ensure_future(self.download_site(client, url))
                tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)

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