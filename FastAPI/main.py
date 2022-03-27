# imports
from random import randrange
from fastapi import FastAPI
from fastapi import Response
from post import Post

# setting FastAPI app
app = FastAPI()
my_posts = [
            {"title": "title of post 1",
            "content": "content of post 1",
            "id": 1},
            
            {"title": "fave car",
             "content": "BMW",
             "id": 2}
        ]

# function to iterate throught list to find post based on id passed to the function
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

# root mapping
@app.get("/")
def root():
    return {"message": "Hello World yoooooooo"}

# get all posts Get mapping
@app.get("/posts")
def get_posts():
    return [{"Posts": my_posts}]

# create post with Post mapping
@app.post("/posts")
def create_post(post: Post):
    if my_posts[0] == "PLACEHOLDER":
        my_posts.remove("PLACEHOLDER")
    post.id = randrange(0, 10000000)
    post_dict = post.dict()
    my_posts.append(post_dict)
    return {"Post": post_dict}

# get post depending on ID in url
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    print(post)
    if not post:
        response.status_code = 404
        response.body = f"Post with id {id} was not found"
        return {"Response": [
            {"Status Code": response.status_code},
            {"Body": response.body},
        ]}
    return {"Post": post}
