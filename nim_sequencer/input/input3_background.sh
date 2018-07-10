#!/usr/bin/bash
# input3_background.sh i j k max"
# creates all cardinality 4 subsets (without repetition) from the set {1..(max - 1)}

max=$4
filename=$5

for ((k = $3; k <= $max - 1; k++))
do
	stdbuf -oL printf "$1 $2 $k\n" >> $filename 
done

for ((j = $2 + 1; j <= $max - 2; j++))
do
	for ((k = j + 1; k <= $max - 1; k++)) 
	do
		stdbuf -oL printf "$1 $j $k\n" >> $filename
	done
done

for ((i = $1 + 1; i <= $max - 3; i++))
do
	for  ((j = i + 1; j <= $max - 2; j++)) 
	do
		for ((k = j + 1; k <= $max - 1; k++))
		do
			stdbuf -oL printf "$i $j $k\n" >> $filename 
		done
	done
done

cat $filename | shuf -o $filename
