# Articuno-Coding-Intern-Assignment

<h3> Instructions for setting up and running the API: </h3>
- Install Flask,Flask-SQLAlchemy, psycopg2 and PostgreSQL.
- Create a new Flask project and a new PostgreSQL database.
- In the PostgreSQL database, create two tables: one for messages and one for likes.
- In the messages table, include columns for the message text, the user who posted it, and the timestamp.
- In the likes table, include columns for the message ID, the user who liked it, and the timestamp.
- Use Flask to create routes for creating and querying messages and likes.
- Use PostgreSQL triggers to automatically update the "likes" count for a message whenever a new like is added or removed.
- Run the following command to create the tables in the database: db.create_all().
- Start the application by running 'flask run' command
