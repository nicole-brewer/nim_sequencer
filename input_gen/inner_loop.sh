# ./inner_loop.sh i max filename

starttime=$(date +%s)

for ((j = $1 + 1; j <= $2 - 2; j++)) 
do
	for ((k = $j + 1; k <= $2 - 1; k++))
	do
		for ((l = $k + 1; l <= $2; l++)) 
		do
			printf "$1 $j $k $l\n" >> $3
		done
	done
done

