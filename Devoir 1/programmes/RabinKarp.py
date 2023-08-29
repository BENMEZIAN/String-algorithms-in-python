# Python program for implementation of Rabin-Karp algorithm for string matching
import timeit

mycode='''
# define the prime numbers for the hash functions
primes = [101, 103, 107]

d = 256

def rabin_karp(text, pattern):
    matches = []
    comparisons = 0  # initialize counter for comparisons
    # loop through each prime number
    for q in primes:
        # calculate the hash value of the pattern and first window of text
        m = len(pattern)
        n = len(text)
        h = pow(d, m-1) % q
        p = 0
        t = 0
        for i in range(m):
            p = (d*p + ord(pattern[i])) % q
            t = (d*t + ord(text[i])) % q
        # slide the pattern over text one by one and check hash values
        for i in range(n-m+1):
            comparisons += 1  # increment counter for comparisons
            # check if any of the hash values match
            if p == t:
                # check for characters one by one
                for j in range(m):
                    if text[i+j] != pattern[j]:
                        break
                else:
                    # if the loop above completes without hitting the break statement, it means all characters match
                    matches.append(i)
            # calculate hash value for next window of text
            if i < n-m:
                t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
                
        # if matches are found, return the list of indices
        if matches:
            return matches, comparisons
    # if no matches are found, return an empty list
    return matches, comparisons


text = "AAACABBAAAABBAAABAAABAABB"
pattern1 = "AB"
pattern2 = "AA"
pattern3 = "AAB"

# call the rabin_karp function and print the results
matches, comparisons = rabin_karp(text, pattern1)
print("Matches found at indices:", matches)
print("Number of comparisons:", comparisons)

matches, comparisons = rabin_karp(text, pattern2)
print("Matches found at indices:", matches)
print("Number of comparisons:", comparisons)

matches, comparisons = rabin_karp(text, pattern3)
print("Matches found at indices:", matches)
print("Number of comparisons:", comparisons)
'''

exec_time = timeit.timeit(stmt=mycode,number=1) * 10**3
print(f"The time of execution of above program is : {exec_time:.03f}ms")





