def anagram_check(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False


word1 = "keep"
word2 = "peek"
word3 = "clock"

# Anagrams
print(anagram_check(word1, word2))

# Not anagrams
print(anagram_check(word1, word3))
