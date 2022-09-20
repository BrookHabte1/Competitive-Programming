class Solution:
    def fizzBuzz(self, m: int) -> List[str]:
        def f(n):
            if n%3==0 and n%5==0:
                return "FizzBuzz"
            elif n%3==0:
                return "Fizz"
            elif n%5 ==0:
                return "Buzz"
            else:
                return str(n)
        return [f(n) for n in range(1,m+1)]
        