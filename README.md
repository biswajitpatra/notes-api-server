# Note-taking application

URL : <https://notes-api-app.herokuapp.com/>

## Endpoints
- Create a new note containing a note title and content
    >`POST` <https://notes-api-app.herokuapp.com/notes>
- Edit the title or content of an existing note
    > `PUT` <https://notes-api-app.herokuapp.com/notes/{id}>
- Get a list of titles along with ids
    > `GET` <https://notes-api-app.herokuapp.com/notes>
- Get a list of titles of all the notes
    > `GET` <https://notes-api-app.herokuapp.com/notes/list_titles>
- Get the title and content of a particular note
    > `GET` <https://notes-api-app.herokuapp.com/notes/{id}>
- Delete a note
   > `DELETE` <https://notes-api-app.herokuapp.com/notes/{id}>


For **JSON** response ,add `/?format=json` at the end of each request
