import time
import ssl
import socket
import json
import pymysql

login=bytes('{"M":"login","ID":"17591","K":"52660fa46d"}\n',encoding="utf-8")
status=bytes('{"M":"isOL","ID":"24113"}\n',encoding="utf-8")
getdata=bytes('{"M":"getdata","ID":"24113"}\n',encoding="utf-8")

s=socket.socket(socket.AF_INET)
sslcon=ssl.wrap_socket(s,ssl_version=ssl.PROTOCOL_SSLv23)
sslcon.connect(('www.bigiot.net',8585))
sslcon.send(login)

while True:
    sslcon.send(getdata)
    message=sslcon.recv(1024).decode('utf-8','replace')
    print(message)
    dic=json.loads(message)
    if(dic['M']=='update'):
        print(dic)

        if '22163' in dic['V']:
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            table = 'tmp'
            keys = 'nowtime,tmp'
            valuesLI=dic['V']['22163']
            sql = "INSERT INTO %s (%s) VALUES (now(),'%s')"%(table,keys,valuesLI)
            print(sql)
            try:
                cursor.execute(sql)
                print('tmp Successful')
                db.commit()
            except:
                print('Failed')
                db.rollback()
            cursor.close()
            db.close()
        if '22113' in dic['V']:
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            table = 'tmp1'
            keys = 'nowtime,tmp'
            valuesLI=dic['V']['22113']
            sql = "INSERT INTO %s (%s) VALUES (now(),'%s')"%(table,keys,valuesLI)
            print(sql)
            try:
                cursor.execute(sql)
                print('tmp1 Successful')
                db.commit()
            except:
                print('Failed')
                db.rollback()
            cursor.close()
            db.close()
        if '22166' in dic['V']:
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            table = 'tmp2'
            keys = 'nowtime,tmp'
            valuesLI=dic['V']['22166']
            sql = "INSERT INTO %s (%s) VALUES (now(),'%s')"%(table,keys,valuesLI)
            print(sql)
            try:
                cursor.execute(sql)
                print('tmp2 Successful')
                db.commit()
            except:
                print('Failed')
                db.rollback()
            cursor.close()
            db.close()
        if '22164' in dic['V']:
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            table = 'hum'
            keys = 'nowtime,hum'
            valuesLI=dic['V']['22164']
            sql = "INSERT INTO %s (%s) VALUES (now(),'%s')"%(table,keys,valuesLI)
            print(sql)
            try:
                cursor.execute(sql)
                print('hum Successful')
                db.commit()
            except:
                print('Failed')
                db.rollback()
            cursor.close()
            db.close()

        if '22165' in dic['V']:
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            table = 'hum2'
            keys = 'nowtime,hum'
            valuesLI=dic['V']['22165']
            sql = "INSERT INTO %s (%s) VALUES (now(),'%s')"%(table,keys,valuesLI)
            print(sql)
            try:
                cursor.execute(sql)
                print('hum1 Successful')
                db.commit()
            except:
                print('Failed')
                db.rollback()
            cursor.close()
            db.close()

        if '21951' in dic['V']:
            db = pymysql.connect(host='localhost',user='root', password='123456', port=3306, db='sensor')
            cursor = db.cursor()
            table = 'hum2'
            keys = 'nowtime,hum'
            valuesLI=dic['V']['22166']
            sql = "INSERT INTO %s (%s) VALUES (now(),'%s')"%(table,keys,valuesLI)
            print(sql)
            try:
                cursor.execute(sql)
                print('hum2 Successful')
                db.commit()
            except:
                print('Failed')
                db.rollback()
            cursor.close()
            db.close()
    time.sleep(5)