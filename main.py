from app import create_app

# 플라스크 라이브러리를 구동시켜주는 역할

# 라이브 서버 (운영) / 개발용 서버 를 구별해서 돌려야 할 필요가 있다.
#  => 관련 세팅들을 쉽게 관리할 수 있도록 도와주는 역할

app = create_app()

# 다른 (모든) 컴퓨터에서도 접속할 수 있게 허용해주자 => 0.0.0.0으로 주소 설정
app.run( host='0.0.0.0' )