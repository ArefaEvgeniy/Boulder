import json
import os

import constants as const


class InputOutput:

    def __init__(self, file_name):
        self.file_name = file_name
        res = self.load_file()
        self.json_data = self.jsonLoadsSafe(res)


    @staticmethod
    def jsonLoadsSafe(jsonString):
        res = None
        try:
            if jsonString:
                if isinstance(jsonString, str):
                    res = json.loads(jsonString)
                else:
                    res = jsonString
        except Exception as err:
            print("Error pars json: %s;\nsource string: %s"
                  .format(str(err), str(jsonString)))

        return res


    def load_file(self):
        res = ''
        if os.path.exists(self.file_name):
            with open(self.file_name) as file_score:
                for line in file_score:
                    res += line

        return res


    def save_best_score(self, best_score):
        data = {const.JSON_BEST_SCORE: best_score}
        with open(self.file_name, 'w') as file_score:
            file_score.write(str(data).replace("'", '"'))


    def get_best_score(self):
        res = 0
        if self.json_data:
            res = self.json_data.get(const.JSON_BEST_SCORE)
        return res
