import asyncio
import aiohttp
from data import config


class Kwork:

    def __init__(self, login: str, password: str):
        self.session = aiohttp.ClientSession()
        self.login = login
        self.password = password
        self._token = None
        self.api_url = 'https://api.kwork.ru/'

    async def get_token(self):
        if self._token is None:
            async with self.session.post(url=self.api_url + 'signIn', data={
                'login': self.login,
                'password': self.password,
            }) as response:
                token = await response.json()
                return token["response"]["token"]

    # @property
    # async def token(self):
    #     if self._token is None:
    #         self._token = await self.get_token()
    #     return self._token

    async def keywords_search(self, keywords):
        async with self.session.post(url=self.api_url + 'projects',
                                     data={
                                         'query': keywords,
                                         'token': self._token,
                                     }) as response:
            answer = await response.json()
            if answer['success']:

                pages = answer['paging']['pages']
                posts = []
                for page in range(1, pages + 1):
                    async with self.session.post(url=self.api_url + 'projects',
                                                 data={
                                                     'query': keywords,
                                                     'token': self._token,
                                                     'page': page
                                                 }) as page_response:
                        page_answer = await page_response.json()
                        if page_answer['success']:
                            posts.extend(page_answer['response'])
                return posts
            else:
                return False

# kwo = Kwork(login=config.kwork_user, password=config.kwork_password)


kwo = Kwork(login=config.kwork_user, password=config.kwork_password)

