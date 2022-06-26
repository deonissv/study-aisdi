from n import find_n
from kmp import find_kmp
from rk import find_rk
from random import choice


def test_n_empty_str():
    string = ''
    text = 'asddddaasdssasd'
    assert find_n(string, text) == []


def test_kmp_empty_str():
    string = ''
    text = 'asddddaasdssasd'
    assert find_kmp(string, text) == []


def test_rk_empty_str():
    string = ''
    text = 'asddddaasdssasd'
    assert find_rk(string, text) == []


def test_n_empty_txt():
    string = 'asd'
    text = ''
    assert find_n(string, text) == []


def test_kmp_empty_txt():
    string = 'asd'
    text = ''
    assert find_kmp(string, text) == []


def test_rk_empty_txt():
    string = 'asd'
    text = ''
    assert find_rk(string, text) == []


def test_n_str_eq_to_txt():
    string = 'asd'
    text = 'asd'
    assert find_n(string, text) == [0]


def test_kmp_str_eq_to_txt():
    string = 'asd'
    text = 'asd'
    assert find_kmp(string, text) == [0]


def test_rk_str_eq_to_txt():
    string = 'asd'
    text = 'asd'
    assert find_rk(string, text) == [0]


def test_n_long_str():
    text = 'asd'
    string = 'asddddaasdssasd'
    assert find_n(string, text) == []


def test_kmp_long_str():
    text = 'asd'
    string = 'asddddaasdssasd'
    assert find_kmp(string, text) == []


def test_rk_long_str():
    text = 'asd'
    string = 'asddddaasdssasd'
    assert find_rk(string, text) == []


def test_n_no_match():
    string = 'aaa'
    text = 'asddddaasdssasd'
    assert find_n(string, text) == []


def test_kmp_no_match():
    string = 'aaa'
    text = 'asddddaasdssasd'
    assert find_kmp(string, text) == []


def test_rk_no_match():
    string = 'aaa'
    text = 'asddddaasdssasd'
    assert find_rk(string, text) == []


def test_n():
    text = 'asddddaasdssasd'
    string = 'asd'
    assert find_n(string, text) == [0, 7, 12]
    assert find_rk(string, text) == find_kmp(string, text) == find_n(string, text)
    string = 'ddd'
    assert find_n(string, text) == [2, 3]
    assert find_rk(string, text) == find_kmp(string, text) == find_n(string, text)
    string = 'sa'
    assert find_n(string, text) == [11]
    assert find_rk(string, text) == find_kmp(string, text) == find_n(string, text)
