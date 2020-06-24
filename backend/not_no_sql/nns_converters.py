from backend.utils.StringUtil import StringUtil
import json


class nns_converters:
    """ Converters to be used in translations between SQL and JSON. """

    @staticmethod
    def is_valid_json(params: str) -> bool:
        """ Checks, if given string is a valid JSON. """
        if StringUtil.is_none(params) or params.strip() == '{}':
            return False
        try:
            json_object = json.loads(params)
        except ValueError as e:
            return False
        return True

    @staticmethod
    def conv_json_to_where(params: str) -> str:
        """ Converts JSON to SQL SELECT's WHERE clause. """
        if params is not None and len(params.strip()) == 0:
            return "1 = 1"
        if not nns_converters.is_valid_json(params):
            return None
        result = ''
        parsed = json.loads(params)
        for key in parsed:
            print(key, ":", parsed[key])
            if StringUtil.has_content(result):
                result += ' AND '
            if str(parsed[key]).isnumeric():
                result += key + ' = ' + str(parsed[key])
            else:
                result += key + ' LIKE \'' + parsed[key] + '\''
        return result
