max=2048
cd $HOME/input_gen
starttime=$(date +%s)
mkdir -p $RCAC_SCRATCH/input3/max$max/
mkdir -p $HOME/runtimes/input3/
> $HOME/runtimes/input3/input$1.txt

# intervals (1 - 8) (9 - 16) (...) (2041 - 2048) 

for ((i = 1; i <= 485; i = i + 4))
do
	> $RCAC_SCRATCH/input3/max$max/start$i.txt
	((j = i + 3))
	qsub -F "$i $j $max" -N $i_$j input.sub
	sleep 0.5 
done
