# Lab4
Варіант 10:
('python 3.6.*', 'virtualenv + requirements.txt')
Для виконання лабораторної роботи використовується GitHub.
За допомогою PyEnv інстальовано Python 3.6.3.
Встановлено virtualenv i Flask
Реалізовано адресу api/v1/hello-world-10
Для запуску проекту використовується WSGI сервер waitress.



Для розгортання проекту:
1) в командному рядку перейти до Lab4\virtualenv-name\
2) запустити команду Lab4\virtualenv-name\Scripts\activate або Lab4\virtualenv-name\Scripts\activate.ps1 (для PowerShell)
3) запустити команду waitress-serve --host 127.0.0.1 --port 5000 --call "helloworld10:create_app"
4) відкрити в браузері  http://127.0.0.1:5000/api/v1/hello-world-10
