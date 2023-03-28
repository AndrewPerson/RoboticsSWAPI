from enum import Enum
from converters import StrToFloat
from resource import SWAPIResource
from starship import Starship
from vehicle import Vehicle


class Gender(Enum):
    male = "male"
    female = "female"
    unknown = "unknown"
    na = "n/a"


class Person(SWAPIResource):
    @staticmethod
    def get_root_path() -> str:
        return "people"

    @staticmethod
    def get_all():
        return SWAPIResource.get_all_generic(Person)

    @staticmethod
    def get(id: int):
        return SWAPIResource.get_generic(Person, id)

    @staticmethod
    def search(search: str):
        return SWAPIResource.search_generic(Person, search)

    async def get_starships(self):
        for starship in self.starships:
            yield await SWAPIResource.get_url(Starship, starship)

    async def get_vehicles(self):
        for vehicle in self.vehicles:
            yield await SWAPIResource.get_url(Vehicle, vehicle)

    birth_year: str
    eye_color: str
    gender: Gender
    hair_color: str
    height: StrToFloat
    mass: StrToFloat
    skin_color: str
    homeworld: str
    species: list[str]
    starships: list[str]
    vehicles: list[str]
