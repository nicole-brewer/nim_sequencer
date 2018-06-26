# ./inner_loop.sh max

max=$1

for ((j = 1; j <= $max - 3; j++)) 
do
	for ((k = $j + 1; k <= $max - 2; k++))
	do
		for ((l = $k + 1; l <= $max - 1; l++)) 
		do
			printf "$j $k $l\n"
		done
	done
done

