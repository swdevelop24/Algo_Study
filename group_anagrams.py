def groupAnagrams(wordlist):
    # Write your code here.
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

    
