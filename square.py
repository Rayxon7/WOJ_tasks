def main():
    n = get_number()
    print_square(n)

def get_number():
    while True:
        side = int(input("what is side? "))
        if side > 0:
            return side

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
