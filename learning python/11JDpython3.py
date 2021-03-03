"""Ask the user what's on their mind. Then after the user responds, count the number of words in the sentence and print that as an output."""

import string 
import csv 

print("what's on your mind today?")

mind_co = input ()

mind_count = str(len(mind_co.split()))

print("oh nice, you just told me what's on your mind in " + mind_count + " words!")


"""To take this a step further, open a file that is handed to you, count the number of words in there, then print it out."""



