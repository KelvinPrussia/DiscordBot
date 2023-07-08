import sqlite3

def create_table(content):
        conn = sqlite3.connect('kelili_db')
        table_name = content.split()[1]
        columns_list = content.replace(('$addtable ' + table_name + ' - '), '').split('|')
        table_columns = ' text, '.join(columns_list)

        sql_query = ('CREATE TABLE '
                    + table_name
                    + '(' 
                    + table_columns 
                    + ');')

        conn.execute(sql_query)
        print('Executed sql query: \n' + sql_query)
        conn.close()
        return '|'.join(columns_list)

def insert_data(content):
        print('TO DO')

def check_for_table(content):
        conn = sqlite3.connect('kelili_db')
        table_name = content.split()[1]

        sql_query = f"Select count(name) from sqlite_master where type='table' and name='{table_name}'"

        print(sql_query)
        res = conn.execute(sql_query).fetchone()[0]
        conn.close()
        return res