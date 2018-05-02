Operationalizing Python ML models in a web app using Flask - K. Narayana Swamy

Tuesday, May 3, 2016
7:00 PM to 10:00 PM
Donald Danforth Plant Science Center
975 North Warson Road · Saint Louis, MO

How to find us

Library on the floor above the entry

The demonstration will show how machine learning models built in Python can be operationalized in a web application using Flask. The example will use a Beer Recommender model built in Python using a cosine similarity approach. The Recommendation model will be pickled after it is built using historical Beer user reviews data. A Restful Flask app will be built in a AWS Ubuntu machine and this Ubuntu machine will also be hosting a PHP based web application using the apache web server and a MySql database. The Restful Flask app will load the pickled recommendation model and will be listening on port 8081 (any port other than 80 can be chosen). A mod_wsgi module and a mod_wsgi file will be needed for apache web server to communicate with python. The web application will ping the Flask app at the listening port to retrieve the recommended beers based on the user input of liked beers on the web application interface. All the pieces of operationalizing the recommender model will be demonstrated. The implementation uses fully open source tools and one AWS EC2 t2.micro instance.

K. Narayana Swamy has a long experience building web applications in PHP and has recently been working on using Python to build machine learning models. He is a Finance Manager and leads the data analytics group at the Doe Run company that comprises both visual analytics and advanced analytics of operations data. He has a Ph.D in engineering and a MBA from Washington University. He is a co-founder of a local startup called runiq.com.
