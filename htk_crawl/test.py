# coding=utf-8
import mysql_repository

if __name__ == '__main__':
    cursor = mysql_repository.get_mysql_cursor()
    connection = mysql_repository.get_mysql_connection()
    item = {
        'content': '二手房足迹',
        'href': 'javascript:void(0);',
        'image_url': ''
    }
    sql = "INSERT INTO spider(content, href, image_url) VALUE " \
          "('%s', '%s', '%s')" % \
          (item['content'], item['href'], item['image_url'])
    cursor.execute(sql)
    connection.commit()
