Freedom Python Logger
=====

Installation
-----

```sh
sudo pip3 install freedom_python_logger
```

Usage
-----

```py
from freedom_python_logger import logger

log = logger('config.ini')
```

Config File Format
-----
```ini
[logger]
name=
level=

[file_logger]
file_path=
max_log_file_size=
backup_count=
level=

[email_logger]
host=
port=
from=
to=
subject=
username=
password=
level=
```

Logging Levels
-----
- CRITICAL
- ERROR
- WARNING
- INFO
- DEBUG
- NOTSET
