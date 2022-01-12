from pymysql import connect
from pymysql.cursors import DictCursor

# 연락처에 관련된 로직을 담당하는 파일
# db 연결 / cursor 변수
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
    
    # 사전 검사 : user_id 파라미터의 값이 실제 사용자 id가 맞는지? 그런 사용자가 있는지 검사
    sql = f"SELECT * FROM users WHERE id={params['user_id']}"
    cursor.execute(sql)
    
    user_result = cursor.fetchone()
    
    if user_result == None :
        return {
            'code' : 400,
            'message' : '해당 사용자 id값이 잘못 되었습니다.'
        }, 400
    
    # 연락처 추가 등록 쿼리
    sql = f"INSERT INTO contacts (user_id, name, phone_num, memo) VALUES ({params['user_id']}, '{params['name']}', '{params['phone']}', '{params['memo']}')"
    
    cursor.execute(sql)
    db.commit()
    
    return {
        'code' : 200,
        'message' : '연락처 등록 성공'
    }