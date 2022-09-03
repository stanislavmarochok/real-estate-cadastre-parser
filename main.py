import xmltojson
import json
import pandas as pd

from _jsonParser import JsonParser
from _argParser import ArgParser


def getFullJsonFromFile(filename):
    with open(filename, "r", encoding='utf8') as html_file:
        try:
            html = html_file.read()
            html_str = str(html)

            from bs4 import BeautifulSoup

            soup = BeautifulSoup(html_str)
            pretty_soup = soup.prettify()

            json_ = xmltojson.parse(pretty_soup)
            loaded_json = json.loads(json_)

            return loaded_json

        except UnicodeDecodeError as e:
            print('error')
            print(e)


def saveDataframeToFile(output_file_full_name, results_dataframe: pd.DataFrame):
    results_dataframe.to_csv(f'{output_file_full_name}.csv')


def getAllFilenames(full_path_to_directory):
    # get all files in directory "fullPathToDirectory" here

    import glob

    path = f'{full_path_to_directory}/*.html'
    files = glob.glob(path)
    return files


def main():
    args = ArgParser.getArgs()
    path = args.path

    if args.all:  # replace with "parser.all"
        filenames = getAllFilenames(path)
    else:
        filenames = [args.path]

    all_results_dataframe = None

    for _filename in filenames:
        print(f'Processing file {_filename}')
        try:
            full_json = getFullJsonFromFile(filename=f'{_filename}')
        except Exception:
            continue
        # saveJsonToFile(filename=f'{filename}.json', _json=full_json)

        parser = JsonParser(full_json)
        parser.runParser()

        results_dataframe = parser.results
        results_dataframe = pd.DataFrame(results_dataframe)
        # save results_dataframe to common excel
        if all_results_dataframe is None:
            all_results_dataframe = results_dataframe
        all_results_dataframe = pd.concat([all_results_dataframe, results_dataframe], ignore_index=True)

    saveDataframeToFile(args.output, all_results_dataframe)


if __name__ == "__main__":
    main()
