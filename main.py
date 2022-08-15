'''
Author: Mecil Meng
Date: 2022-06-14 12:44:16
LastEditors: Mecil Meng
LastEditTime: 2022-08-15 11:57:58
FilePath: /Full_course/main.py
Description:

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from app.config import settings
from app.database import engine
from app.routers import auth, post, user, vote

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# my_posts = [
#     {
#         "title": "title of post 1",
#         "content": "content of post 1",
#         "published": True,
#         "id": 1
#     },
#     {
#         "title": "title of post 2",
#         "content": "content of post 2",
#         "published": False,
#         "id": 2
#     },
# ]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i

app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)


@app.get('/')
async def index():
    return {"message": "Hello World"}
