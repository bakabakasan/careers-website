from flask import Flask, render_template, jsonify

app = Flask(__name__) #создаем объект класса фласк
JOBS = [
  {
    'id': 1, 
    'title': 'Data Analyst',
    'location': 'Minsk, Belarus',
    'salary': '1000$',
  },
  {
    'id': 2, 
    'title': 'Frontend Developer',
    'location': 'Warsaw, Poland',
    'salary': '2300$',
  },
  {
  'id': 3, 
  'title': 'Data Scientist',
  'location': 'Remote',
  'salary': '2000$',
  },
  {
  'id': 4, 
  'title': 'Backend Developer',
  'location': 'Moscow, Russia',
  'salary': '2300$',
  }
]

@app.route("/") #создание маршрута
def hello_world(): #функция, которая будет вызвана при запросе к маршруту
    return render_template('home.html', jobs=JOBS) 

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__": #проверка на запуск самого скрипта 
  app.run(host="0.0.0.0", debug=True)