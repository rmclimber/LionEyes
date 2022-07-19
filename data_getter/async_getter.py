'''
Author: Rick Morris
Repo: https://github.com/rmclimber/LionEyes

This file handles multithreading for data downloads from GBIF.

References (for Rick):
https://realpython.com/python-concurrency/
https://codereview.stackexchange.com/questions/259112/async-download-of-files
https://www.twilio.com/blog/working-with-files-asynchronously-in-python-using-aiofiles-and-asyncio
https://pypi.org/project/aiofiles/
https://zetcode.com/python/httpx/
'''

import asyncio
import httpx
import os
import urllib
import aiofiles

class AsyncGetter(object):
    def __init__(self, base_path: str='', sites: list=None):
        self.sites = sites
        self.base_path = base_path

        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)

    async def download_site(self, client, url):
        '''
        Downloads a single binary file from the url and writes it to disk.

        :param client:
        :param url:
        :return:
        '''
        print('Starting download for: {}'.format(url))
        # response = client.get(url)
        filename = self.make_filename(url=url)
        print(filename)
        async with aiofiles.open(filename, mode='w') as file:
            print('file opened')
            with client.get(url) as response:
                print(response.status_code)
                async for data in response.iter_raw():
                    await file.write(data)
                print('finished writing')

    async def download_all_sites(self):
        '''
        Builds and executes the tasync task list for the data downloads.

        :return:
        '''
        with httpx.Client() as client:
            tasks = []
            for url in self.sites:
                task = asyncio.ensure_future(self.download_site(client, url))
                tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)
            print('Finished downloading')

    def run(self):
        asyncio.run(self.download_all_sites())

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
        print(filename)
        if not filename:
            raise ValueError("Invalid URL: please enter a URL with a valid filename")
        return self.base_path + filename


if __name__ == '__main__':
    sites = ['https://www.jython.org/index.html'] * 30
    getter = AsyncGetter(base_path='test//', sites=sites)
    getter.run()