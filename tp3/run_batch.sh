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
export_path="data/last_run"

stop_condition=content
crossover_algorithm=one_point
mutation_algorithm=uniform_gen

selection_algorithm_1=roulette
selection_algorithm_2=probabilistic_tournament
selection_algorithm_3=roulette
selection_algorithm_4=probabilistic_tournament
selection_algorithm_5=tournament

scaling_algorithm=none
initial_temperature=100
temperature_step=0.1

replacement_method=1

percentage_for_selection=0.5
percentage_for_replacement=0.5

max_generation=10000
fitness_max=48

population_percentage_to_say_equals=0.7
generation_number_to_say_equals=500

prob_mutation=0.2
rate_mutation=0.001

: <<'COMMENT'
for i in 'one_point' 'two_points' 'uniform' 'anular'
do
    echo $i
    export_path="data/${i}"
    python main.py -ex $export_path -sd $seed -sc $stop_condition -ca $i -ma $mutation_algorithm -atm $attack_multiplier -dfm $defense_multiplier \
    -frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
    -w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $scaling_algorithm -it $initial_temperature  -ts $temperature_step \
    -rpm $replacement_method -sa1 $selection_algorithm_1 -sa2 $selection_algorithm_2 -sa3 $selection_algorithm_3 -sa4 $selection_algorithm_4 \
    -sa5 $selection_algorithm_5 -max_g $max_generation -fm $fitness_max -p1 $percentage_for_selection -p2 $percentage_for_replacement \
    -pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm $prob_mutation -rm $rate_mutation -k $k
done

for i in 'uniform_gen'
do
    echo $i
    export_path="data/${i}"
    python main.py -ex $export_path -sd $seed -sc $stop_condition -ca $crossover_algorithm -ma $i -atm $attack_multiplier -dfm $defense_multiplier \
    -frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
    -w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $scaling_algorithm -it $initial_temperature  -ts $temperature_step \
    -rpm $replacement_method -sa1 $selection_algorithm_1 -sa2 $selection_algorithm_2 -sa3 $selection_algorithm_3 -sa4 $selection_algorithm_4 \
    -sa5 $selection_algorithm_5 -max_g $max_generation -fm $fitness_max -p1 $percentage_for_selection -p2 $percentage_for_replacement \
    -pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm $prob_mutation -rm $rate_mutation -k $k
done

for i in 'non_uniform_gen'
do
    echo $i
    export_path="data/${i}"
    python main.py -ex $export_path -sd $seed -sc $stop_condition -ca $crossover_algorithm -ma $i -atm $attack_multiplier -dfm $defense_multiplier \
    -frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
    -w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $scaling_algorithm -it $initial_temperature  -ts $temperature_step \
    -rpm $replacement_method -sa1 $selection_algorithm_1 -sa2 $selection_algorithm_2 -sa3 $selection_algorithm_3 -sa4 $selection_algorithm_4 \
    -sa5 $selection_algorithm_5 -max_g $max_generation -fm $fitness_max -p1 $percentage_for_selection -p2 $percentage_for_replacement \
    -pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm 0.4 -rm $rate_mutation -k $k
done

for i in 'uniform_multi_gen'
do
    echo $i
    export_path="data/${i}"
    python main.py -ex $export_path -sd $seed -sc $stop_condition -ca $crossover_algorithm -ma $i -atm $attack_multiplier -dfm $defense_multiplier \
    -frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
    -w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $scaling_algorithm -it $initial_temperature  -ts $temperature_step \
    -rpm $replacement_method -sa1 $selection_algorithm_1 -sa2 $selection_algorithm_2 -sa3 $selection_algorithm_3 -sa4 $selection_algorithm_4 \
    -sa5 $selection_algorithm_5 -max_g $max_generation -fm $fitness_max -p1 $percentage_for_selection -p2 $percentage_for_replacement \
    -pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm 0.03 -rm $rate_mutation -k $k
done

for i in 'non_uniform_multi_gen'
do
    echo $i
    export_path="data/${i}"
    python main.py -ex $export_path -sd $seed -sc $stop_condition -ca $crossover_algorithm -ma $i -atm $attack_multiplier -dfm $defense_multiplier \
    -frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
    -w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $scaling_algorithm -it $initial_temperature  -ts $temperature_step \
    -rpm $replacement_method -sa1 $selection_algorithm_1 -sa2 $selection_algorithm_2 -sa3 $selection_algorithm_3 -sa4 $selection_algorithm_4 \
    -sa5 $selection_algorithm_5 -max_g $max_generation -fm $fitness_max -p1 $percentage_for_selection -p2 $percentage_for_replacement \
    -pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm $prob_mutation -rm $rate_mutation -k $k
done

COMMENT

for i in 1 2 3
do
    echo $i
    export_path="data/${i}"
    python3 main.py -ex $export_path -sd $seed -sc $stop_condition -ca $crossover_algorithm -ma $mutation_algorithm -atm $attack_multiplier -dfm $defense_multiplier \
    -frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
    -w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $scaling_algorithm -it $initial_temperature  -ts $temperature_step \
    -rpm $i -sa1 $selection_algorithm_1 -sa2 $selection_algorithm_2 -sa3 $selection_algorithm_3 -sa4 $selection_algorithm_4 \
    -sa5 $selection_algorithm_5 -max_g $max_generation -fm $fitness_max -p1 $percentage_for_selection -p2 $percentage_for_replacement \
    -pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm $prob_mutation -rm $rate_mutation -k $k
done

: <<'COMMENT'
for i in 'none' 'boltzmann'
do
    echo $i
    export_path="data/${i}"
    python main.py -ex $export_path -sd $seed -sc $stop_condition -ca $crossover_algorithm -ma $mutation_algorithm -atm $attack_multiplier -dfm $defense_multiplier \
    -frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
    -w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $i -it $initial_temperature  -ts $temperature_step \
    -rpm $replacement_method -sa1 roulette -sa2 $selection_algorithm_2 -sa3 roulette -sa4 $selection_algorithm_4 \
    -sa5 $selection_algorithm_5 -max_g $max_generation -fm $fitness_max -p1 1.0 -p2 1.0 \
    -pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm $prob_mutation -rm $rate_mutation -k $k
done

for i in 'elite' 'roulette' 'universal' 'tournament' 'probabilistic_tournament' 'ranking'
do
    echo $i
    export_path="data/sel1_full_${i}"
    python main.py -ex $export_path -sd $seed -sc $stop_condition -ca $crossover_algorithm -ma $mutation_algorithm -atm $attack_multiplier -dfm $defense_multiplier \
    -frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
    -w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $scaling_algorithm -it $initial_temperature  -ts $temperature_step \
    -rpm $replacement_method -sa1 $i -sa2 $selection_algorithm_2 -sa3 $selection_algorithm_3 -sa4 $selection_algorithm_4 \
    -sa5 $selection_algorithm_5 -max_g $max_generation -fm $fitness_max -p1 1.0 -p2 $percentage_for_replacement \
    -pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm $prob_mutation -rm $rate_mutation -k $k
done

COMMENT

for i in 'elite' 'roulette' 'universal' 'tournament' 'probabilistic_tournament' 'ranking'
do
    echo $i
    export_path="data/rpm2_sel3_full_${i}"
    python3 main.py -ex $export_path -sd $seed -sc $stop_condition -ca $crossover_algorithm -ma $mutation_algorithm -atm $attack_multiplier -dfm $defense_multiplier \
    -frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
    -w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $scaling_algorithm -it $initial_temperature  -ts $temperature_step \
    -rpm 2 -sa1 $selection_algorithm_1 -sa2 $selection_algorithm_2 -sa3 $i -sa4 $selection_algorithm_4 \
    -sa5 $selection_algorithm_5 -max_g $max_generation -fm $fitness_max -p1 $percentage_for_selection -p2 1.0 \
    -pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm $prob_mutation -rm $rate_mutation -k $k
done

for i in 'elite' 'roulette' 'universal' 'tournament' 'probabilistic_tournament' 'ranking'
do
    echo $i
    export_path="data/sel5_${i}"
    python3 main.py -ex $export_path -sd $seed -sc $stop_condition -ca $crossover_algorithm -ma $mutation_algorithm -atm $attack_multiplier -dfm $defense_multiplier \
    -frm $force_multiplier -agm $agility_multiplier -exm $expertise_multiplier -rsm $resistance_multiplier -lfm $life_multiplier \
    -w $weapons -b $boots -hm $helmets -g $gloves -s $shirts -sca $scaling_algorithm -it $initial_temperature  -ts $temperature_step \
    -rpm $replacement_method -sa1 $selection_algorithm_1 -sa2 $selection_algorithm_2 -sa3 $selection_algorithm_3 -sa4 $selection_algorithm_4 \
    -sa5 $i -max_g $max_generation -fm $fitness_max -p1 $percentage_for_selection -p2 $percentage_for_replacement \
    -pe $population_percentage_to_say_equals -ne $generation_number_to_say_equals -pm $prob_mutation -rm $rate_mutation -k $k
done


