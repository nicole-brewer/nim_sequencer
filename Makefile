CC=c99

.PHONY: clean

clean: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -rf {} +

all: single find_period

single: src/single.c
	$(CC) -o bin/single src/single.c 

find_period: src/find_period.c
	$(CC) -o bin/find_period src/find_period.c

# The .PHONY tells Make to always execute this 
# rule if we run "make clean". Phony target means
# that it doesn't build anything.
