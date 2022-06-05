from cmath import pi, sqrt
import getpass
import math


class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        return self.a / self.b

    def square_binomial(self) -> float:
        return self.a**2 + self.b**2

    def pythagorean_rule(self) -> float:
        return (self.a + self.b)**2

    def factorial_sum(self) -> float:
        return math.factorial(int(self.a)) + math.factorial(int(self.b))

    def circle_area(self) -> float:
        if self.b <= 0: #umjesto a<=0
            return 0
        return self.a ** 2 * pi



if __name__ == "__main__":
    print("Login success!")
    a = float(input("A = "))
    b = float(input("B = "))
    ops_manager = OperationsManager(a, b)
    print(ops_manager.perform_division())
    print(ops_manager.square_binomial())
    print(ops_manager.pythagorean_rule())
    print(ops_manager.factorial_sum())
    print(ops_manager.circle_area())

