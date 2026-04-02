"""Prime number checker."""

def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def main() -> None:
    try:
        value = int(input("Enter a number: ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if is_prime(value):
        print(f"{value} is prime")
    else:
        print(f"{value} is not prime")


if __name__ == "__main__":
    main()
