#PBS -l nodes=4:ppn=20
#PBS -l walltime=04:00:00
#PBS -e $HOME/error/input.txt
#PBS -o $HOME/runtimes/input.txt
#PBS -N input

# qsub -F "max"
# creates all cardinality 4 subsets (without repeating numbers) from the set {1..max}t

nodes=4
cores=$(expr 20 \* $nodes)
max=$1
cd $HOME/input_gen
starttime=$(date +%s)
filename="$RCAC_SCRATCH/input/input$1.txt"
mkdir -p $RCAC_SCRATCH/input/
mkdir -p $HOME/runtimes
> $filename
> $HOME/runtimes/input$1.txt

for ((i = 1; i <= $max - 3; i++))
do
	((n=n%($cores * 4 - 1))); ((n++==0)) && wait
	./inner_loop.sh $i $max $filename &
done
wait
# output should have max choose 4 lines
cat $filename | shuf -o $filename

endtime=$(date +%s)
printf "$max $(wc -l $filename) $nodes $(expr $endtime - $starttime)\n" >> $HOME/runtimes/input$max.txt
