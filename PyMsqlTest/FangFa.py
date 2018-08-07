import pymysql
from testcase.pub import PubTest


class TestMysql(object):

    conn = pymysql.connect(host="sit5home.uuabc.com",
                           user="wufenfen",
                           password="wufenfen",
                           db="uuabc",
                           port=3306,
                           charset="utf8"
                           )
    # conn = pymysql.connect(host="newhome.uuabc.com",
    #                        user="wufenfen",
    #                        password="wufenfen",
    #                        db="uuabc",
    #                        port=3306,
    #                        charset='utf8'
    #                        )

    """
    CourseRankList接口查询用户最近一节课，获得钻石不为0
    """

    cursor = conn.cursor()
    cur = conn.cursor()
    cursor.execute("select max(class_appoint_course_id) from course_details WHERE student_id = 1952 and harvest !=0")
    re_dock = cursor.fetchall()
    cursor.close()

    """
    PadLiveReserve接口查询最近一节课用户是否预约
    """

    cursor = conn.cursor()
    cur1 = conn.cursor()
    cursor.execute("select max(id) from live_course WHERE status=1 ")
    cur.execute("select max(live_id) from live_reserve WHERE disabled =0 ")
    dock = cursor.fetchall()
    dock2 = cur.fetchall()
    for raw in dock:
        for row in dock2:
            if raw != row:
                cursor.execute("select max(id) from live_course WHERE status=1 ")
            else:
                # cur.execute("delete from live_reserve where student_id=1952 ORDER BY update_at DESC limit 1")
                pass

    cur.close()
    cursor.close()
    conn.close()

    data2 = {
        'liveId': raw[0],
        'token': PubTest.ld['token'],
    }
    print(raw[0])
