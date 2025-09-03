from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
CORS(app)

CSV_FILE = 'daily_log.csv'

# اگر فایل وجود نداشت، هدرها رو بنویس
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'mood', 'energy', 'motivation', 'stress', 'activities', 'diary',
            'sleep_time', 'sleep', 'exercise','exercise_dur', 'water', 'fatigue', 'meals',
            'focus', 'workHours', 'tasksDone', 'distraction',
            'phoneUsage', 'topApps', 'movieTime', 'gamingTime',
            'interaction', 'loneliness', 'socialEvent',
            'satisfaction', 'meditation', 'testTaken',
            'tomorrowFeeling', 'tomorrowPlan'
        ])

@app.route('/api/save', methods=['POST'])
def save_data():
    data = request.get_json()

    # تبدیل boolean به string برای ذخیره در CSV
    row = [
        #mental
        data.get('mood', ''),
        data.get('energy', ''),
        data.get('motivation', ''),
        data.get('stress', ''),
        data.get('activities', ''),
        data.get('diary', ''),
        #physical
        data.get('sleep_time', ''),
        data.get('sleep', ''),
        data.get('exercise', ''),
        data.get('exercise_dur', ''),
        data.get('water', ''),
        data.get('fatigue', ''),
        data.get('meals', ''),
        #productivity
        data.get('focus', ''),
        data.get('workHours', ''),
        'Yes' if data.get('tasksDone') else 'No',
        data.get('distraction', ''),
        #technology
        data.get('phoneUsage', ''),
        data.get('topApps', ''),
        data.get('movieTime', ''),
        data.get('gamingTime', ''),
        #social
        data.get('interaction', ''),
        data.get('loneliness', ''),
        data.get('socialEvent', ''),
        #personal
        data.get('satisfaction', ''),
        'Yes' if data.get('meditation') else 'No',
        'Yes' if data.get('testTaken') else 'No',
        data.get('tomorrowFeeling', ''),
        data.get('tomorrowPlan', ''),
    ]

    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

    return jsonify({'message': 'Data saved to CSV'}), 200
    
@app.route('/api/download', methods=['GET'])
def download_csv():
    return send_file(CSV_FILE, as_attachment=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)



