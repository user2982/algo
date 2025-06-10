PROCEDURE: 
The Naive Pattern Searching algorithm involves iterating through the text and checking if the pattern 
matches at each position. If a match is found, we record the position or print it. 
 
1. Start from the first character of the text and iterate through each character. 
2. For each position, compare the characters of the pattern with the characters in the text, starting from 
that position. 
3. If a match is found, print or record the position of the match. 
4. Continue the process until the end of the text is reached. 
----------------------------------------------------------------------------------------------------------
PROGRAM:
def naive_pattern_search(text, pattern): 
    text_length = len(text) 
    pattern_length = len(pattern) 
    occurrences = [] 
    for i in range(text_length - pattern_length + 1): 
        match = True 
        for j in range(pattern_length): 
            if text[i + j] != pattern[j]: 
                match = False 
                break 
        if match: 
            occurrences.append(i) 
    return occurrences 

text_input = "ABABCABABABCABABAB" 
pattern_input = "ABAB" 
result = naive_pattern_search(text_input, pattern_input) 
print(f"Text: {text_input}") 
print(f"Pattern: {pattern_input}") 
print(f"Occurrences found at positions: {result}") 
