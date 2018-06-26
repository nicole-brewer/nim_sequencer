#PBS -l nodes=1:ppn=2
#PBS -l walltime=04:00:00
#PBS -e $HOME/error/input.txt
#PBS -o $HOME/runtimes/input.txt
#PBS -N input

# qsub -F "i j k max"
# creates all cardinality 4 subsets (without repeating numbers) from the set {1..max}t


max=$4
cd $HOME/input_gen
filename="$RCAC_SCRATCH/input3/input$max.txt"

printf "max: $max i: $1 j: $2 k: $3\n" >> $HOME/runtimes/input3/input$max.txt

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

printf "Finished!" >> $HOME/runtimes/input3/input$max.txt
