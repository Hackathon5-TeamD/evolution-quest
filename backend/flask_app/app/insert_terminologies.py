import csv

from model import Terminologie, db


# DBの初期化,terminologiesの初期データを挿入する


def insert_terminologie():
    """
    問題のデータをコンテナ立ち上げ時に挿入する.
    """
    with open("csv/terminologie.csv", "r") as f:
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
    insert_terminologie()
