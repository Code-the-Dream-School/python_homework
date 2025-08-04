from assignment1 import hello, greet, calc, data_type_conversion, grade, repeat, student_scores, titleize, hangman, pig_latin

def test_hello():
    assert hello() == "Hello!"

def test_greet():
    assert greet("Alice") == "Hello, Alice!"

def test_calc_add():
    assert calc(2, 3, "add") == 5

def test_calc_divide_by_zero():
    assert calc(5, 0, "divide") == "You can't divide by 0!"

def test_data_type_conversion():
    assert data_type_conversion("3.14", "float") == 3.14

def test_grade_A():
    assert grade(95, 92, 97) == "A"

def test_repeat():
    assert repeat("ha", 3) == "hahaha"

def test_student_scores_best():
    assert student_scores("best", Alice=90, Bob=80) == "Alice"

def test_titleize():
    assert titleize("the lord of the rings") == "The Lord of the Rings"

def test_hangman():
    assert hangman("alphabet", "ab") == "a___ab__"

def test_pig_latin():
    assert pig_latin("quiet queen apple") == "ietquay eenquay appleay"
