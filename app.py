import datetime
from flask import Flask

app = Flask(__name__)

DATE_FORMAT = "%m/%d/%Y"
ANNIVERSARY = '4/27/2018'
MULTIPLIER = 1.5

@app.route('/')
def the_max():
    time_together = calculate_time()
    curr_max = '{:%m/%d/%Y}'.format(calculate_max(time_together))
    return f'Our first date was on {ANNIVERSARY}. We have been dating for {time_together} days.  Our current planning max is {curr_max}.'


def calculate_time():
    anniversary = datetime.datetime.strptime(ANNIVERSARY, DATE_FORMAT).date()
    today = datetime.date.today()
    delta = today - anniversary
    return delta.days


def calculate_max(days):
    n_days = days * MULTIPLIER
    delta = datetime.timedelta(days=n_days)
    anniversary = datetime.datetime.strptime(ANNIVERSARY, DATE_FORMAT).date()
    return delta + anniversary



if __name__ == '__main__':
    app.run(host='0.0.0.0')
