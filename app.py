from flask import Flask #импорт класса фласк

app = Flask(__name__) #создаем объект класса фласк

@app.route("/") #создание маршрута
def hello_world(): #функция, которая будет вызвана при запросе к маршруту
    return "Hello, World!" #возвращение строки

if __name__ == "__main__": #проверка на запуск самого скрипта 
  app.run(host="0.0.0.0", debug=True)