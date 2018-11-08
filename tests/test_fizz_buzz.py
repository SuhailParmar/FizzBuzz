from lib.fizz_buzz import FizzBuzz


class TestFizzBuzz:
    '''
      FizzBuzzSpec
    - Prints the numbers from 1 to 100.
    - But for multiples of three print “Fizz”
    - For the multiples of five print “Buzz”
    - For numbers which are multiples of both three and five print “FizzBuzz”."
    '''
    fb = FizzBuzz()

    def test_is_fizz_returns_true_for_muliples_of_3(self):

        multiples_of_three = [3, 6, 9, 12, 30]
        for value in multiples_of_three:
            assert self.fb.is_fizz(value) is True

    def test_is_fizz_returns_false_for_not_muliples_of_3(self):
        not_multiples_of_three = [1, 2, 7, 11, 29]
        for value in not_multiples_of_three:
            assert self.fb.is_fizz(value) is False

    def test_is_buzz_returns_true_for_muliples_of_5(self):
        multiples_of_five = [5, 10, 15, 35, 50]
        for value in multiples_of_five:
            assert self.fb.is_buzz(value) is True

    def test_is_buzz_returns_false_for_not_muliples_of_5(self):
        not_multiples_of_five = [1, 3, 4, 9, 144]
        for value in not_multiples_of_five:
            assert self.fb.is_buzz(value) is False

    def test_is_fizzbuzz_for_multiples_of_3_5(self):
        multiples_of_three_five = [15, 30, 45, 60, 90]
        for value in multiples_of_three_five:
            assert self.fb.is_fizz_buzz(value) is True

    def test_run_fizz_buzz(self, capsys):
        output = self.fb.run_fizz_buzz(15)
        out = capsys.readouterr()[0]  # Returns Tuple of out, error
        assert out.count('Fizz') == 5  # 4 + 1(FIZZBuzz)
        assert out.count('Buzz') == 3  # 2 + 1 (FizzBUZZ)
        assert out.count('FizzBuzz') == 1
