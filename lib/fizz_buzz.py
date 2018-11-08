class FizzBuzz:

    def is_fizz(self, integer):
        return (integer % 3 == 0)

    def is_buzz(self, integer):
        return (integer % 5 == 0)

    def is_fizz_buzz(self, integer):
        return (self.is_fizz(integer) and self.is_buzz(integer))
