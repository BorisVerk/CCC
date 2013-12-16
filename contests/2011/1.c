#include <stdio.h>


int main(void)
{
    int numTs = 0, numJs = 0;
    
    FILE * fp = fopen("s1.in", "r");
    if (fp == NULL) return 1;
    
    //what's the point of reading lines?
    for (char k = fgetc(fp); k != EOF; k = fgetc(fp)){
        if (k == 't' || k == 'T')
            numTs++;
        if (k == 'j' || k == 'J') 
            numJs++;
    }
    
    if (numTs <= numJs) printf("French\n");    
    else printf("English\n");
    
    fclose(fp);
}