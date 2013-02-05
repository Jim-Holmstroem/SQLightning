
import sqlite3 as sql

import collections as c



class Database(c.Mapping):

    class Adapter(c.Callable):
        """
        ABC for the Adapters
        """
        def get_sql_type(self):
            return self.__sql_type


    class IntegerAdapter(Adapter):
        __sql_type = "INT"
        __python_type = int

    class StringAdapter(Adapter):
        """
        Variable-length string
        """
        __sql_type = "TEXT"
        __python_type = str

    class FloatAdapter(Adapter):
        """
        Double precision: IEEE754
        """
        __sql_type = "FLOAT(53)"
        __python_type = float




    "({types})".format(types=",".join(map(..,rows)))



    def __init__(self, filename):
        self.filename = filename

    def __getitem__(self, table_name):
        pass

    def __delitem__(self, table_name):
        raise NotImplementedError()

    def __setitem__(self, table_name):
        raise NotImplementedError()

    def __len__(self):
        #"SELECT COUNT(*) FROM information_schema.tables WHERE table_type = 'base table'"
        raise NotImplementedError()

class Table(object):
    def __init__(self):
        pass


