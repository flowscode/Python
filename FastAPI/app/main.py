# imports
from random import randrange
from telnetlib import STATUS
from fastapi import FastAPI, Response, status, HTTPException
from app.post import Post

# setting FastAPI app
app = FastAPI()

# in memory db (LIST)
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

# Function to find and delete post
def find_and_delete_post(id):
    for p in my_posts:
        if p["id"] == id:
            my_posts.remove(p)
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                        detail=f"Post with id {id} has been removed")

# function to find and update
def find_and_update_post(id,post: Post):
    for p in my_posts:
        if p["id"] == id:
            id = p.get("id")
            p.update(post)
            p["id"] = id
            raise HTTPException(status_code=status.HTTP_201_CREATED,
                        detail=f"Post with id {id} has been Updated")

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
    
    post.id = randrange(0, 10000000)
    post_dict = post.dict()
    my_posts.append(post_dict)
    raise HTTPException(status_code=status.HTTP_201_CREATED, 
                            detail=post_dict)

# get post depending on ID in url
@app.get("/posts/{id}")
def get_post(id: int):
    
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id {id} was not found")
    return {"Post": post}

# Delete post from list
@app.delete("/posts/{id}")
def delete_post(id: int):
    find_and_delete_post(id)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id {id} was not found")
    
# Update a post in list
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    find_and_update_post(id,post)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id {id} was not found")