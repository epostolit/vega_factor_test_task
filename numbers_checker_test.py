from numbers_checker import *


def test_23():
    a = 2
    b = 3
    checker = Checker(3)
    checker.run_check()

    correct_path = NumbersPath(
        a, b,
        (
           [NumbersStep(1, 1)],
           []
        )
    )

    path = checker.get_path(a, b)
    assert path == correct_path

def test_correct_path():
    N = 10
    checker = Checker(N)
    checker.run_check()

    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            path = checker.get_path(a, b)
            assert path.a == a
            assert path.b == b

            cur_a, cur_b = a, b
            for numbers_step in path.steps[0]: # check a
                assert numbers_step.m + numbers_step.n == cur_a
                cur_a  = numbers_step.next()

            for numbers_step in path.steps[1]: # check b
                assert numbers_step.m + numbers_step.n == cur_b
                cur_b = numbers_step.next()

            assert cur_a == cur_b