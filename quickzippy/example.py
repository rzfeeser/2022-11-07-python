
def example():
    root = '/home/student/'
    dirs = ['mycode', 'px', 'static', '.ssh']
    files = ['.python_history', 'zork.test', 'example.py'] # and so on
    return root, dirs, files # returning 3 items (3-tuple)

def main():
    root, dirs, files = example()

    print(root + files[0])
    print(root + files[1])
    print(root + files[2])

    for file in files:
        print(root + file)


if __name__ == "__main__":
    main()
