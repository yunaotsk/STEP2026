PATH_TO_WORDS = 'anagram/words.txt'
def create_dictionary():
    dict = []
    with open(PATH_TO_WORDS, 'r') as f:
        words = f.read().splitlines()
    for word in words:
        dict.append(("".join(sorted(word)), word))
    sorted_dict = sorted(dict)
    return sorted_dict

def find_anagrams(random_word, dictionary):
    anagrams = []
    sorted_random_word = "".join(sorted(random_word))
    a, b = 0, len(dictionary) - 1
    while a <= b:
        mid = (a + b) // 2
        if dictionary[mid][0] == sorted_random_word:
            anagrams.append(dictionary[mid][1])
            i = mid + 1
            while i < len(dictionary) and dictionary[i][0] == sorted_random_word:
                anagrams.append(dictionary[i][1])
                i += 1
            j = mid - 1
            while j >= 0 and dictionary[j][0] == sorted_random_word:
                anagrams.append(dictionary[j][1])
                j -= 1
            break
        elif dictionary[mid][0] < sorted_random_word:
            a = mid + 1
        else:
            b = mid - 1
    return anagrams

def anagram_1_solution(query, dictionary):
    res = {}
    for random_word in query:
        anagrams = find_anagrams(random_word, dictionary)
        res[random_word] = anagrams
    return res
