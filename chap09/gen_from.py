from collections.abc import Generator

def read_files(*files: str) -> Generator[str]:
    for file in files:
        yield from read_lines(file)

def read_lines(path: str) -> Generator[str]:
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            yield line.rstrip('\n')

for line in read_files(
        './chap09/sample1.dat', './chap09/sample2.dat',
        './chap09/sample3.dat'):
    print(line)
