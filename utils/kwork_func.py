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
                await self.session.close()
                return token["response"]["token"]
    @property
    async def token(self):
        if self._token is None:
            self._token = await self.get_token()
        return self._token


kwo = Kwork(login=config.kwork_user, password=config.kwork_password)

