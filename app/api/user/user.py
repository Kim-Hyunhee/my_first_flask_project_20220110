from pymysql import connect
from pymysql.cursors import DictCursor

# 사용자 정보 관련된 기능들을 모아두는 모듈
# app.py에서 이 함수들을 끌어다 사용

def user_test():
    
    # 추가 기능 작성
    
    # DB에서 아이디/비번을 조회해서 로그인 확인 등등
        
    return{
        'name' :'김현희',
        'birth_year' :1995
    }
    
def login_test(id, pw):
    # id, pw를 이용해서 -> SQL 쿼리 작성 -> 결과에 따라 다른 응답 리턴
    
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
    
    sql = "SELECT * FROM users WHERE email='{id}' AND password='{pw}'"
    cursor.execute(sql)
    
    query_result = cursor.fetchone()  # 검색 결과 없으면 None 리턴
    
    # 쿼리 결과 : None -> 아이디 비번 맞는 사람 X -> 로그인 실패
    if query_result == None :
        return {
            'code':400,
            'message':'아이디 또는 비번이 잘못되었습니다.'
        }, 400
    else:
        # 검색 결과 있다. => 아이디/비번 모두 맞는 사람 O -> 로그인 성공
        # query_result 가 실제가 있다. (None이 아니다.) => 앱에서 사용 가능한 JSONObject로 보내보자
        
        print(query_result)
        
        user_dict = {
            'id': query_result['id'],
            'email': query_result['email'],
            'nickname': query_result['nickname']
        }
        
        return {
            'code' :200,
            'message' : '로그인 성공',
            'data' : {
                'user' : user_dict,
            }
        }
         