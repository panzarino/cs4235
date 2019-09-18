#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/*
 * a toy program for learning stack buffer
 * overflow exploiting
 * It reads a list of hex data from the
 * specified file, and performs bubble sorting
 */

#define SORT_ME 1 //Comment this out and recompile if you do not want the function to sort your values.

long n = 0, c = 0, d = 0, v = 0;

FILE *fp = NULL;

void SortData()
{
  long swap = 0;
  long array[17];

  // loading data to array
  printf("Source list:\n");
  char line[sizeof(long) * 2 + 1] = {0};
  while(fgets(line, sizeof(line), fp)) {
    if (strlen((char *)line) > 1) {
      sscanf(line, "%lx", &(array[n]));
      printf("0x%lx\n", array[n]);
      ++n;
    }
  }
  fclose(fp);
 
#ifdef SORT_ME   
  for (c = 0; c < (n - 1); c++) 
  { 
    v = c; 
    for (d = ( c + 1 ); d < n; d++) 
    {
      if (array[d] < array[v]) 
      {
        // Swap the found minimum element with the first element 
        swap       = array[d];
        array[d]   = array[v];
        array[v]   = swap;
      }
    }
  }
#endif 

  // output sorting result
  printf("\nSorted list in ascending order:\n");
  for ( c = 0 ; c < n ; c++ )
     printf("%lx\n", array[c]);
 
}

int main(int argc, char **argv)
{
    if(argc!=2)
    {
        printf("Usage: ./sort file_name\n");
        return -1;
    }

    // From http://stackoverflow.com/questions/5141960/get-the-current-time-in-c
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    printf("Current local time and date: %s\n\n", asctime(timeinfo));
    
    fp = fopen(argv[1], "rb");
    SortData();

    return 0;
}
