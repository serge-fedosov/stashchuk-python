from pathlib import Path


Path('files').mkdir(exist_ok=True)

with open('files/first.txt', 'w') as first_file:
    first_file.write('first line\n')
    first_file.write('second line\n')

with open('files/second.txt', 'w') as second_file:
    second_file.write('2 first line\n')
    second_file.write('2 second line\n')

with open('files/first.txt') as first_file:
    print(first_file.read())

with open('files/second.txt') as second_file:
    for line in second_file:
        print(line)

first_file = Path('files/first.txt')
if first_file.exists():
    first_file.unlink()

second_file = Path('files/second.txt')
if second_file.exists():
    second_file.unlink()

dir_file = Path('files')
if dir_file.is_dir():
    try:
        dir_file.rmdir()
    except OSError:
        print('Can not remove directory')
