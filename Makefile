CC=c99

.PHONY: clean

clean: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -rf {} +

all: single2 single3 find_period

single2: c_programs/single_set_v4squared.c
	$(CC) -o bin/single2 src/single_set_v4squared.c 

single3: c_programs/single_set_v4cubed.c
	$(CC) -o bin/single3 src/single_set_v4cubed.c

find_period: c_programs/find_period.c
	$(CC) -o bin/find_period src/find_period.c

# The .PHONY tells Make to always execute this 
# rule if we run "make clean". Phony target means
# that it doesn't build anything.
