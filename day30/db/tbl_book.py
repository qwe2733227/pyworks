#도서 db 만들기
import sqlite3 as sql

def getconn():
    # 데이터베이스 생성 및 접속
    conn = sql.connect("./tbl_book.db")
    return conn

def create_table():
    #테이블 생성
    con = getconn()
    cursur = con.cursor()
    sql = """
        CREATE TABLE book(
            book_no integer PRIMARY KEY AUTOINCREMENT,
            title text NOT NULL,
            publisher text NOT NULL,
            page integer
        ) 
    """
    cursur.execute(sql)
    con.commit()
    con.close()

def insert_book():
    #도서 추가
    con = getconn()
    cursur = con.cursor()
    sql = "INSERT INTO book (title, publisher, page) VALUES(?, ?, ?)"
    # book_no는 자동이므로 입력하면 안됨
    cursur.execute(sql, ('점프 투 파이썬', '박응용', 350))
    con.commit()
    con.close()

def select_book():
    #도서 전체 검색
    con = getconn()
    cursur = con.cursor()
    sql = "SELECT * FROM book"
    cursur.execute(sql)
    #책 정보 가져오기
    rs = cursur.fetchall()
    print(rs)
    con.close()

def select_one():
    #특정 도서 검색
    con = getconn()
    cursur = con.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"
    cursur.execute(sql, (2,))   #튜플 1개일때 콤머 붙임
    # 책 정보 가져오기
    rs = cursur.fetchone()
    print(rs)
    con.close()

def update_book():
    # 도서 수정
    con = getconn()
    cursur = con.cursor()
    sql = "UPDATE book SET page = ? WHERE book_no = ?"
    cursur.execute(sql, (400, 5))
    con.commit()
    con.close()

def delete_book():
    con = getconn()
    cursur = con.cursor()
    sql = "DELETE FROM book WHERE book_no = ?"
    cursur.execute(sql, (3,))
    con.commit()
    con.close()

if __name__=="__main__":
    #con = getconn()
    #print(con, "연결")
    #create_table()
    #insert_book()
    #select_book()
    update_book()
    #delete_book()
    #select_one()

