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
    OR:
    (online-exam)  D:\flask-angular-app\online-exam\frontend> npm start

https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-web-apps-part-2/

We are going to configure an Auth0 API as the identity management system of our Flask application. For startup projects 
like this one, the free tier provided by Auth0 is more than enough. Besides being free, by choosing Auth0, 
we get a modern, easy to use, and reliable service capable of integrating with tons of different social identity 
providers (e.g. Facebook, Google, Twitter, etc). Also, if we ever need to integrate with enterprise identity 
providers using protocols like OpenID Connect, SAML, and WS-Federation, don't worry, Auth0's got you covered.

That is, Auth0 can help us focus on what matters the most to us, the special features of our product. 
In addition, Auth0 can improve oour product's security with state-of-the-art features like passwordless, 
breached password surveillance, and multifactor authentication.


    C:\Users\rauna>
    curl --request POST --url https://rkshakya.auth0.com/oauth/token --header "content-type: application/json" --data "{\"client_id\":\"WrsPEivnNQFsfxih5gfy5Eg25ALNlBen\",\"client_secret\":\"lAHyK2wnFdJ__3WtwyfF_iG32JciZ2n8tH1NAkLTr1Ya3TxTSGFlOuaQleWyJz20\",\"audience\":\"https://online-exam.digituz.com.br\",\"grant_type\":\"client_credentials\"}"
    
    Output:
    {"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9EWXdNVGMzUlRVMk9UTTBOa1JCUXpCRU16RTJPVVpGTlRjd1JEWkVRMFl6TkRVek9FTkZOUSJ9.eyJpc3MiOiJodHRwczovL3Jrc2hha3lhLmF1dGgwLmNvbS8iLCJzdWIiOiJXcnNQRWl2bk5RRnNmeGloNWdmeTVFZzI1QUxObEJlbkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9vbmxpbmUtZXhhbS5kaWdpdHV6LmNvbS5iciIsImlhdCI6MTU0MDA5MTkwMiwiZXhwIjoxNTQwMTc4MzAyLCJhenAiOiJXcnNQRWl2bk5RRnNmeGloNWdmeTVFZzI1QUxObEJlbiIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.konS5qLv97Kj3y1w0P2H6KlmNIOIfJBKB6lao22twPyPH8yxccaddUOI8YRJ5Hf80nOl189ue1z5Oqhcm2hqqkv8lnKs-PTUg1jbjunuuD8jzsbtLRUkV1Ob8yBFK9ZrO-lK4PR6evchBS5SWZptqj4DJrl6IHzSgHOR_kAJ9eFr3QAxBnfW-VXVYG51DgrKlo1wtWpm1t36mPSsWZCP3mGdbaSS9PhDT0rKi3KcyVBts6XxHcRouLMMfY0IMOG_ZqM_h52mKtLjgodu81zenMDnylZ-_7fNR5HbMBXEh6Lcij7hHkfEMuCFA2_NAmL7fc31OFaUOLXSf6cww5WV4A","expires_in":86400,"token_type":"Bearer"}
    
    # copy token into env variable
    C:\Users\rauna>
    SET JWT="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9EWXdNVGMzUlRVMk9UTTBOa1JCUXpCRU16RTJPVVpGTlRjd1JEWkVRMFl6TkRVek9FTkZOUSJ9.eyJpc3MiOiJodHRwczovL3Jrc2hha3lhLmF1dGgwLmNvbS8iLCJzdWIiOiJXcnNQRWl2bk5RRnNmeGloNWdmeTVFZzI1QUxObEJlbkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9vbmxpbmUtZXhhbS5kaWdpdHV6LmNvbS5iciIsImlhdCI6MTU0MDA4OTM1MiwiZXhwIjoxNTQwMTc1NzUyLCJhenAiOiJXcnNQRWl2bk5RRnNmeGloNWdmeTVFZzI1QUxObEJlbiIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.vCnYl6JfLFfsTvc1yszTLzg7g3iYsXmoKTHzEpaSsNc1E_-sDPwgjBlC_BZEBLV2HNwIctnUTaxdAV3fSdD_w_l_WI0oEk97mbhR68CvbN394ddfnGhe2OOxI73K-Gf0ZLh5YQZ4PuVBQxA2hn5clLZD_qwvVIW4T0RTyRoBbH_M3IH6UMEtOy0ENm4DjoAEhE9uWfQLfyBFEpEdrNdHm3Y9313RUbrzJWMoXtb98QXr3dKifdqyStIzNO7RPO7NGQKW4StF-mDrwVZsfKqIJLuEp2wWgVTksnb0BDzmulOdp5RAPS2EMYqsofCnDxFmUZzPBsnu7dKWizSdgMjg9g"
    
    # create new exam
    C:\Users\rauna>
    curl -X POST -H "Content-Type:application/json" -H "Authorization:Bearer %JWT%" -d "{\"title\":\"JavaScript Advanced  Exam\",\"description\":\"Tricky questions about JavaScript.\"}" http://127.0.0.1:5000/exams
    
    C:\Users\rauna>
    curl -X POST -H "Content-Type:application/json" -H "Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9EWXdNVGMzUlRVMk9UTTBOa1JCUXpCRU16RTJPVVpGTlRjd1JEWkVRMFl6TkRVek9FTkZOUSJ9.eyJpc3MiOiJodHRwczovL3Jrc2hha3lhLmF1dGgwLmNvbS8iLCJzdWIiOiJXcnNQRWl2bk5RRnNmeGloNWdmeTVFZzI1QUxObEJlbkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9vbmxpbmUtZXhhbS5kaWdpdHV6LmNvbS5iciIsImlhdCI6MTU0MDA4OTM1MiwiZXhwIjoxNTQwMTc1NzUyLCJhenAiOiJXcnNQRWl2bk5RRnNmeGloNWdmeTVFZzI1QUxObEJlbiIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.vCnYl6JfLFfsTvc1yszTLzg7g3iYsXmoKTHzEpaSsNc1E_-sDPwgjBlC_BZEBLV2HNwIctnUTaxdAV3fSdD_w_l_WI0oEk97mbhR68CvbN394ddfnGhe2OOxI73K-Gf0ZLh5YQZ4PuVBQxA2hn5clLZD_qwvVIW4T0RTyRoBbH_M3IH6UMEtOy0ENm4DjoAEhE9uWfQLfyBFEpEdrNdHm3Y9313RUbrzJWMoXtb98QXr3dKifdqyStIzNO7RPO7NGQKW4StF-mDrwVZsfKqIJLuEp2wWgVTksnb0BDzmulOdp5RAPS2EMYqsofCnDxFmUZzPBsnu7dKWizSdgMjg9g" -d "{\"title\":\"TypeScript Advanced  Exam\",\"description\":\"Tricky questions about TypeScript.\"}" http://127.0.0.1:5000/exams
    
    Output:
    {"created_at":"2018-10-21T08:55:24.288517+00:00","description":"Tricky questions about TypeScript.","id":7.0,"last_updated_by":"HTTP post request","title":"TypeScript Advanced  Exam","updated_at":"2018-10-21T08:55:24.288517+00:00"}