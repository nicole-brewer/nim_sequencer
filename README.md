# nim_sequencer

My first undergraduate research project in which I implemented the KMP string matching algorithm to create a large data set for a combinatorial 
game theory problem. This was my first experience using HPC resources. The problem was trivially parallel, but not all of the threads were guarenteed to find
a solution given and would have to be run again. Manually taking care of this on every run became cumbersome, and the bulk of the project quickly became about
writing a command line interface that made file management and cluster submission much more maintainable. 

## More

My advisor had me I study and implement an algorithm and he connected me to the campus supercomputing clusters so I
could create a workflow to efficiently run this algorithm in parallel to generate the outcome data.
The challenge was that some runs of the algorithm required an indeterminate amount of computing resources, 
which required me to get creative about implementing a “guess and check” strategy. My advisor hinted that I 
might use a batching strategy, but it took me time to realize he was not going to give me instructions for how 
to accomplish my task directly. I started to understand that research was about intellectually independent problem 
solving. After struggling to manually queue runs with the right inputs several times a day, I took matters into my 
own hands and implemented a command line tool that managed data files and job submissions to the cluster. This was my 
first experience in HPC and research, but I was successfully able to use my programming and problem-solving skills to create
a reproducible and scalable scientific dataset. 
