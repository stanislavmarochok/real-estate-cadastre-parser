import argparse


class ArgParser:
    @staticmethod
    def getArgs():
        parser = argparse.ArgumentParser(description="Specify details of parsing.")
        parser.add_argument('--all', dest='all', action='store_true', default=False, help='Specify this argument if '
                                                                                          'you want to parse all the '
                                                                                          'files in a folder.')
        parser.add_argument('--path', type=str, dest='path', action='store', default='./', help='Specify full path to '
                                                                                                'the file that you '
                                                                                                'want to process (if '
                                                                                                'you want to process '
                                                                                                'one file), '
                                                                                                'or full path to a '
                                                                                                'directory (if you '
                                                                                                'choose to process '
                                                                                                'all the files in the '
                                                                                                'directory)')
        parser.add_argument('--output', type=str, dest='output', action='store', default='./output', help='Specify '
                                                                                                          'the name '
                                                                                                          'of the '
                                                                                                          'output '
                                                                                                          'file ('
                                                                                                          'where all '
                                                                                                          'the parsed '
                                                                                                          'data will '
                                                                                                          'be saved). '
                                                                                                          'Please '
                                                                                                          'specify '
                                                                                                          'filenam '
                                                                                                          'with .csv '
                                                                                                          'extension '
                                                                                                          '(for '
                                                                                                          'example, '
                                                                                                          '"--output '
                                                                                                          '"C://cadastre_realty/output.csv""),')
        args = parser.parse_args()
        return args

