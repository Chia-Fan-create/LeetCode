class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def is_integer_num(n):
            if isinstance(n, int):
                return True
            if isinstance(n, float):
                return n.is_integer()
            return False
        List = []
        for i in range(1, n+1):
            # print(isinstance(i/3, int))
            if is_integer_num(i/15) == True:
                List.append('FizzBuzz')
            elif is_integer_num(i/5) == True:
                List.append('Buzz')
            elif is_integer_num(i/3) == True:
                List.append('Fizz')
            else:
                List.append(str(i))
        return List