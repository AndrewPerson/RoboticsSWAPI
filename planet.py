from resource import SWAPIResource


class Planet(SWAPIResource):
    @staticmethod
    def get_root_path() -> str:
        return "planets"

    @staticmethod
    def get_all():
        return SWAPIResource.get_all_generic(Planet)

    @staticmethod
    def get(id: int):
        return SWAPIResource.get_generic(Planet, id)

    @staticmethod
    def search(search: str):
        return SWAPIResource.search_generic(Planet, search)

    name: str
    diameter: str
    rotation_period: str
    orbital_period: str
    gravity: str
    population: str
    climate: str
    terrain: str
    surface_water: str
