from calculator import multiply

def test_multiply():
    assert multiply(10, 5) == 50
    assert multiply(-3, 4) == -12
    assert multiply(0, 100) == 0
    assert multiply(2.5, 4) == 10.0


if __name__ == "__main__":
    test_multiply()
    print("All tests passed!")
