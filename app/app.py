from flask import Flask

def create_app():
    # 플라스크 서버를 변수에 담자
    app = Flask(__name__)
    
    # 서버에 대한 세팅 진행
    
    @app.route("/")   # 만들고 있는 서버의 / (아무것도 붙이지 않은 주소) 로 접속하면 보여줄 내용
    def test():
        # return 내용 : HTML 등 웹 프론트엔드 태그 <h1>은 제목으로 제일 큰 글씨로 보여줌
        return "<h1>Hello World!</h1>"   # Hello World 문장 리턴 => 이 내용을 사용자에게 보여주겠다.
    
    # 이 서버를 사용하도록 결과로 내보내자
    return app