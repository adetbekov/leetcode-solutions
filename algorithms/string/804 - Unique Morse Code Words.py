"""
Author:  Adetbekov
Problem: 804. Unique Morse Code Words
Link:    https://leetcode.com/problems/unique-morse-code-words/description/
"""


class Solution:
    morse_codes = [".-","-...","-.-.","-..",".","..-.",
                   "--.","....","..",".---","-.-",".-..",
                   "--","-.","---",".--.","--.-",".-.",
                   "...","-","..-","...-",".--","-..-",
                   "-.--","--.."]
    morse_dict = dict(zip(string.ascii_lowercase, morse_codes))
    
    def toMorse(self, word):
        return "".join(map(self.morse_dict.get, word))
    
    def uniqueMorseRepresentations(self, words):
        return len(set(map(self.toMorse, words)))