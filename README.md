# bootstrap-tornado
Write a tornado app from a template

# Install
```
npm i -g bower
bower install

# suggest use virtualenv
pip install -r requirements.txt
```

Install rethinkdb 

# Usage
```
python -u web.py --port 6000 # --debug
```

Environments can be used to set Rethinkdb

- RDB_NAME
- RDB_HOST
- RDB_PORT

- SECRET_COOKIE

See [settings.py](settings.py) for more details.

# Database
rethinkdb

# LICENSE
[MIT](LICENSE)