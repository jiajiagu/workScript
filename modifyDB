import pymysql as pymysql
from datetime import datetime, timedelta

dt = datetime(2021, 10, 14, 15, 30, 00)
dt_end = dt + timedelta(hours=2)

def modifyDB(lessontid,n):
    conn = pymysql.connect(host='test.db.xxx.com',port=yyyy, user='xxx', passwd='xxx', db='xxx',charset="utf8")
    cursor = conn.cursor()

    for i in range(0,n):
        tid=lessontid[i]
        startTime = dt + timedelta(days=i)
        startTime = startTime.strftime("%Y-%m-%d %H:%M:%S")
        startTime=str(startTime)
        endTime = dt_end + timedelta(days=i)
        endTime = endTime.strftime("%Y-%m-%d %H:%M:%S")
        endTime = str(endTime)
        try:
            sql_query = "UPDATE t_lesson SET start_time ='"+startTime +"',end_time='"+endTime+"',duration = 120 WHERE tid='"+tid+"'"
            cursor.execute(sql_query)
            conn.commit()
            print(f'{str(tid)}开课时间为{str(startTime)}')
        except Exception as e:
            print("{0}".format(e))
    conn.close()

def main():
    file = open("../information/stuMobileList", 'r', encoding='UTF-8')
    lessontid = []
    for line in file:
        # 将空格作为分隔符将一个字符切割成一个字符数组
        lessontid.extend([str(i) for i in line.split()])
    file.close()
    n=len(lessontid)
    print(lessontid)
    modifyDB(lessontid,n)

main()
