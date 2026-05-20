from hw1.hw1_1 import anagram_1_solution, create_dictionary, find_anagrams

dictionary = create_dictionary()
def test_anagram_1():
    query = ["ely", "eyl", "yel", "lye", "ley", "yle"]
    expected_output = {
        "ely": ["ely", "ley", "lye"],
        "eyl": ["ely", "ley", "lye"]    ,
        "yel": ["ely", "ley", "lye"],
        "lye": ["ely", "ley", "lye"],
        "ley": ["ely", "ley", "lye"],
        "yle": ["ely", "ley", "lye"]
    }
    assert anagram_1_solution(query, dictionary) == expected_output

def test_anagram_2():
    query = []
    expected_output = {
    }
    assert anagram_1_solution(query, dictionary) == expected_output

def test_anagram_3():
    query = ["cdz"]
    expected_output = {
        "cdz": []
    }
    assert anagram_1_solution(query, dictionary) == expected_output

def test_anagram_4():
    query = ["cdz", "stuouslypum", "tlostoy"]
    expected_output = {
        "cdz": [],
        "stuouslypum": ["sumptuously"],
        "tlostoy": ["tolstoy"]
    }
    assert anagram_1_solution(query, dictionary) == expected_output