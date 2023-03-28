from converters import StrToInt, StrToFloat
from resource import SWAPIResource


class Starship(SWAPIResource):
    @staticmethod
    def get_root_path() -> str:
        return "starships"

    @staticmethod
    def get_all():
        return SWAPIResource.get_all_generic(Starship)

    @staticmethod
    def get(id: int):
        return SWAPIResource.get_generic(Starship, id)

    @staticmethod
    def search(search: str):
        return SWAPIResource.search_generic(Starship, search)

    name: str
    model: str
    starship_class: str
    manufacturer: str
    cost_in_credits: StrToFloat
    length: StrToFloat
    crew: StrToInt
    passengers: StrToInt
    max_atmosphering_speed: StrToFloat
    hyperdrive_rating: StrToFloat
    MGLT: StrToFloat
    cargo_capacity: StrToInt
    consumables: str
