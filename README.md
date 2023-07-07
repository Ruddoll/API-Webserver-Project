# Web Server README


## Problem Statement


The problem being addressed by this application is the need for a web server that allows users to create and manage posts. The application aims to provide a platform for users to share their thoughts, ideas, and experiences through posts, while also providing functionality for users to interact with and comment on each other's posts.


## Why is it a Problem?


In today's digital age, there is a growing demand for platforms that facilitate content sharing and user engagement. By building this web server, we aim to address the need for a user-friendly and efficient system that enables users to create and manage posts easily. This application seeks to enhance user experiences by providing a centralized platform for sharing and engaging with content.


## Database System - SQLite


For this web server, we have chosen SQLite as the database system. SQLite is a reliable and lightweight relational database management system (RDBMS) that is well-suited for small to medium-sized applications. It offers the advantage of being serverless and file-based, making it easy to set up and manage.


Drawbacks Compared to Others:


1. Scalability: Compared to more robust database systems like MySQL or PostgreSQL, SQLite may have limitations in handling large-scale applications with high concurrency and heavy write loads.


2. Advanced Features: SQLite has a simplified feature set compared to other database systems. It may lack some advanced functionalities such as stored procedures, triggers, or fine-grained access control.


## Key Functionalities and Benefits of an ORM


ORM (Object-Relational Mapping) is a key component of this web server application. It provides several functionalities and benefits, including:


1. Simplified Database Interaction: ORM abstracts away the complexities of interacting with the underlying database. It allows developers to work with objects and classes, reducing the need to write raw SQL queries.


2. Database Agnostic: ORM frameworks provide a layer of abstraction that enables the application to work with different database systems without significant code changes. This flexibility allows for easy migration between database platforms.


3. Model-View-Controller (MVC) Structure: ORM promotes the separation of concerns by following the MVC architectural pattern. It helps maintain a clear separation between the database models, business logic, and presentation layer of the application.


4. Data Integrity and Validation: ORM frameworks often provide built-in mechanisms for data validation and integrity checks. This helps ensure that data stored in the database follows the defined rules and constraints.


5. Efficient Query Generation: ORM frameworks generate optimized SQL queries based on the defined models and relationships. This improves performance by reducing unnecessary database round trips.


## API Endpoints


The following endpoints are available in the API:


- `GET /posts`: Retrieves a list of all posts.
- `GET /posts/:id`: Retrieves a specific post by its ID.
- `POST /posts`: Creates a new post.
- `PUT /posts/:id`: Updates an existing post.
- `DELETE /posts/:id`: Deletes a post.
- `GET /comments`: Retrieves a list of all comments.
- `GET /comments/:id`: Retrieves a specific comment by its ID.
- `POST /comments`: Creates a new comment.
- `PUT /comments/:id`: Updates an existing comment.
- `DELETE /comments/:id`: Deletes a comment.


Please refer to the API documentation for detailed information on required data and expected responses for each endpoint.


## Entity Relationship Diagram (ERD)


```
       +--------------+        +-------------+
       |    User      |        |    Post     |
       +--------------+        +-------------+
       | id (PK)      |        | id (PK)     |
       | name         |        | title       |
       | email        |        | content     |
       +--------------+        | user_id (FK)|




                               +-------------+
```


## Third-Party Services


This application utilizes the following third-party services:


1. Authentication Service: We will integrate a third-party authentication service, such as OAuth or JWT, to handle user authentication and authorization.


2. Email Service: We will utilize a third-party email service, like SendGrid or Mailgun, to enable email notifications for user actions, such as new post notifications or comment replies.


## Models and Relationships


The application consists of the following models:


1. User: Represents a user of the application. It has attributes such as id, name, and email. A user can have multiple posts.


2. Post: Represents a post created by a user. It has attributes such as id, title, content, and user_id. A post belongs to a specific user. A post can have multiple comments.


3. Comment: Represents a comment made on a post. It has attributes such as id, content, post_id, and user_id. A comment belongs to a specific post and user.


## Database Relations


The database relations to be implemented in this application are as follows:


- One-to-Many: User has a one-to-many relationship with Post. A user can have multiple posts, but a post belongs to a single user.


- One-to-Many: Post has a one-to-many relationship with Comment. A post can have multiple comments, but a comment belongs to a single post.


## Task Allocation and Tracking


Tasks in this project will be allocated and tracked using an Agile methodology, specifically the Scrum framework. The development process will consist of short iterations called sprints, typically lasting one to two weeks. The team will hold daily stand-up meetings to discuss progress, challenges, and task assignments.


We will use project management tools like Trello or Jira to create and manage a backlog of tasks. Each task will be assigned to team members with estimated timeframes. Progress will be tracked through regular updates on the task board, and any impediments or issues will be addressed promptly.


The team will also conduct periodic retrospectives to reflect on the progress, identify areas of improvement, and make necessary adjustments to ensure the successful completion of the project.