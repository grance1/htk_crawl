import MySQLdb

cursor = None
connection = None


def get_mysql_cursor():
    global cursor
    if cursor is not None:
        return cursor
    cursor = get_mysql_connection().cursor()
    return cursor


def get_mysql_connection():
    global connection
    if connection is not None:
        return connection
    connection = MySQLdb.connect(host='localhost', db='spider',
                                 user='root', passwd='123',
                                 charset='utf8')
    return connection

