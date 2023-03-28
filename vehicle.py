from converters import StrToInt, StrToFloat
from resource import SWAPIResource


class Vehicle(SWAPIResource):
    @staticmethod
    def get_root_path() -> str:
        return "vehicles"

    @staticmethod
    def get_all():
        return SWAPIResource.get_all_generic(Vehicle)

    @staticmethod
    def get(id: int):
        return SWAPIResource.get_generic(Vehicle, id)

    @staticmethod
    def search(search: str):
        return SWAPIResource.search_generic(Vehicle, search)

    name: str
    model: str
    vehicle_class: str
    manufacturer: str
    length: StrToFloat
    cost_in_credits: StrToInt
    crew: StrToInt
    passengers: StrToInt
    max_atmosphering_speed: StrToFloat
    cargo_capacity: StrToInt
    consumables: str
