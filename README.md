# Keycloakとdjango-allauthのPOC

## 事前準備
`127.0.0.1 proxy`を`/etc/hosts`に追加
```sh
sudo vi /etc/hosts
```

※ やりたいことは以下の記事の「ホストマシン側の設定」と同じ

https://ryu22e.org/posts/2024/12/12/allauth-and-keycloak/


## 起動
```sh
docker compose up -d
```
- ログイン画面(django-allauth): http://localhost:18000/accounts/login/
- TOP(ログイン不要): http://localhost:18000/app/
- マイページ(ログイン必須) http://localhost:18000/app/mypage/
- Django Admin: http://localhost:18000/admin/
- Silk: http://localhost:18000/silk/
- Keycloak: http://proxy/

## コンテナにログイン
```sh
docker compose exec django_app /bin/bash
```

## マイグレーション作成
```sh
docker compose exec django_app python manage.py makemigrations
```

## マイグレーション実行
```sh
docker compose exec django_app python manage.py migrate
```

## adminユーザー作成
```sh
docker compose exec django_app python manage.py createsuperuser
```

## フォーマット
```sh
docker compose exec django_app bash -c "ruff check . --fix && ruff format ."
```

## MySQL接続
```sh
mysql -u admin -p --protocol=tcp
```
