#include <stdio.h>
#include <stdlib.h>

char nextLine(FILE* fp);

int main(void)
{
    FILE* fp = fopen("s2.in", "r");
    if (fp == NULL) return 1;
    
    int lines;
    fscanf(fp, "%d", &lines);

    char answers[lines];
    char key[lines];
    
    for (int i = 0; i < lines; i++)
        answers[i] = nextLine(fp);
        
    for (int i = 0; i < lines; i++)
        key[i] = nextLine(fp);
    
    int right = 0;
    for (int i = 0; i < lines; i++)
        if (answers[i] == key[i]) right++;
        
    printf("%d\n", right);
    
    fclose(fp);
}

char nextLine(FILE* fp)
{
    fseek(fp, SEEK_CUR, 1);
    return fgetc(fp);
}