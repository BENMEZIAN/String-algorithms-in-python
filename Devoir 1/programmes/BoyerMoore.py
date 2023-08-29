# Python program for implementation of BoyerMoore algorithm for string matching
import timeit

mycode = '''
NO_OF_CHARS = 256

def badCharHeuristic(string, size):

    # Initialize all occurrence as -1
    badChar = [-1]*NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i
    
    return badChar

def search(txt, pat):

    m = len(pat)
    n = len(txt)

    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)

    # s is shift of the pattern with respect to text
    s = 0
    comparisons = 0
    while(s <= n-m):
        j = m-1
        # Keep reducing index j of pattern while characters of pattern and text are matching
        # at this shift s
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
            comparisons += 1

        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j<0:
            print("Pattern occur at shift = {}".format(s))
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badChar[ord(txt[s+j])])
            comparisons += 1
    
    return comparisons

# Driver program to test above function
text = "Walking along the beach, feeling the sand between my toes and listening to the waves crashing on the shore - this is my happy place."
pattern = "place"

comparisons = search(text, pattern)
print("Number of comparisons: ", comparisons)
'''

exec_time = timeit.timeit(stmt=mycode,number=1) * 10**3
print(f"The time of execution of above program is : {exec_time:.03f}ms")
