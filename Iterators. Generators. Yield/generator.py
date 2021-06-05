import hashlib


def generator(file_name):
    with open(file_name) as f:
        for string1 in f:
            yield hashlib.md5(string1.encode()).hexdigest()


if __name__ == '__main__':
    for string2 in generator('country_links.txt'):
        print(string2)