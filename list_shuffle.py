import random
import json

def read_file(filename):
    """
    A function that reads a json file

    Parameters: filename
    Return: file's content

    """
    with open(filename, "r") as infile:
        return json.load(infile)

def write_file(filename, content):
    """
    A function that writes a json file

    Parameters: filename and content
    Return: none

    """
    with open(filename, "w") as outfile:
        json.dump(content, outfile)

def main(): 
    data = read_file("ex2.2.json")
    
    for i in data:
        random.shuffle(i)

    write_file("ex2.5.json", data)

if __name__ == "__main__":
    main()
