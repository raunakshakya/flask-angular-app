## Using Python, Flask, and Angular to Build Modern Web Apps - Part 1

https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/

    D:\flask-angular-app\online-exam>cd backend    
    D:\flask-angular-app\online-exam\backend>pipenv --three

###### Script to facilitate running the application

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


https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-web-apps-part-2/

We are going to configure an Auth0 API as the identity management system of our Flask application. For startup projects 
like this one, the free tier provided by Auth0 is more than enough. Besides being free, by choosing Auth0, 
we get a modern, easy to use, and reliable service capable of integrating with tons of different social identity 
providers (e.g. Facebook, Google, Twitter, etc). Also, if we ever need to integrate with enterprise identity 
providers using protocols like OpenID Connect, SAML, and WS-Federation, don't worry, Auth0's got you covered.

That is, Auth0 can help us focus on what matters the most to us, the special features of our product. 
In addition, Auth0 can improve oour product's security with state-of-the-art features like passwordless, 
breached password surveillance, and multifactor authentication.