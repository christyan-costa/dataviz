import json

from country_codes import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

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

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10_000_000:
        cc_pops_1[cc] = pop
    elif pop < 1_000_000_000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Print how many countries are in each level.
print(f"number of countries -- population group")
print(f"{len(cc_pops_1)} -- less than 10 million")
print(f"{len(cc_pops_2)} -- between 10 million and 1 billion")
print(f"{len(cc_pops_3)} -- more than 1 billion")

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm._title = 'World population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')
