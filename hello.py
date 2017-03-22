#import cgi
def application(environ, start_response):
    #post_env = environ.copy()
    # бизнес-логика
    status = '200 OK'
    headers = [
    ('Content-Type', 'text/plain')
    ]
    body = 'Hello, world!'
    # post = cgi.FieldStorage(
    #     fp=environ['wsgi.input'],
    #     environ=post_env,
    #     keep_blank_values=True
    # )
    # for i in post:
    #     print(i,'=',i.value)
    start_response(status, headers )
    return [ body ]
