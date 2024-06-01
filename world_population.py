import json

import pygal_maps_world.maps 
from country_codes import get_country_code
import pygal_maps_world
 
# import pygal

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population 

wm = pygal_maps_world.maps.World()
wm._title = 'World population in 2010, by Country'
wm.add('2010', cc_populations)
wm.render_to_file('world_population.svg')


# worldmap_chart = pygal.maps.world.World()
# worldmap_chart.title = 'Some countries'
# worldmap_chart.add('F countries', ['fr', 'fi'])
# worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg',
#                                    'mk', 'ml', 'mm', 'mn', 'mo',
#                                    'mr', 'mt', 'mu', 'mv', 'mw',
#                                    'mx', 'my', 'mz'])
# worldmap_chart.add('U countries', ['ua', 'ug', 'us', 'uy', 'uz'])
# worldmap_chart.render()