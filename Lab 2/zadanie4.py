# Zadanie 4
# Zaimplementuj własny iterator o nazwie fibonacci, zwracający kolejne liczby ciągu Fibonacciego. 
# Funkcja __init__ powinna posiadać parametr o nazwie steps określający liczbę wyrazów ciągu, 
# po których funkcja  __next__  rzuca wyjątek StopIteration


class Fibonacci:
    def __init__(self, steps):
        self.steps = steps      # liczba wyrazów ciągu
        self.current_step = 0   
        self.a, self.b = 0, 1   # pierwsze dwie liczby Fibonacciego

    def __iter__(self):
        """
        Zwraca iterator (self), aby klasa była iterowalna.
        """
        return self

    def __next__(self):
        """
        Zwraca kolejny wyraz ciągu Fibonacciego. Po osiągnięciu limitu kroków rzuca wyjątek StopIteration.
        """
        if self.current_step >= self.steps:
            raise StopIteration
        fib_number = self.a

        self.a, self.b = self.b, self.a + self.b
        self.current_step += 1
        
        return fib_number

fibonacci_iterator = Fibonacci(steps=10)

for num in fibonacci_iterator:
    print(num)


