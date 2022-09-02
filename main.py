import xmltojson
import json

from _jsonParser import JsonParser
from _argParser import ArgParser


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


def saveResultsToFile(outputFileFullName, results):
    with open(outputFileFullName, "w") as file:
        json.dump(results, file)


def getAllFilenames(fullPathToDirectory):
    # get all files in directory "fullPathToDirectory" here
    return ["filename1", "filename.2"]


def main():

    # parse arguments here

    args = ArgParser.getArgs()

    path = args.path

    filename = f'{path}/test' # replace with "parser.filename"
    filenames = [filename]

    if args.all: # replace with "parser.all"
        filenames = getAllFilenames(path)

    allResults = []

    for _filename in filenames:
        fullJson = getFullJsonFromFile(filename=f'{_filename}')
        # saveJsonToFile(filename=f'{filename}.json', _json=fullJson)

        parser = JsonParser(fullJson)
        parser.runParser()

        results = parser.results
        print(results)
        # save results to common excel
        allResults = allResults + results

    saveResultsToFile(args.output, allResults)


if __name__ == "__main__":
    main()
