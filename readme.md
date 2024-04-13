

# Product Requirements Documentation

| Field | Detail |
| ----- | ------ |
| Project Name |  Content Management System |
| Description |  CMS to publish articles and read artiles and blogs  |
| Developer |   Izzy Zinxhirija   |
| Live Website | TBD  |
| Repo |  https://github.com/Izzy-2023/seir-seal-capstone-backend |

## Problem being solved and Target Market

This CMS app is a modern content management system designed to address the common challenges faced by individual content creators and small businesses. This tool will provide users the ability to create and manage content using a user friendly interface. 

## Dependencies
- dj-database-ur
- psycopg2-binary
- django-environ
- apollo client

## ERD Diagram

| Article |
| ------- |
| id (PK) |
| title   |
| body    |
| published_date |


## Route Name

| Route Name | Endpoint |	Method | Description |
| --------- | -------- | ------ | ----------- |
| Fetch Articles | /graphql/ | POST | Retrieves a list of all articles. |
| Fetch Article	| /graphql/	| POST	| Retrieves a single article by its ID. |
| Create Article | /graphql/ | POST	| Creates a new article with provided title and body. |
| Update Article | /graphql/ | POST	| Updates an existing article by ID with new data. |
| Delete Article | /graphql/ |POST	| Deletes an existing article by its ID. |