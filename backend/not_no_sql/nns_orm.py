from backend.not_no_sql.exception.NoContentException import NoContentException
from backend.utils.StringUtil import StringUtil


class nns_orm:

    def query(self, string: str):
        """ Calls with SQL to parse. """
        if string is None or len(string.strip()):
            raise NoContentException('Provided query is empty.')
        query_type = self.__check_template(string)
        return query_type

    def __check_template(self, string: str) -> str:
        """ Compares given query with known templates. """
        str_0 = str(string).strip()
        if len(str_0) == 0:
            return "Empty"
        # Fix keywords to upper
        str_0 = StringUtil.replace_with_uppercase(str_0, 'select')
        str_0 = StringUtil.replace_with_uppercase(str_0, 'where')
        str_0 = StringUtil.replace_with_uppercase(str_0, 'from')
        str_0 = StringUtil.replace_with_uppercase(str_0, 'in')
        str_0 = StringUtil.replace_with_uppercase(str_0, 'count')

        cnt_where = str_0.count("WHERE")
        cnt_from = str_0.count("FROM")
        cnt_select = str_0.count("SELECT")
        cnt_in = str_0.count("IN")
        cnt_count = str_0.count("COUNT")

        # If it is a select
        if not str_0.startswith("SELECT "):
            return "NotASelect"
        # It is a select
        if cnt_count == 1 and cnt_select == 1 and cnt_from == 1 and cnt_where == 1:
            return "S2"
        elif cnt_select == 2 and cnt_from == 2 and cnt_where == 2 and cnt_in == 1:
            return "S3"
        elif cnt_select == 1 and cnt_from == 1 and cnt_where == 1:
            return "S4" if cnt_in == 1 else "S1"
        return "UnknownSelect"
