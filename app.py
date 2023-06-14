from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        data = get_weather(city, state, country)
    return render_template('index.html', data=data)
    # weather = get_weather(city)
    # return render_template('index.html', weather=weather)
    # return render_template('index.html')
    # return 'index'


# @app.route('/weather')
# def blog():
    # weather_data = get_weather(request.args.get('city_name'), request.args.get('state_name'),
    #                           request.args.get('country_name'))
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
