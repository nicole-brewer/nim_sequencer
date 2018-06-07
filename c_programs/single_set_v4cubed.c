#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define PRINT 0
#define ITERATIONS 5 

int g_of_x (int n, short* g_values) {

  int i, j, temp;

  for (i = 0; i < n; i++) {
    j = i;
    while (j > 0 && g_values[j] < g_values[j - 1]) {
      temp = g_values[j];
      g_values[j] = g_values[j - 1];
      g_values[j - 1] = temp;
      j--;

    }
  }
  int ret = 0;
  for (i = 0; i < n; i++) {
    if (g_values[i] == ret) {
      ret = ret + 1;
    }
  }
  return ret;
}

int kmp(short* pattern, unsigned long* overlap, unsigned long cachesize) {
  unsigned long i;
  overlap[0] = -1;

  for (i = 0; i < cachesize; i++) {
    overlap[i + 1] = overlap[i] + 1;
    while (overlap[i + 1] > 0 && pattern[i] != pattern[overlap[i + 1] - 1]) {
      overlap[i + 1] = overlap[overlap[i + 1] - 1] + 1;
    }
  }
  return overlap[cachesize];
}

unsigned long findPeriod (short* g, unsigned long cachesize, short* subtraction_set, unsigned long* overlap) { 
  int i, num_g_previous;
  unsigned long x;
  unsigned long subtracted_index;
  short g_previous[4];
  int periodFound = 0;
  unsigned long index = 0;
  unsigned long iter = 0;
  unsigned long tempPeriod = 0;

  while (iter < ITERATIONS) {
  // fill up g with cachesize numbers and check for periodicity 200 times.
  // This ought to get you though the preperiod. If you complete the loop
  // without breaking, the cachesize is too small to fit the period

    for (x = 0; x < cachesize; x++) {

      num_g_previous = 0; // number of positive g previous

      for (i = 0; i < 4; i++) {
        if (index >= subtraction_set[i]) {
          num_g_previous++;
          g_previous[i] = g[(index - subtraction_set[i]) % cachesize];
        }
      }

      if (num_g_previous == 0) {
        g[index % cachesize] = 0;
      } else {
        g[index % cachesize] = g_of_x(num_g_previous, g_previous);
      }
      index++;
    }

    // PRINT: prints g values every 2 * (v1 + v2) iterations
    if (PRINT && index % cachesize == 0) {
      unsigned long k;
      printf("\n");
      for (k = 0; k < cachesize; k++) {
        printf("%d", g[k]);
      }
      printf("\n");
    } //END PRINT

    tempPeriod = kmp(g, overlap, cachesize);
    if (tempPeriod >= subtraction_set[3]) {
      break; //period found
    }
    iter++;  // while loop iterate
  }
  if (iter == ITERATIONS) {
    printf("Period not found\n");
    return 0;
  }
  return (cachesize - tempPeriod);
}

int main (int argc, char *argv[]) {

  // input validation
  int i, j, k, l;
  if (argc == 5) {
    i = atoi(argv[1]);
    j = atoi(argv[2]);
    k = atoi(argv[3]);
    l = atoi(argv[4]);
  }
  if (argc != 5) {
    printf("Please enter four integer values when running this program.\n");
    return 0;
  }
  // end input validation

  // initialization
  unsigned long cachesize = l * l * l;   // just a guess
  short* g = malloc(sizeof(short)*cachesize);
  unsigned long* overlap = malloc(sizeof(unsigned long)*cachesize);
  short subtraction_set[4] = {i, j, k, l};
  unsigned long period;
  // end initialization
  
    period = findPeriod(g, cachesize, subtraction_set, overlap);
    printf("%hu %hu %hu %hu %lu\n", i, j, k, l, period);
    return 0;
}
