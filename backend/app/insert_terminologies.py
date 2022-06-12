import csv

from data.sampledata import sampleusers, samplresults
from model import Terminologie, Person, Result, db

# DBの初期化,terminologiesの初期データを挿入する

def insert_user():
    """
    サンプルユーザーデータをコンテナ立ち上げ時に挿入する.
    """
    for i in sampleusers:
        u  = Person(
            user_name=i["user_name"],
            password=i["password"]
            )
        db.session.add(u)
    db.session.commit()

def insert_result():
    """
    サンプルリザルトデータをコンテナ立ち上げ時に挿入する. ※おそらくDateTimeの問題で挿入できていない
    """
    for i in samplresults:
        u  = Result(
            user_id=i["user_id"],
            accuracy_value=i["accuracy_value"],
            wpm=i["wpm"],
            playd_at_date=i["playd_at_date"]
            )
        db.session.add(u)
    db.session.commit()

def insert_terminologie():
    """
    問題のデータをコンテナ立ち上げ時に挿入する.
    """
    with open("csv/terminologie.csv", "r", encoding="utf-8_sig") as f:
        data = csv.reader(f)
        for i, row in enumerate(data):
            if i == 0:
                continue
            else:
                insert_data = Terminologie(
                    genre_id=row[0],
                    theme_jp=row[1],
                    theme_ro=row[2],
                    description_ja=row[3],
                    description_ro=row[4],
                )

                db.session.add(insert_data)
    db.session.commit()


if __name__ == "__main__":
    db.create_all()
    insert_user()
    insert_result()
    insert_terminologie()
