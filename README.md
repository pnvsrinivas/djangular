# Django - Angular Authentication Demo Application

## Installation

git clone https://github.com/pnvsrinivas/djangular.git


### Setup APIs
cd djangular\apis

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

bash setup.sh

bash runserver.sh

The server will be running on http://127.0.0.1:8005


### Setup UI
cd djangular\spa

npm install

ng serve

This server will be running on http://127.0.0.1:4205