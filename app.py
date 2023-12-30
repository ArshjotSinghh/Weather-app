from flask import Flask, render_template, jsonify
import requests

app= Flask(__name__, static_url_path='/static')


def fahrenheit_to_celcius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result_page():
    try:
        ip_address =requests.get('https://api64.ipify.org?format=json').json()   
        ip_address=ip_address['ip']
        print(ip_address)
        ip_stack_key='bbd1b0be3c33d5358bfec4931e44e2f0'
        ip_stack_url = f"http://api.ipstack.com/{ip_address}?access_key={ip_stack_key}"
        response = requests.get(ip_stack_url)
        ip_data = response.json()
        lat = ip_data["latitude"]
        lon = ip_data["longitude"]
        openweather_api_key='fb4946664b1bd1d81772c212df9b43d7'
        openweathermap_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweather_api_key}"
        response = requests.get(openweathermap_url)
        weather_data = response.json()
        return weather_data
    except Exception as e:
        print(e)

       

if __name__ == '__main__':
    app.run(debug=True)
