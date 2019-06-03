#!/bin/bash

attack_multiplier=0.9
defense_multiplier=0.1

force_multiplier=0.9
agility_multiplier=1.1
expertise_multiplier=1.0
resistance_multiplier=0.9
life_multiplier=0.8

weapons=fulldata/armas.tsv
boots=fulldata/botas.tsv
helmets=fulldata/cascos.tsv
gloves=fulldata/guantes.tsv
shirts=fulldata/pecheras.tsv

population_size=100
k=50
seed=cRYEJJgvmksuIiEnJZJmdtBzsJjkxCHdAMvsSJkWLvEwucvJuByqumCUHKSSPhYAAbJpfcMQjEmqlazvURqjTLQDfxpMrZNGaJQU

stop_condition=structure
crossover_algorithm=one_point
mutation_algorithm=uniform_gen

selection_algorithm_1=roulette
selection_algorithm_2=probabilistic_tournament
selection_algorithm_3=roulette
selection_algorithm_4=probabilistic_tournament
selection_algorithm_5=tournament

scaling_algorithm=none
initial_temperature=100
temperature_step=1

replacement_method=1

percentage_for_selection=0.5
percentage_for_replacement=0.5

max_generation=1000
fitness_max=30

population_percentage_to_say_equals=0.7
generation_number_to_say_equals=10

prob_mutation=0.2
rate_mutation=0.2

python3 main.py -sc $stop_condition -ca $crossover_algorithm -ma $mutation_algorithm -atm $attack_multiplier -dfm $defense_multiplier \
-frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
-w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $scaling_algorithm -it $initial_temperature  -ts $temperature_step \
-rpm $replacement_method -sa1 $selection_algorithm_1 -sa2 $selection_algorithm_2 -sa3 $selection_algorithm_3 -sa4 $selection_algorithm_4 \
-sa5 $selection_algorithm_5 -max_g $max_generation -fm $fitness_max -p1 $percentage_for_selection -p2 $percentage_for_replacement \
-pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm $prob_mutation -rm $rate_mutation -k $k


