#!/bin/bash

stop_condition=generation_number
selection_algorithm=elite
crossover_algorithm=two_points
mutation_algorithm=gen

attack_multiplier=0.9
defense_multiplier=0.1

force_multiplier=0.9
agility_multiplier=1.1
expertise_multiplier=1
resistance_multiplier=0.9
life_multiplier=0.8

weapons=testdata/armas.tsv
boots=testdata/botas.tsv
helmets=testdata/cascos.tsv
gloves=testdata/guantes.tsv
shirts=testdata/pecheras.tsv

python ./main.py -sc $stop_condition -sa $selection_algorithm -ca $crossover_algorithm -ma $mutation_algorithm -am $attack_multiplier -dm $defense_multiplier \
-frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
-w $weapons -b $boots -hm $helmets -g $gloves -s $shirts
