Simple chatting application made using Django. Here users are added to some groups. User can send a query in that group, reply to a query and can reply to a reply as well. We have used two models Groups and Messages and for stroing user details we have used the default user model of the django framework. One for group which has a many to many relation with the User model. The message group has a foreign key relation with the Group model which tells that from which group this message belong. There is another foreign key linking between User model and Messages model which tells that from which user sent this message. Then for implementing reply part, we have created a foreign key self linking field which is null by default. If a user reply to some message then that message get linked to the replied message throgh the reply field. The replied message will contain the foreign key reference to the message for which it has been replied. 

We also have made UI for the project. The first page will be a login page and when user login he will be taken to chatting home page which will contain all his groups and messages. He can send a new message to the groups or can reply to any message.

## Credentials 

We have seven users with there own username and password. For testing purpose you can use the following credentails

<ul>
<li> Username - rajat
<li> Password - mapple1205
</ul>
Rest of the usernames are - 
<ul>
<li> isha
<li> anushka
<li> ranjan
<li> arora
<li> agarwal
<li> luv
<li> mayank
<li> abhinay
</ul>
The password for all the accounts is same <strong>mapple1205</strong>

# Steps to install dependency

Python 3.x should be installed
```
pip install -r requirements.txt
```


# Steps to run the project

``` 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Steps to view project

<ol>
<li> After running the project visit <strong>127.0.0.1:8000</strong>
<li> Use the credential with username <strong> rajat </strong> to login.
<li> Chatting home page will be displayed. You can send message to any group and can reply to any messages as well.
<li> To login into another account, first logout and then use any of the registed user to login again.
</ol>
<br><br>
<hr>
<center> Made with 💓 by <a href="https://itsrajat.xyz">Rajat Shrivastava</a>
