import json

import pygal.maps.world as pyg
from country_codes import get_country_code

filename = "..\data\population_data.json"
with open(filename) as file:
    pop_data = json.load(file)

    cc_populations = {}

    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            code = get_country_code(country_name)
            # country_code = pop_dict['Country Code']
            population = int(float(pop_dict['Value']))

            if code:
                cc_populations[code] = population

    cc_pops1 = {}
    cc_pops2 = {}
    cc_pops3 = {}
    for cc, pop in cc_populations.items():
        if pop < 10000000:
            cc_pops1[cc] = pop
        elif pop < 100000000:
            cc_pops2[cc] = pop
        else:
            cc_pops3[cc] = pop

wm = pyg.World()
wm.title = 'world population in 2010'
#wm.add('2010', cc_populations)
wm.add('2010(0-10m)', cc_pops1)
wm.add('2010(10m-1bn)', cc_pops2)
wm.add('2010(>1bn)', cc_pops3)

wm.render_to_file('svg_data\world_population.svg')
