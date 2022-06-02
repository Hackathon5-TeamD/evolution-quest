# evolution-quest

## db 作成

`python3` or `python`
Python 対話モードとなったら

```python
>>> from app import db
>>> db.create_all()
```

※Migration を導入した場合は不要

## CloudFomation による VPC 作成コマンド

パブリック・プライベートサブネットが 2AZ にまたがる可用性のある一般的な VPC 構成

VPC レイヤーの構造を記載した CloudFomation の YML ファイル
vpc.yml

変数を格納しているコンフィグファイル
dev.cfg

### up していません

dev.cfg ファイルが必要となるので寺に問い合わせてください。

上記 2 つのファイルが同じディレクトリにあることを確認後下記コマンドを実施（aws cli 必須）

```bash
aws cloudformation deploy --template-file vpc.yml --stack-name hack5-app --parameter-overrides $(cat dev.cfg) --capabilities CAPABILITY_NAMED_IAM --no-execute-changeset
```

## Git ブランチライフサイクルチートコード

```bash
# リモートdevelopブランチから最新の環境をpullする
git pull origin develop

# 新たにブランチを切る#numberはissue番号
git checkout -b feature/#number

# インデックス（add）・ステージング（commit）した後
git push origin feature/#number

# 完了したfeatureブランチは削除する
git branch -D feature/#number

# 以降繰り返し
```
