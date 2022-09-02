import xmltojson
import json

from _parser import Parser


def getFullJsonFromFile(filename):
    with open(filename, "r", encoding='utf8') as html_file:
        try:
            html = html_file.read()
            html_str = str(html)

            from bs4 import BeautifulSoup

            soup = BeautifulSoup(html_str)
            prettySoup = soup.prettify()

            json_ = xmltojson.parse(prettySoup)
            loadedJson = json.loads(json_)

            return loadedJson

        except UnicodeDecodeError as e:
            print('error')
            print(e)


def saveJsonToFile(filename, _json):
    with open(filename, "w") as file:
        json.dump(_json, file)


def main():
    filename = 'test'

    fullJson = getFullJsonFromFile(filename=f'{filename}.html')
    # saveJsonToFile(filename=f'{filename}.json', _json=fullJson)

    parser = Parser(fullJson)
    parser.runParser()

    results = parser.results
    print(results)


if __name__ == "__main__":
    main()
