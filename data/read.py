from os import popen

def read_data() :
    return popen("ls")