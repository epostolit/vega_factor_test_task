import typing as tp

from dataclasses import dataclass

@dataclass
class NumbersStep:
    m: int
    n: int

    def next(self) -> int:
        return self.m ** 2 + self.n ** 2 + 1


@dataclass
class NumbersPath:
    a: int
    b: int
    steps: tp.Tuple[
        tp.List[NumbersStep], # steps for a
        tp.List[NumbersStep] # steps for b
    ]
    
    @staticmethod
    def sum(m: int, n: int) -> int:
        return m + n
    
    @staticmethod
    def sq_sum1(m: int, n: int) -> int:
        return m ** 2 + n ** 2 + 1


class Checker:
    def __init__(self, max_n: int) -> None:
        """
        Class to check hypothesis
        Args:
            max_n (int): N from the task description
        """
        self.N = max_n


    def run_check(self) -> None:
        pass


    def get_path(self, a: int, b: int) -> NumbersPath:
        raise NotImplementedError

