import mysql_repository
import demjson
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class HtkCrawlPipeline(object):
    def process_item(self, item, spider):
        cursor = mysql_repository.get_mysql_cursor()
        connection = mysql_repository.get_mysql_connection()
        item = format_item(item)
        sql = "INSERT INTO spider(content, href, image_url) VALUE " \
              "('%s', '%s', '%s')" % \
              (item['content'], item['href'], item['image_url'])
        cursor.execute(sql)
        connection.commit()

        result_file = open('result.txt', 'a+')
        result_file.writelines('%s,%s,%s' %
                               (item['content'], item['href'], item['image_url']))
        result_file.close()
        return item


def format_item(item):
    for key in item.keys():
        value = item[key]
        # value = str(value).decode('unicode-escape').encode('utf8')
        item[key] = value
    return item
