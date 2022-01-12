from pymysql import connect
from pymysql.cursors import DictCursor
# 연락처에 관련된 로직을 담당하는 파일

db = connect(
    host='finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='admin',
    passwd='Vmfhwprxm!123',
    db='test_phone_book',
    charset='utf8',
    cursorclass=DictCursor
    )
    
cursor = db.cursor()

def add_contact_to_db(params):
    
    sql = f"SELECT* FROM users WHERE user_id= params['user_id']"
    user_result =
    sql = f"INSERT INTO contacts(user_id, name, phone_num, memo) VALUES({params['user_id']}, '{params['name']}', '{params['phone']}', '{params['memo']}')"
    cursor.execute(sql)
    db.commit()
    return {
        'code':200,
        'message':'연락처 등록이 완료되었습니다.'
    }