from flask import Flask, request
from flask.templating import render_template

from .api import user_test, login_test

def create_app():
    # 플라스크 서버를 변수에 담자
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행
    
    @app.route("/")   # 만들고 있는 서버의 / (아무것도 붙이지 않은 주소) 로 접속하면 보여줄 내용
    def home():
        # return 내용 : HTML 등 웹 프론트엔드 태그 <h1>은 제목으로 제일 큰 글씨로 보여줌
        return "<h1>Hello World!</h1>"   # Hello World 문장 리턴 => 이 내용을 사용자에게 보여주겠다.
           
    @app.route('/module_test')
    def module_test():
        return user_test()  # 다른 모듈의 함수의 실행 결과를 내보내자 => 로직을 다른 모듈에서만 작성하면 됨
    
    @app.route('/login_test')
    def login_01():
        
        # 외부에서 보내준 파라미터들 확인
        params = request.args.to_dict()
        print(f'전달받은 파라미터 : {params}')
        
        # 아이디 : login_id 이름표를 뽑아서 사용
        # 비번 : pw 이름표 뽑아서 사용
        
        id = params['login_id']
        pw = params['pw']
        
        return login_test(id, pw)
    
    # 이 서버를 사용하도록 결과로 내보내자
    return app