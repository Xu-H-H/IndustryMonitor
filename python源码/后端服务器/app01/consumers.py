from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
import time
import pymysql

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        print("有人连接")
        #接受连接
        self.accept()
        self.send('60')
    def websocket_receive(self, message):
        print(message)
        text=message['text']
        print(text)
        if text=='sendtmp1':
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            sql = "SELECT * FROM tmp1 WHERE id=(SELECT max(id) FROM tmp1);"
            try:
                cursor.execute(sql)
                results=cursor.fetchone()
                print(results[1])
                db.commit()
            except:
                print('Failed')
                db.rollback()
                cursor.close()
            db.close()
            self.send(results[1])
            time.sleep(1)
        if text=='sendtmp2':
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            sql = "SELECT * FROM tmp2 WHERE id=(SELECT max(id) FROM tmp2);"
            try:
                cursor.execute(sql)
                results=cursor.fetchone()
                print(results[1])
                db.commit()
            except:
                print('Failed')
                db.rollback()
                cursor.close()
            db.close()
            self.send(results[1])
            time.sleep(1)
        if text=='sendtmp3':
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            sql = "SELECT * FROM tmp3 WHERE id=(SELECT max(id) FROM tmp3);"
            try:
                cursor.execute(sql)
                results=cursor.fetchone()
                print(results[1])
                db.commit()
            except:
                print('Failed')
                db.rollback()
                cursor.close()
            db.close()
            self.send(results[1])
            time.sleep(1)
        if text=='sendhum1':
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            sql = "SELECT * FROM hum1 WHERE id=(SELECT max(id) FROM hum1);"
            try:
                cursor.execute(sql)
                results=cursor.fetchone()
                print(results[1])
                db.commit()
            except:
                print('Failed')
                db.rollback()
                cursor.close()
            db.close()
            self.send(results[1])
            time.sleep(1)
        if text=='sendhum2':
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            sql = "SELECT * FROM hum2 WHERE id=(SELECT max(id) FROM hum2);"
            try:
                cursor.execute(sql)
                results=cursor.fetchone()
                print(results[1])
                db.commit()
            except:
                print('Failed')
                db.rollback()
                cursor.close()
            db.close()
            self.send(results[1])
            time.sleep(1)
        if text=='sendhum3':
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            sql = "SELECT * FROM hum3 WHERE id=(SELECT max(id) FROM hum3);"
            try:
                cursor.execute(sql)
                results=cursor.fetchone()
                print(results[1])
                db.commit()
            except:
                print('Failed')
                db.rollback()
                cursor.close()
            db.close()
            self.send(results[1])
            time.sleep(1)
    def websocket_disconnect(self, message):
        print("连接断开")
        raise StopConsumer()
