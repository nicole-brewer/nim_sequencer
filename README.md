# nim_sequencer

My first undergraduate research project in which I implemented the KMP string matching algorithm to create a large data set for a combinatorial 
game theory problem. This was my first experience using HPC resources. The problem was trivially parallel, but not all of the threads were guarenteed to find
a solution given and would have to be run again. Manually taking care of this on every run became cumbersome, and the bulk of the project quickly became about
writing a command line interface that made file management and cluster submission much more maintainable. 

## More

My advisor had me study and implement a string matching algorithm in C so I could detect the length of repeating sequences in infinitely long strings. To detect the repeating sequence, I had to use an array longer that was at least as large as the sequence itself. The challenge was that the length of the sequence was indeterminate, so I had no way to know how long of an array to use. Execution of the algorithm was proportional to the array size, so it was to my benefit to use the smallest array possible. In response, I had to get creative about implementing a “guess and check” batching strategy to maintain a reasonable walltime; I would run the sequence detection with a small array and then re-run those that weren’t detected with a larger array.
After struggling to manually queue runs with the right inputs several times a day, I took matters into my 
own hands and implemented a command line tool that managed data files and job submissions to the cluster. This was my 
first experience in HPC and research, but I was successfully able to use my programming and problem-solving skills to create
a reproducible and scalable scientific dataset. 
