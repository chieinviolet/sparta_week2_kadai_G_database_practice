"""
1,データベースファイルを作るよ
2,データベースに書き込むよ
3,データベースからすべてのデータを取り出して表示するよ

"""
import sqlite3


def create_database():
    # print("a")
    conn = sqlite3.connect("age.db")
    sql = """create table  if not exists users(name text, age integer)"""
    cursor = conn.cursor()

    cursor.execute(sql)

    conn.commit()


def insert_database(input_name, input_age):
    connection = sqlite3.connect("age.db")
    cursor = connection.cursor()
    sql = 'INSERT INTO users(name, age) VALUES (?,?)'  # columunタグに ?,? を挿入する)
    cursor.execute(sql, (input_name, input_age))
    print(cursor)
    connection.commit()
    connection.close()


# データをテーブルから探して全部取り出したい
def get_all_data():
    connection = sqlite3.connect("age.db")
    cursor = connection.cursor()

    sql = f'select * from users '
    query_result = cursor.execute(sql)
    users = query_result.fetchall()  # タプルのリスト[(), ()]が返ってきます。Docに書いてます。
    connection.close()
    # print(users)
    # return users
    for person in users:
        print(f'Name: {person[0]}, Age: {person[1]}')


def not_found():
    print("command not found")


def say_bye():
    print("Bye!!")


def main():
    create_database()
    while True:
        input_letter = input("commandを入力してね :) >>")

        if input_letter == "a":
            input_name = input("名前を教えてね>")
            input_age = input("年齢を教えてね>")

            insert_database(input_name, input_age)  # command "a"
        if input_letter == "s":
            get_all_data()  # データ全部並べちゃうぜ  command "s"
        if input_letter == "x":
            not_found()  # コマンドx
            # qを入力したら終了するよ
        if input_letter == "q":
            say_bye()
            break
            # command q


if __name__ == '__main__':
    main()
