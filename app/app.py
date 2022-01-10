from flask import Flask, jsonify
from flask.templating import render_template

def create_app():
    # 플라스크 서버를 변수에 담자
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행
    
    @app.route("/")   # 만들고 있는 서버의 / (아무것도 붙이지 않은 주소) 로 접속하면 보여줄 내용
    def home():
        # return 내용 : HTML 등 웹 프론트엔드 태그 <h1>은 제목으로 제일 큰 글씨로 보여줌
        return "<h1>Hello World!</h1>"   # Hello World 문장 리턴 => 이 내용을 사용자에게 보여주겠다.
    
    @app.route("/test") # 서버의 /test 주소로 오면 수행해줄 일을 작성
    def test():
        return "이곳은 테스트 페이지 입니다."  # 서버/test 로 오면 보여줄 내용
    
    @app.route("/web")
    def web_test():
        return render_template('web_test.html')  # templates 폴더 내부의 파일을 불러는 역할 (render_template)
    
    @app.route("/json")
    def json_test():
        # JSON 양식 => "이름표" : 실제값의 조합 => dict를 이용하면 작업이 편하다.
        test_dict = {}
        test_dict['name'] = '김현희'
        test_dict['birth_year'] = 1995
        test_dict['height'] = 178.8
        test_dict["is_female"] =True
        
        return jsonify(test_dict) # dict -> json 변경 함수 활용 => JSON 응답 내려주기
    
    # 이 서버를 사용하도록 결과로 내보내자
    return app