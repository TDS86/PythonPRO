import json


class Iterator:
    def __iter__(self):
        with open('countries.json') as f:
            self.country_list = [country['name']['official'] for country in json.loads(f.read())]
        return self

    def __next__(self):
        if not self.country_list:
            raise StopIteration
        country_name = self.country_list.pop()
        return f'{country_name} - https://en.wikipedia.org/wiki/{country_name.replace(" ", "_")}'


if __name__ == '__main__':
    with open('country_links.txt', 'w') as f:
        for i in Iterator():
            f.write(i+'\n')