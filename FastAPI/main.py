from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World yoooooooo"}


@app.get("/allposts")
def get_posts():
    return [{"data": "this is my first post"}, {"data": "this is my second post"}]


@app.post("/post")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"Title: {payLoad['title']} "
                        f"Content: {payLoad['content']}"}
