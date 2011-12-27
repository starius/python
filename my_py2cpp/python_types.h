
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

#include <list.h>
#include <map.h>
#include <string>
#include <iostream>

#typedef unsigned char byte

const PY_INT = 0;
const PY_STRING = 1;
const PY_LIST = 2;
const PY_DICT = 3;


class python_data
{
    byte type;
    byte* value;
    
    void =operator(int x)
    {
        type = PY_INT;
        value = (int*) x;
    }
    void =operator(string x)
    {
        type = PY_STRING;
        value = x;
    }
}

p = new python_data;

p = 3;
p = "123";




