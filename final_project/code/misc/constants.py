STATUS_OK = 200
STATUS_CREATED = 201
STATUS_NO_CONTENT = 204
STATUS_NOT_MODIFIED = 304
STATUS_BAD_REQUEST = 400
STATUS_UNAUTHORIZED = 401
STATUS_NOT_FOUND = 404

METHOD_GET = 'GET'
METHOD_POST = 'POST'

MYSQL_HOST = 'mysql'
MYSQL_DB_NAME = 'myapp_db'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'pass'

MYAPP_PORT = 7331
MYSQL_PORT = 3306
SELENOID_PORT = 4444

VALID_USERNAME = 'username'
VALID_PASSWORD = 'password'
VALID_EMAIL = 'user@mail.ru'

CONTROL_USER_USERNAME = 'kirill'
CONTROL_USER_PASSWORD = 'kirill_pass'
CONTROL_USER_EMAIL = 'kirill@mail.ru'
CONTROL_USER_ID = '3'

ERROR_USER_EXISTS = 'User already exist'
ERROR_USERNAME_LENGTH = 'Incorrect username length'
ERROR_PASSWORD_LENGTH = 'Incorrect password length'
ERROR_PASSWORD_MATCH = 'Passwords must match'
ERROR_EMAIL_LENGTH = 'Incorrect email length'
ERROR_EMAIL_INVALID = 'Invalid email address'
ERROR_INVALID_USERNAME_OR_PASSWORD = 'Invalid username or password'
ERROR_EMPTY_USERNAME = 'Необходимо указать логин для авторизации'
ERROR_EMPTY_PASSWORD = 'Необходимо указать пароль для авторизации'

INVALID_USERNAME_TOO_SHORT = '2shrt'
INVALID_USERNAME_TOO_LONG = 'usernamethatistoolong'  # >16 (21) characters
INVALID_USERNAME_NONEXISTENT = 'nosuchuser'
INVALID_PASSWORD_TOO_LONG = 'passwordthatistool' + 'o' * 236 + 'ng'  # 255 + 1 characters
INVALID_EMAIL_TOO_SHORT = 't@s.t'
INVALID_EMAIL_TOO_LONG = 'emailthatistool' + 'o' * 40 + 'ng@mail.ru'  # 64 + 1 characters
INVALID_EMAIL_FORMAT = 'definitely a valid email :)'
