Design philsophy:
Goal is to make this as flat and simple as possible to hit task requirements. Docker-complose sets up two containers: assessment4_db with the database craigslist_db in it and assesment4_api to establish locahost server to interface with database. 

Models and endpoints are established in the listings app, which is kept in the parent directory adjacent to the docker-compose.yml etc. I used this structure to reduce the chances of improper changes and migrations as well as improved modularity and clarity of organization in the case that I decide to take the structure and expand it for a later project.


Listings App Structure:
|---categories_model
|   |---GET all categories
|   |---POST new category
|   |---PUT /update a category
|   |---DELETE a category
|---posts_model
|   |---GET all posts within a category
|   |---POST new post within a category
|   |---PUT /update a post within a category
|   |---DELETE a post within a category