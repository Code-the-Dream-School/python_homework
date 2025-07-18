import assignment1

# Task 1
def test_hello():
    assert assignment1.hello() == "Hello!"

# Task 2
def test_greet():
    assert assignment1.greet("Gedam") == "Hello, Gedam!"

# Task 3
def test_calc():
    assert assignment1.calc(4, 2, "add") == 6
    assert assignment1.calc(4, 2, "subtract") == 2
    assert assignment1.calc(4, 2) == 8  # default multiply
    assert assignment1.calc(4, 2, "divide") == 2
    assert assignment1.calc(4, 0, "divide") == "You can't divide by 0!"
    assert assignment1.calc("a", "b", "multiply") == "You can't multiply those values!"

# Task 4
def test_data_type_conversion():
    assert assignment1.data_type_conversion("123", "int") == 123
    assert assignment1.data_type_conversion("123.45", "float") == 123.45
    assert assignment1.data_type_conversion(123, "str") == "123"
    result = assignment1.data_type_conversion("nonsense", "float")
    assert result == "You can't convert nonsense into a float."

# Task 5
def test_grade():
    assert assignment1.grade(90, 95, 100) == "A"
    assert assignment1.grade(85, 80, 89) == "B"
    assert assignment1.grade(75, 70, 79) == "C"
    assert assignment1.grade(65, 60, 69) == "D"
    assert assignment1.grade(50, 55, 59) == "F"
    assert assignment1.grade("a", "b") == "Invalid data was provided."

# Task 6
def test_repeat():
    assert assignment1.repeat("Go!", 3) == "Go!Go!Go!"
    assert assignment1.repeat("Hi", 0) == ""

# Task 7
def test_student_scores():
    scores = {"Alice": 90, "Bob": 80, "Carol": 85}
    assert assignment1.student_scores("best", **scores) == "Alice"
    assert assignment1.student_scores("mean", **scores) == 85
    assert assignment1.student_scores("worst", **scores) is None

# Task 8
def test_titleize():
    text = "a tale of two cities"
    expected = "A Tale of Two Cities"
    assert assignment1.titleize(text) == expected

# Task 9
def test_hangman():
    secret = "alphabet"
    guess = "ab"
    expected = "a___ab__"
    assert assignment1.hangman(secret, guess) == expected

# Task 10
def test_pig_latin():
    text1 = "apple"
    text2 = "quiet banana"
    assert assignment1.pig_latin(text1) == "appleay"
    assert assignment1.pig_latin(text2) == "ietquay ananabay"
