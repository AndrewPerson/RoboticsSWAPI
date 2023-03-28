from typing import TypeVar
from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import Callable, Any
import asyncio
import requests

base = "https://swapi.dev/api"


def get_resource(url: str):
    return async_resource(requests.get, url)


def get_resource_relative(path: str):
    return get_resource(f"{base}/{path}")


def async_resource(request_func: Callable[[str, ...], Any], url: str):
    loop = asyncio.get_event_loop()
    return loop.run_in_executor(None, request_func, url)


SWAPIResourceTypeVar = TypeVar("SWAPIResourceTypeVar", bound="SWAPIResource")


class SWAPIResource(BaseModel, ABC):
    @staticmethod
    @abstractmethod
    def get_root_path() -> str:
        pass

    @staticmethod
    async def get_all_generic(cls: SWAPIResourceTypeVar):
        url: str | None = f"{base}/{cls.get_root_path()}"

        while url != None:
            response = await get_resource(url)
            data = response.json()

            for starship_raw in data.get("results"):
                yield cls.parse_obj(starship_raw)

            url = data.get("next")

    @staticmethod
    @abstractmethod
    async def get_all():
        pass

    @staticmethod
    async def get_url(type: SWAPIResourceTypeVar, url: str):
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, requests.get, url)
        return type.parse_raw(response.text)

    @staticmethod
    async def get_generic(cls: SWAPIResourceTypeVar, id: int):
        response = await get_resource_relative(f"{cls.get_root_path()}/{id}")
        return cls.parse_raw(response.text)

    @staticmethod
    @abstractmethod
    async def get(id: int):
        pass

    @staticmethod
    async def search_generic(cls: SWAPIResourceTypeVar, search: str):
        pass

    @staticmethod
    @abstractmethod
    async def search(search: str):
        pass
