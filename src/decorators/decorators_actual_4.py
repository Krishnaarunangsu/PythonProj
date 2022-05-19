from datetime import datetime


def timed_log(log_msg):
    def time_added(*args, **kwargs):
        return f'[{datetime.now()}] {log_msg(*args, **kwargs)}'

    return time_added


@timed_log
def log_error(line_no):
    return f'There is an error happened at line {line_no}'


@timed_log
def log_done():
    return 'Great! All processed done.'


print(log_error(50))
print(log_done())
