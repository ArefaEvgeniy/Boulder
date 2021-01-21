"""
File input_output.py used to work with files.
"""

import json
import os

import constants as const


class InputOutput:
    """
    Used to work with files.
    """
    def __init__(self, file_name):
        self.file_name = file_name
        res = self.load_file()
        self.json_data = self.json_loads_safe(res)


    @staticmethod
    def json_loads_safe(json_string):
        """
        Safe method to read data in json-format.
        :param json_string: input json as string
        :return: json-data as dictionary
        """
        res = None
        try:
            if json_string:
                if isinstance(json_string, str):
                    res = json.loads(json_string)
                else:
                    res = json_string
        except Exception as err:
            print(f"Error pars json: {str(err)};\n"
                  f"source string: {str(json_string)}")

        return res


    def load_file(self):
        """
        Read data from file of statistic.
        :return: read data
        """
        res = ''
        if os.path.exists(self.file_name):
            with open(self.file_name) as file_score:
                for line in file_score:
                    res += line

        return res


    def save_best_score(self, best_score):
        """
        Write best score to file of statistic.
        :param best_score: best score from game
        """
        data = {const.JSON_BEST_SCORE: best_score}
        with open(self.file_name, 'w') as file_score:
            file_score.write(str(data).replace("'", '"'))


    def get_best_score(self):
        """
        Read best score from file of statistic.
        :return: best score to game
        """
        res = 0
        if self.json_data:
            res = self.json_data.get(const.JSON_BEST_SCORE)
        return res
