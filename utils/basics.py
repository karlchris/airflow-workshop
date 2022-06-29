SQL_PARENT_PATH = "sql/"


def read_sql(table_name):
    with open(SQL_PARENT_PATH + table_name + ".sql") as fl:
        fl_content = fl.read()
    return fl_content
