import asyncio
from pprint import pprint

from starship import Starship
from vehicle import Vehicle
from person import Person


async def net_worth(person: Person):
    value = 0

    async for starship in person.get_starships():
        value += cost if (cost := starship.cost_in_credits) is not None else 0

    async for vehicle in person.get_vehicles():
        value += cost if (cost := vehicle.cost_in_credits) is not None else 0

    return value


async def main():
    print(await net_worth(await Person.get(1)))

    async for vehicle in Vehicle.get_all():
        pprint(vehicle)

    async for starship in Starship.get_all():
        pprint(starship)


if __name__ == '__main__':
    asyncio.run(main())
