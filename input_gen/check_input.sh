# ./check_input $max
max=$1

lastline=$(tail -n 1 $HOME/runtimes/input3/input$max.txt)
if [ "$lastline" == "Finished!" ]
then
	printf "Finished! Wordcount: $(wc -l $RCAC_SCRATCH/input3/input$max.txt)\n"
	cat $RCAC_SCRATCH/input3/input$max.txt | shuf -o $RCAC_SCRATCH/input3/input$max.txt
	printf "File is shuffled\n"
else
	printf "Last line: $(tail -n 1 $RCAC_SCRATCH/input3/input$max.txt)\n"
fi
