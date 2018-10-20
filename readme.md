## Using Python, Flask, and Angular to Build Modern Web Apps - Part 1

https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/

    $ ./bootstrap.sh &
    
    $ curl -X POST -H 'Content-Type: application/json' -d '{
          "title": "TypeScript Advanced Exam",
          "description": "Tricky questions about TypeScript."
        }' http://127.0.0.1:5000/exams
    
    $ curl http://127.0.0.1:5000/exams

In Windows:
    
    D:\flask-angular-app\online-exam\backend> bootstrap.bat
    
    > curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"TypeScript Advanced Exam\", \"description\":\"Tricky questions about TypeScript.\"}" http://127.0.0.1:5000/exams
    
    > curl http://127.0.0.1:5000/exams


Running the frontend application

    (online-exam)  D:\flask-angular-app\online-exam> cd frontend
    
    (online-exam)  D:\flask-angular-app\online-exam\frontend> ng serve
