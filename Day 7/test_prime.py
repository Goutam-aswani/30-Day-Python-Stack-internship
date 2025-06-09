import unittest
import prime


class Testprime(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(prime.is__prime(1), False)
        self.assertEqual(prime.is__prime(2), True)
        self.assertEqual(prime.is__prime(11), True)
        self.assertEqual(prime.is__prime(25), False)


if __name__ == "__main__":
    unittest.main()
