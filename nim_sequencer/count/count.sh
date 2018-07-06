#!/bin/bash
#max
max=$1

echo "data/"
for data in input output skipped; do
    file="max$max.txt"
    path="$NIM/data/$data/$file"
    lines=$(wc -l $path 2>/dev/null)
    if  [[ $? -ne 0 ]]
    then
        lines=0
    else
        lines=$(echo $lines | cut -d ' ' -f 1)
    fi
    printf "|--$data/\n|     |--$lines\n"
done

