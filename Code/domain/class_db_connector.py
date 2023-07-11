import sqlite3

from Code.domain.class_user import User
from Code.domain.class_user_talk_room import UserTalkRoom
from Code.domain.class_talk_room import TalkRoom
from Code.domain.class_message import Message
from Code.domain.class_long_contents import LongContents


class DBConnector:
    _instance = None

    def __new__(cls, test_option=None):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, test_option=None):
        self.conn = None
        self.test_option = test_option

    def start_conn(self):
        if self.test_option is True:
            self.conn = sqlite3.connect('db_test.db')

        else:
            self.conn = sqlite3.connect('main_db.db')
        return self.conn.cursor()

    def end_conn(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def commit_db(self):
        if self.conn is not None:
            self.conn.commit()
        else:
            raise f"cannot commit database! {self.__name__}"

    # CREATE TABLES =======================================================================
    def create_tables(self):
        c = self.start_conn()
        c.executescript("""
            DROP TABLE IF EXISTS user;
            CREATE TABLE "user" (
                "user_id"	INTEGER,
                "username"	TEXT NOT NULL UNIQUE,  
                "password"	TEXT NOT NULL,
                "nickname"	TEXT NOT NULL,
                PRIMARY KEY("user_id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS user_talk_room;
            CREATE TABLE "user_talk_room" (
                "user_talk_room_id"	INTEGER,
                "user_id" INTEGER,
                "talk_room_id"	INTEGER,
                PRIMARY KEY("user_talk_room_id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS talk_room;
            CREATE TABLE "talk_room" (
                "talk_room_id"	INTEGER,
                "talk_room_name" TEXT NOT NULL,
                "open_time_stamp"	TEXT NOT NULL,
                PRIMARY KEY("talk_room_id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS message;
            CREATE TABLE "message" (
                "message_id" INTEGER, 
                "sender_user_id" INTEGER, 
                "talk_room_id" INTEGER,
                "send_time_stamp" TEXT, 
                "contents" TEXT, 
                "long_contents_id" INTEGER,
                PRIMARY KEY("message_id" AUTOINCREMENT)
            );
            DROP TABLE IF EXISTS long_contents;
            CREATE TABLE "long_contents" (
                "contents_id" INTEGER, 
                "contents_type" INTEGER, 
                "long_text" TEXT, 
                "image" BLOB,
                PRIMARY KEY("contents_id" AUTOINCREMENT)
            );

        """)
        self.commit_db()
        self.end_conn()

    # user 테이블========================================================================================
    def insert_user(self, user_object: User):
        c = self.start_conn()
        user_id = user_object.user_id
        user_name = user_object.username
        password = user_object.password
        nickname = user_object.nickname
        users_id = c.execute('select * from user where user_id = ?', (user_id,)).fetchone()

        if users_id is None:
            c.execute('insert into user(username, password, nickname) values (?, ?, ?)',
                      (user_name, password, nickname))
            self.commit_db()
            inserted_user_row = c.execute('select * from user order by user_id desc limit 1').fetchone()
            inserted_user_obj = User(*inserted_user_row)
            self.end_conn()
            return inserted_user_obj
        else:
            updated_user_obj = self.update_user(user_object)
            return updated_user_obj

    def update_user(self, user_object: User):
        c = self.start_conn()
        user_id = user_object.user_id
        user_name = user_object.username
        password = user_object.password
        nickname = user_object.nickname
        c.execute('update user set username=?, password = ?, nickname=? where user_id = ?',
                  (user_name, password, nickname, user_id))
        self.commit_db()
        updated_user_row = c.execute('select * from user where user_id = ?', (user_id,)).fetchone()
        updated_user_obj = User(*updated_user_row)
        self.end_conn()
        return updated_user_obj

    # User 찾기
    def find_all_user(self):
        c = self.start_conn()
        user_data = c.execute('select * from user').fetchall()
        if user_data is None:
            return None
        all_user_obj_list = list()
        for row_user in user_data:
            all_user_obj_list.append(User(*row_user))
        self.end_conn()
        return all_user_obj_list

    def find_user_by_username(self, username):
        c = self.start_conn()
        user_data = c.execute('select * from user where username = ?', (username,)).fetchone()
        if user_data is None:
            return None
        user_object = User(*user_data)
        self.end_conn()
        return user_object

    def find_user_by_user_id(self, user_id):
        c = self.start_conn()
        user_data = c.execute('select * from user where user_id = ?', (user_id,)).fetchone()
        if user_data is None:
            return None
        user_object = User(*user_data)
        self.end_conn()
        return user_object

    # user 삭제
    def delete_user_by_username(self, username: str):
        c = self.start_conn()
        deleted_user = c.execute('select * from user where username = ?', (username,)).fetchone()
        deleted_user_obj = User(*deleted_user)
        c.execute('delete from user where username = ?', (username,))
        self.commit_db()
        self.end_conn()
        return deleted_user_obj

    def delete_user_by_user_id(self, user_id):
        c = self.start_conn()
        deleted_user = c.execute('select * from user where user_id = ?', (user_id,)).fetchone()
        deleted_user_obj = User(*deleted_user)
        c.execute('delete from user where user_id = ?', (user_id,))
        self.commit_db()
        self.end_conn()
        return deleted_user_obj

    # id 기준으로 함수로 하나 더 만들기

    # user_talk_room================================================
    # 새로운 채팅방 생성 함수 호출 및 user_talk_room 테이블 정보 추가
    # def insert_user_talk_room(self, user_id, talk_room_name, open_time_stamp):
    #     talk_room_obj = self.create_talk_room(talk_room_name, open_time_stamp)
    #     c = self.start_conn()
    #     talk_room_id = talk_room_obj.talk_room_id
    #     c.execute('insert into user_talk_room (user_id, talk_room_id) values (?, ?)', (user_id, talk_room_id))
    #     self.commit_db()
    #     self.end_conn()

    def insert_user_talk_room(self, user_talk_room_obj: UserTalkRoom):
        c = self.start_conn()
        # user_talk_room_id = user_talk_room_obj.user_talk_room_id
        user_id = user_talk_room_obj.user_id
        talk_room_id = user_talk_room_obj.talk_room_id
        c.execute('insert into user_talk_room (user_id, talk_room_id) values (?, ?)', (user_id, talk_room_id))
        self.commit_db()
        inserted_user_talk_room_row = c.execute('select * from user_talk_room order by user_talk_room_id desc limit 1').fetchone()
        inserted_user_talk_room_obj = UserTalkRoom(*inserted_user_talk_room_row)
        self.end_conn()
        return inserted_user_talk_room_obj

    # 유저가 속한 모든 채팅방 객체 반환
    def find_all_talk_room_by_user_id(self, user_id: int) -> list[TalkRoom]:
        c = self.start_conn()
        users_talk_room_list = list()
        user_talk_rooms = c.execute('select * from user_talk_room where user_id = ?', (user_id,)).fetchall()
        # talk_rooms = c.execute('select * from talk_room').fetchall()
        for user_talk_row in user_talk_rooms:
            user_talk_room_obj = UserTalkRoom(*user_talk_row)
            searched_talk_room = self.find_talk_room_by_talk_room_id(user_talk_room_obj)
            users_talk_room_list.append(searched_talk_room)
        self.end_conn()
        return users_talk_room_list

    def find_all_talk_room_by_username(self, username: str) -> list[TalkRoom]:
        c = self.start_conn()
        username_row = c.execute('select * from user where username = ?', (username,)).fetchone()
        user_id = username_row[0]
        self.end_conn()
        result = self.find_all_talk_room_by_user_id(user_id)
        return result

    # talk_room_id에 해당하는 톡방에 있는 유저 객체 반환
    def find_all_user_by_talk_room_id(self, talk_room_id: int) -> list[User]:
        c = self.start_conn()
        all_user = list()
        involved_user = c.execute('select * from user_talk_room where talk_room_id = ?', (talk_room_id,)).fetchall()
        if len(involved_user) == 0:
            return None
        for user in involved_user:
            user_id = user[1]
            user = c.execute('select * from user where user_id = ?', (user_id,)).fetchone()
            all_user.append(User(*user))
        self.end_conn()
        return all_user

    # 회원이 자신이 속한 모든 톡방을 나간 경우(탈퇴 등-이미 탈퇴 함수 있음), user_id / username에 따라 삭제(유저가 속한 모든 톡방 나감)
    def delete_user_talk_room_by_user_id(self, user_id):
        c = self.start_conn()
        c.execute('delete from user_talk_room where user_id = ?', (user_id,))
        self.commit_db()
        self.end_conn()

    def delete_user_talk_room_by_username(self, user_name):
        out_user_id = self.find_user_by_username(user_name).user_id
        self.delete_user_talk_room_by_user_id(out_user_id)

    # 회원이 자신이 속한 특정 톡방을 나간 경우, user_id / username에 따라 삭제(해당 톡방만 나감)
    def delete_user_talk_room_by_user_id_and_talk_room_id(self, user_id, talk_room_id):
        c = self.start_conn()
        c.execute('delete from user_talk_room where user_id = ? and talk_room_id = ?', (user_id, talk_room_id))
        self.commit_db()
        self.end_conn()

    def delete_user_talk_room_by_username_and_talk_room_id(self, user_name, talk_room_id):
        out_user_id = self.find_user_by_username(user_name).user_id
        self.delete_user_talk_room_by_user_id_and_talk_room_id(out_user_id, talk_room_id)

    # 회원 탈퇴한 경우 user테이블 삭제 함수 및 user_talk_room 삭제 함수 호출(user 및 user_talk_room 모두 삭제)
    def delete_withdrawal_user_talk_room_by_username(self, user_name: str):
        withdrawal_user_id = self.delete_user_by_username(user_name).user_id
        self.delete_user_talk_room_by_user_id(withdrawal_user_id)


    def delete_withdrawal_user_talk_room_by_user_id(self, user_id):
        self.delete_user_by_user_id(user_id)
        self.delete_user_talk_room_by_user_id(user_id)

    # talk_room 테이블=======================================================
    # 새로운 채팅방 생성
    def create_talk_room(self, talk_room_name, open_time_stamp):
        c = self.start_conn()
        c.execute('insert into talk_room (talk_room_name, open_time_stamp) values (?, ?)',
                  (talk_room_name, open_time_stamp))
        self.commit_db()
        created_talk_room = c.execute('select * from talk_room order by talk_room_id desc limit 1').fetchone()
        created_talk_room_obj = TalkRoom(*created_talk_room)
        self.end_conn()
        return created_talk_room_obj

    def find_talk_room_by_talk_room_id(self, user_talk_room_obj: UserTalkRoom):
        c = self.start_conn()
        talk_room_id = user_talk_room_obj.talk_room_id
        row_data = c.execute('select * from talk_room where talk_room_id = ?', (talk_room_id,)).fetchone()
        talk_room_obj = TalkRoom(*row_data)
        self.end_conn()
        return talk_room_obj

    # message테이블===================================================================================
    def insert_message(self, sender_user_id, talk_room_id, send_time_stamp, contents=None, long_contents_id=None):
        c = self.start_conn()
        c.execute('insert into message (sender_user_id, talk_room_id, send_time_stamp, contents, long_contents_id',
                  (sender_user_id, talk_room_id, send_time_stamp, contents, long_contents_id))
        self.commit_db()
        inserted_message_row = c.execute('select * from message order by message_id desc limit 1').fetchone()
        inserted_message_obj = Message(*inserted_message_row)
        self.end_conn()
        return inserted_message_obj

    def find_message_by_message_id(self, message_id):
        c = self.start_conn()
        message_row = c.execute('select * from message where message_id = ?', (message_id,)).fetchone()
        message_obj = Message(*message_row)
        self.end_conn()
        return message_obj

    # long_contents 테이블==========================================================================================
    # contents_type - 0 : long_text, 1: image
    def insert_long_contents(self, contents_type, long_text=None, image=None):
        c = self.start_conn()
        if contents_type == 0 and long_text is not None:
            c.execute('insert into long_content (contents_type, long_text) values (?, ?)', (contents_type, long_text))
            self.commit_db()
            inserted_long_contents = c.execute(
                'select * from long_contents order by contents_id desc limit 1').fetchone()
            inserted_long_contents_obj = LongContents(*inserted_long_contents)
            self.end_conn()
            return inserted_long_contents_obj

        elif contents_type == 0 and long_text is not None:
            raise f"콘텐츠타입{contents_type} 과 롱텍스트{long_text} 불일치, 이미지{image}"

        elif contents_type == 1 and image is not None:
            c.execute('insert into long_content (contents_type, image) values (?, ?)', (contents_type, image))
            self.commit_db()
            inserted_long_contents = c.execute(
                'select * from long_contents order by contents_id desc limit 1').fetchone()
            inserted_long_contents_obj = LongContents(*inserted_long_contents)
            self.end_conn()
            return inserted_long_contents_obj

        elif contents_type == 1 and image is None:
            raise f"콘텐츠타입{contents_type} 과 이미지{image} 불일치, 롱텍스트{long_text}"

    def find_long_contents_by_contents_id(self, contents_id):
        c = self.start_conn()
        long_contents_row = c.execute('select * from long_contents where contents_id = ?', (contents_id,)).fetchone()
        long_contents_obj = LongContents(*long_contents_row)
        self.end_conn()
        return long_contents_obj

    # ui 우선 사용 함수=============================================================================================
    # 사용자 아이디 중복 확인
    def assert_same_login_id(self, inserted_id):
        c = self.start_conn()
        username_id = c.execute('select * from user where username = ?', (inserted_id,)).fetchone()
        if username_id is None:
            print('사용 가능한 아이디 입니다.')  # 사용 가능 아이디
            return True
        else:
            print('사용 불가능한 아이디 입니다.')  # 사용불가
            return False

    # 회원가입용 함수(insert_user함수 호출)
    def user_sign_up(self, insert_id, insert_pw, nickname):
        useable_id = self.assert_same_login_id(insert_id)
        if useable_id == False:
            return False
        c = self.start_conn()
        last_user_row = c.execute('select * from user order by user_id desc limit 1').fetchone()
        user_id = last_user_row[0] + 1
        sign_up_user_obj = User(user_id, insert_id, insert_pw, nickname)
        self.end_conn()
        sing_up_obj = self.insert_user(sign_up_user_obj)
        return sing_up_obj

    # 사용자 로그인 함수
    def user_log_in(self, login_id, login_pw):
        c = self.start_conn()
        exist_user = c.execute('select * from user where username = ? and password = ?',
                               (login_id, login_pw)).fetchone()
        self.end_conn()
        if exist_user is not None:
            print('로그인 성공')
            login_user_obj = User(*exist_user)
            return login_user_obj
        else:
            print('아이디 혹은 비밀번호를 잘못 입력했습니다.')
            return False

if __name__ == '__main__':
    dbconn = DBConnector()
    dbconn.create_tables()
    user1 = User(1, '짱구', '12345', '짱구닉네임')
    user2 = User(2, '철수', '12345', '철수닉네임')
    user3 = User(3, '훈이', '12345', '훈이닉네임')
    user4 = User(4, '유리', '12345', '유리닉네임')
    user5 = User(5, '맹구', '12345', '맹구닉네임')
    # print('>>> insert_user/update_user')
    print(dbconn.insert_user(user1))
    print(dbconn.insert_user(user2))
    print(dbconn.insert_user(user3))
    print(dbconn.insert_user(user4))
    print(dbconn.insert_user(user5))
    # print('\n>>> find_all_user')
    # print(dbconn.find_all_user())
    # print('\n>>> find_user_by_username')
    # print(dbconn.find_user_by_username('훈이'))
    # print(dbconn.find_user_by_username('철수'))
    # print('\n>>> find_user_by_user_id')
    # print(dbconn.find_user_by_user_id(1))
    # print(dbconn.find_user_by_user_id(5))
    # print('\n>>> delete_user_by_username')
    # print(dbconn.delete_user_by_username('유리'))
    # # print(dbconn.delete_user_by_username('안경')) #존재하지 않는 username 입력하면 오류남(당연함)
    # print(dbconn.find_all_user())
    # print('\n>>> delete_user_by_user_id')
    # print(dbconn.delete_user_by_user_id(2))
    # print(dbconn.find_all_user())

    # dbconn.update_user()

    # LongContents(1, 0, long_text = '아주 긴 글')
    # LongContents(2, 1, long_text = '아주 긴 글')
    # LongContents(3, 0, image = '아주 긴 글')
    # LongContents(4, 1, image = '사진')
    usertalkroom1 = UserTalkRoom(1, 1, 1)
    usertalkroom2 = UserTalkRoom(2, 1, 2)
    usertalkroom3 = UserTalkRoom(3, 4, 2)
    usertalkroom4 = UserTalkRoom(4, 4, 3)
    usertalkroom5 = UserTalkRoom(4, 4, 3)
    # usertalkroom1 = UserTalkRoom(5, 1, 2)

    talkroom1 = TalkRoom(1, '1번방', '2023-01-01')
    talkroom2 = TalkRoom(2, '2번방', '2023-02-01')
    talkroom3 = TalkRoom(3, '3번방', '2023-03-01')

    print(dbconn.insert_user_talk_room(usertalkroom1))
    print(dbconn.insert_user_talk_room(usertalkroom2))
    print(dbconn.insert_user_talk_room(usertalkroom3))
    print(dbconn.insert_user_talk_room(usertalkroom4))
    print(dbconn.insert_user_talk_room(usertalkroom5))

    print(dbconn.create_talk_room('1번방', '2023-01-01'))
    print(dbconn.create_talk_room('2번방', '2023-02-01'))
    print(dbconn.create_talk_room('3번방', '2023-03-01'))
    # print(dbconn.find_all_talk_room_by_user_id(1))
    # print(dbconn.find_all_talk_room_by_username('유리'))

    # print(dbconn.find_all_talk_room_by_username('철수'))
    # print(dbconn.find_all_talk_room_by_username('맹구'))
    # print('>>> find_all_user_by_talk_room_id')
    # print(dbconn.find_all_user_by_talk_room_id(2))
    # print('delete_user_talk_room_by_user_id / delete_user_talk_room_by_user_id')
    # print(dbconn.find_all_talk_room_by_user_id(1))
    # print(dbconn.find_all_talk_room_by_username('짱구'))
    # dbconn.delete_user_talk_room_by_user_id(1)
    # dbconn.delete_user_talk_room_by_username('짱구')
    # dbconn.delete_user_talk_room_by_user_id_and_talk_room_id(1, 1)
    # dbconn.delete_user_talk_room_by_username_and_talk_room_id('짱구', 1)
    # dbconn.delete_withdrawal_user_talk_room_by_user_id(1)
    # dbconn.delete_withdrawal_user_talk_room_by_username('짱구')
    # print(dbconn.find_all_talk_room_by_user_id(1))
    # print(dbconn.find_all_user())
    # print(dbconn.find_all_talk_room_by_username('짱구'))

    print(dbconn.find_talk_room_by_talk_room_id(talkroom1))
    # # 로그인 아이디, 비밀번호 일치 여부 반환
    # dbconn.user_log_in('짱구', '12345')
    # dbconn.user_log_in('짱구', '11111')
    # # 아이디 중복 확인
    # print(dbconn.assert_same_login_id('철수'))
    # print(dbconn.assert_same_login_id('abcde'))
    # #회원가입
    # print(dbconn.user_sign_up('abcde', '12345', '알파벳'))
    # print(dbconn.find_all_user())
