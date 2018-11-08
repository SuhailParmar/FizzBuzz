class FizzBuzz:

    def is_fizz(self, integer):
        return (integer % 3 == 0)

    def is_buzz(self, integer):
        return (integer % 5 == 0)

    def is_fizz_buzz(self, integer):
        return (self.is_fizz(integer) and self.is_buzz(integer))

    def run_fizz_buzz(self, max_range):
        for integer in range(1, max_range+1):
            if self.is_fizz_buzz(integer):
                print('FizzBuzz')
            elif self.is_buzz(integer):
                print('Buzz')
            elif self.is_fizz(integer):
                print('Fizz')
            else:
                print(integer)
