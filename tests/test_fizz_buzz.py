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

