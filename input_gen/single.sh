# start
> $RCAC_SCRATCH/input3/max2048/start$1.txt
j=$(( $1 + 3))
> $RCAC_SCRATCH/input3/max2048/start$1.txt

k=$(( $j + 1))
l=$(( $k + 3))
echo $1 $j $k $l
qsub -F "$1 $j 2048" -N $1-$j input.sub
qsub -F "$k $l 2048" -N $k-$l input.sub
