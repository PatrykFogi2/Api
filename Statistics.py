import requests
from bs4 import BeautifulSoup as soup
from collections import Counter


def char_count(txt: str) -> dict:
    return Counter(c for c in txt.lower() if c.isalnum())


def letter_count(txt: str) -> dict:
    return Counter(c for c in txt.lower() if c.isalpha())


def number_count(txt: str) -> int:
    numbers_count = 0
    for char in txt:
        if char.isnumeric():
            numbers_count += 1
    return numbers_count


def count_vovels(txt: str) -> int:
    vovels = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']
    vovels_count = 0
    for char in txt:
        if char.lower() in vovels:
            vovels_count += 1
    return vovels_count


def get_information(url: str) -> dict:

    response = requests.get(url)

    words_count = 0
    dictionary_letter_count = dict()
    vovels_count = 0
    numbers_count = 0
    https = 0
    a_1 = 0
    p_1 = 0
    html_txt = soup(response.text, 'html.parser')
    for a in html_txt.find_all("a"):
        a_1 += 1
        text_a = a.text
        if a.get('href'):
            https += 1
        words_count += len(text_a.split(' '))
        vovels_count += count_vovels(text_a)
        numbers_count += number_count(text_a)
        dictionary_letter_count = letter_count(text_a)

    for p in html_txt.find_all("p"):
        p_1 += 1
        text_p = p.text
        words_count += len(text_p.split(' '))
        vovels_count += count_vovels(text_p)
        numbers_count += number_count(text_p)
        dictionary_letter_count += letter_count(text_p)
    most_frequency_letter = max(dictionary_letter_count.values())

    return { 'a sign': a_1,
             'p sign': p_1,
             'words': words_count,
             'vovels': vovels_count,
             'most frequency letter': max(dictionary_letter_count, key=dictionary_letter_count.get),
             'count_most_letter': most_frequency_letter,
             'https count': https,
             'numbers count': numbers_count
             }


