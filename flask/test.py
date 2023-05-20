#필요한 데이터모드를 import
from datetime import datetime

def current_time():
    #now함수를 now변수에 할당
    now = datetime.now()

    #원하는 형식으로 시간을 출력해 줄 수 있는 strftime을 이용하여
    #익숙한 형태의 문자열로 변환해 준다.
    time_string = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")

    #문자열 포멧팅을 이용하여 현재시간을 할당하여 print로 출력
    return f"현재 시간 : {time_string}"

if __name__ == '__main__':
    print(current_time())