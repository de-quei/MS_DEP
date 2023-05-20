from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def current_time():
    now = datetime.now()
    time_string = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
    return f"현재 시간 : {time_string}"

if __name__ == '__main__':
    app.run()