# 진입점
import sys # 시스템 관련 기능을 사용하기 위한 모듈
from PyQt5.QtWidgets import QApplication # PyQt5 애플리케이션의 핵심 클래스
from main_window import MainWindow # main_window.py에 정의된 메인 윈도우 클래스

def main():
    app = QApplication(sys.argv) # QApplication 객체 생성
    window = MainWindow() # MainWindow 인스턴스 생성
    window.show() # 화면에 표시
    sys.exit(app.exec_()) # 이벤트 루프 시작 (사용자 입력 대기) 및 애플리케이션 종료 시 정상적으로 프로그램 종료

if __name__ == "__main__": # 이 파일이 직접 실행될 때만 main() 함수 호출
    main()