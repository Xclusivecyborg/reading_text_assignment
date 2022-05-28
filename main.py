# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as file:
       texts = file.read()
    return texts



def count_words():
    text = read_file_content("story.txt")

    # [assignment] Add your code here
    data_into_list = text.split(" ")

    
    professorCount = data_into_list.count("professor")
    asCount = data_into_list.count("as")
    glassCount = data_into_list.count("glass")
    timeCount = data_into_list.count("time")

    maptoReturn = {"professor": professorCount, "time": timeCount, "glass": glassCount, "as": asCount, }
 
    return maptoReturn

count_words()