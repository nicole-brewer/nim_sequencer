#include<stdio.h>
int main()
{
    unsigned int uint = 0 - 1;
    unsigned long ulong = 0 - 1;
    unsigned long long ull = 0 - 1;
    unsigned short ushort = 0 - 1;
    // Sizeof operator is used to evaluate the size of a variable
    printf("Sizeof unsigned short: %d bytes\n", sizeof(unsigned short));
    printf("Largest unsigned short: %hu\n", ushort);
    printf("Size of unsigned int: %u bytes\n",sizeof(unsigned int));
    printf("Largest unsigned int: %u\n", uint);
    printf("Size of unsigned long: %lu bytes\n",sizeof(unsigned long));
    printf("Largest unsigned long: %lu\n", ulong);
    printf("Size of unsigned long long: %llu bytes\n",sizeof(unsigned long long));
    printf("Largest unsigned long long: %llu\n",ull);
    return 0;
}
