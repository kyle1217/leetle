import sys

def solve(a, b):
    addend_1 = int(a, 2)
    addend_2 = int(b, 2)

    sum = addend_1 + addend_2
    return format(sum, 'b')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python leetle.py <addend_1> <addend_2>")
        sys.exit(1)

    a = sys.argv[1]
    b = sys.argv[2]
    print(solve(a, b))