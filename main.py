from backend.KeyValueReader import KeyValueReader  # Used to obtain translations
from backend.not_no_sql.nns_converters import nns_converters
from backend.utils.FileUtil import FileUtil


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Tomasz Trzciński\'s:\nNotNoSQL')
    # result = FileUtil.list_fies('backend/resources', 'lang*.txt')
    # print(result)
    res = nns_converters.conv_json_to_where('{"col_1": "val_1", "col_2": 2}')
    print(res)
