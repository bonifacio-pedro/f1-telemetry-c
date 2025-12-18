#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 512
#define SIZE_CSV 615
#define CRESCENT_SPEED_MOMENTUM 20

void readAndWriteDoubleArrays(double *speed, double *relDist, double *throttle, int *brake, int choose) {
    FILE *file;
    if (choose)
        file = fopen("telemetry_VER_brazil_2024.csv", "r");
    else
        file = fopen("telemetry_HAM_brazil_2024.csv", "r");
    char line[MAX_LINE];

    if (file == NULL) {
        fprintf(stderr, "ERROR! CSV FILE NOT FOUNDED\n");
        exit(1);
    }

    fgets(line, MAX_LINE, file);
    while (fgets(line, MAX_LINE, file)) {
        char *token;
        int col = 0;

        token = strtok(line, ",");

        while (token) {
            switch (col) {
                case 4:   // Speed
                    *speed = atof(token);
                    break;
                case 6:   // Throttle
                    *throttle = atof(token);
                    break;
                case 7:   // Brake
                    if (strcmp(token, "True") == 0) {
                        *brake = 1;
                    } else {
                        *brake = 0;
                    }
                    break;
                case 11:  // RelativeDistance
                    *relDist = atof(token);
                    break;
            }

            token = strtok(NULL, ",");
            col++;
        }
        
        speed++;
        relDist++;
        throttle++;
        brake++;
    }

    fclose(file);
}

int verifyCrescentVel(double *speed, int idx) {
    if (idx + CRESCENT_SPEED_MOMENTUM < SIZE_CSV) {
        double vNow = *(speed+idx);
        double vFuture = *(speed + idx + CRESCENT_SPEED_MOMENTUM);

        if ((vFuture - vNow) > 5.0)
            return 1;
    }
    return 0;
}

const char* getStateName(double *speed, double *relDist, double *throttle, 
                         int *brake, int idx) {
     if (*(brake+idx) == 1 ||
            (*(throttle+idx) < 20 && *(speed+idx) < 250))
        return "IN A CURVE";
    else if (*(brake+idx) == 0 && *(throttle+idx) <= 95 && verifyCrescentVel(speed, idx))
        return "COMING OUT THE CURVE"; 
    else if (*(throttle+idx) <= 98 && *(throttle+idx) > 95)  
        return "ON A STRAIGHT LINE (SHORT)";
    return "ON A STRAIGHT LINE (MEDIUM-LONG)";
}

void exportAndPrintAnalysisToCSV(double *speed, double *relDist, double *throttle, 
                         int *brake) {
    FILE *output = fopen("analysis_output.csv", "w");

    if (output == NULL) {
        fprintf(stderr, "ERROR CREATING OUTPUT FILE!\n");
        return;
    }
    
    
    fprintf(output, "RelativeDistance,State,Speed,Throttle,Brake\n");
    
    for (int i = 0; i < SIZE_CSV; i++) {
        fprintf(output, "%.6f,%s,%.2f,%.2f,%d\n",
                relDist[i],
                getStateName(speed, relDist, throttle, brake, i),
                speed[i],
                throttle[i],
                brake[i]);
        printf("IN POSITION: %.4f -> SPEED: %.4f; THROTTLE: %.4f; BRAKE: %d\n", relDist[i], speed[i], throttle[i], brake[i]);
    }
    
    fclose(output);
}

int main() {
    printf("========================================\n");
    printf("  F1 TELEMETRY ANALYSIS - BRASIL VER (2024)  \n");
    printf("========================================\n\n");

    double speed[SIZE_CSV], relDist[SIZE_CSV], throttle[SIZE_CSV];
    int brake[SIZE_CSV];

    int choose = 0;
    printf("Do you want to export VER or HAM curve analyses? (1/0)\n");
    scanf("%d", &choose);

    readAndWriteDoubleArrays(speed, relDist, throttle, brake, choose);
    exportAndPrintAnalysisToCSV(speed, relDist, throttle, brake);

    return 0;
}