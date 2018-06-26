if [ $1 -eq 512 ]
  then
	split -d -l 20000 -a 4 $IN/input512.txt $IN/max512/batch_
elif [ $1 -eq 1024 ]
  then
	split -d -l 2300 -a 4 $IN/input1024.txt $IN/max1024/batch_
elif [ $1 -eq 2048 ]
  then
	split -d -l 300 -a 4 $IN/input2048.txt $IN/max2048/batch_
else 
	echo "Usage: [max]"
fi

