#include <stdio.h>

int romanToInt(char* s) {
    int result = 0;
    while (*s) {
        if (*s == 'I') {
            if (*(s + 1) == 'V' || *(s + 1) == 'X') result -= 1;
            else result += 1;
        } else if (*s == 'V') {
            result += 5;
        } else if (*s == 'X') {
            if (*(s + 1) == 'L' || *(s + 1) == 'C') result -= 10;
            else result += 10;
        } else if (*s == 'L') {
            result += 50;
        } else if (*s == 'C') {
            if (*(s + 1) == 'D' || *(s + 1) == 'M') result -= 100;
            else result += 100;
        } else if (*s == 'D') {
            result += 500;
        } else if (*s == 'M') {
            result += 1000;
        }
        s++;
    }
    return result;
}
