import assignment1 as a1


def test_hello():
    assert a1.hello() == "Hello!"


def test_greet():
    assert a1.greet("James") == "Hello, James!"


def test_calc():
    assert a1.calc(5, 6) == 30
    assert a1.calc(5, 6, "add") == 11
    assert a1.calc(20, 5, "divide") == 4
    assert a1.calc(14, 2.0, "multiply") == 28.0
    assert a1.calc(12.6, 4.4, "subtract") == 8.2
    assert a1.calc(9, 5, "modulo") == 4
    assert a1.calc(10, 0, "divide") == "You can't divide by 0!"
    assert a1.calc("first", "second", "multiply") == "You can't multiply those values!"


def test_data_type_conversion():
    result = a1.data_type_conversion("110", "int")
    assert type(result).__name__ == "int"
    assert result == 110
    result = a1.data_type_conversion("5.5", "float")
    assert type(result).__name__ == "float"
    assert result == 5.5
    result = a1.data_type_conversion(7, "float")
    assert type(result).__name__ == "float"
    assert result == 7.0
    result = a1.data_type_conversion(91.1, "str")
    assert type(result).__name__ == "str"
    assert result == "91.1"
    assert (
        a1.data_type_conversion("banana", "int")
        == "You can't convert banana into a int."
    )


def test_grade():
    assert a1.grade(75, 85, 95) == "B"
    assert a1.grade("three", "blind", "mice") == "Invalid data was provided."


def test_repeat():
    assert a1.repeat("up,", 4) == "up,up,up,up,"


def test_student_scores():
    assert a1.student_scores("mean", Tom=75, Dick=89, Angela=91) == (75 + 89 + 91) / 3
    assert a1.student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50) == "Angela"


def test_titleize():
    assert a1.titleize("war and peace") == "War and Peace"
    assert a1.titleize("a separate peace") == "A Separate Peace"
    assert a1.titleize("after on") == "After On"


def test_hangman():
    assert a1.hangman("difficulty", "ic") == "_i__ic____"


def test_pig_latin():
    assert a1.pig_latin("apple") == "appleay"
    assert a1.pig_latin("banana") == "ananabay"
    assert a1.pig_latin("cherry") == "errychay"
    assert a1.pig_latin("quiet") == "ietquay"
    assert a1.pig_latin("square") == "aresquay"
    assert a1.pig_latin("the quick brown fox") == "ethay ickquay ownbray oxfay"
