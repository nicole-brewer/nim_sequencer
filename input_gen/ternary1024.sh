max=1024
cd $HOME/input_gen
starttime=$(date +%s)
mkdir -p $RCAC_SCRATCH/input3/max$max/
mkdir -p $HOME/runtimes/input3/
> $HOME/runtimes/input3/input$1.txt

# intervals (1 - 16) (17 - 32) (...) (993 - 1008) (1009 - 1024) 

for ((i = 1; i <= 1009; i = i + 16))
do
	> $RCAC_SCRATCH/input3/max$max/start$i.txt
	((j = i + 15))
	qsub -F "$i $j $max" -N indexStart$i input.sub
	sleep 0.5 
done
