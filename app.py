from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # return 'index'


@app.route('/weather')
def blog():
    # weather_data = get_weather(request.args.get('city_name'), request.args.get('state_name'),
    #                           request.args.get('country_name'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
