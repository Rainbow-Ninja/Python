def get_count(input_str):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        num_vowels += input_str.count(vowel)
    return num_vowels

print(get_count("Hello, my name is Jo"))