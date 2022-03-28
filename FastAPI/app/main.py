# Run this to start the server - uvicorn app.main:app --reload

# imports
from random import randrange
from telnetlib import STATUS
from fastapi import FastAPI, Response, status, HTTPException
from app.post import Post
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# setting FastAPI app
app = FastAPI()

# db Setup
while True:
    
    try:
        conn = psycopg2.connect(host="localhost",
                                database="fastapi", 
                                user='postgres', 
                                password='password',
                                cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)    
        time.sleep(2)

# root mapping
@app.get("/")
def root():
    
    return {"message": "Hello World yoooooooo"}

#################################### GET ALL posts Get mapping
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    return [{"Posts": posts}]

#################################### CREATE post with Post mapping
@app.post("/posts")
def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"Data": new_post}
    
################################### GET 1 POST depending on ID in url
@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id {id} was not found")
    return {"Post": post}
    

################################## DELET post from db
@app.delete("/posts/{id}")
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """,(str(id),))
    deleted_post=cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=F"{id} DELETED!!!")
        
    
    
################################# UPDATE a post db
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,(post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if update_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    raise HTTPException(status_code=status.HTTP_201_CREATED,
                        detail=f"Post with id {id} has been Updated")