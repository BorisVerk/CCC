#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool inSmallGrid(int x, int y);

//bool smallGrid[5][5];

int main(void)
{
    FILE* fp = fopen("s3.in", "r");
    if (fp == NULL) return 1;
    
    int cases;
    fscanf(fp, "%d", &cases);    
    
    for (int i = 0; i < cases; i++) {
        int m, x, y;
        fscanf(fp, "%d %d %d", &m, &x, &y);
        
        while (m > 1){
            m--;
            
            
        }
                
    }
    
    
    fclose(fp);
}

bool inSmallGrid(int x, int y)
{
    return true;
}