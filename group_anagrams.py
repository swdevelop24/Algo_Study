# Time complexity: O(w * nlog(n)) where w is the number of words , n is the longest word
# Space complexity: O(wn)
def groupAnagrams(wordlist):
    anagrams = {}
    for word in wordlist:
        curr_word = "".join(sorted(word))
        if curr_word in anagrams:
            anagrams[curr_word].append(word)
        else:
            anagrams[curr_word] = [word]
    return list(anagrams.values())

def main():
    wordlist = ['lump', 'eat',  'me',  'tea', 'em', 'plum']
    print(groupAnagrams(wordlist))

main()

    
