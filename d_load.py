"""
Load file
Then return the palindrome words as a list
Returns Error if found

"""
import sys

def load(file):
    try:
        with open(file) as f:
            a = [l.lower() for l in f.read().strip().split('\n')  if len(l)>1]
##            pali = [i.lower() for i in a if i[:]==i[::-1] and len(i)>1]
        
    except:
        print("You did an oopsie, bad you, I'm gonna stop working now because\
                    my creator didn't know what else to do.")
        sys.exit(1)
    return a
