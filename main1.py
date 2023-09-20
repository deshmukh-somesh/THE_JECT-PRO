from fastapi import FastAPI
from typing import Optional 

app =FastAPI()

# query parameters
@app.get('/blog')
def index(limit:int, published:bool , sort:Optional[str]=None):
    # return published
    if published:
     return {'data':f'{limit} published  blogs from the db'}
    else:
      return {'data': f"{limit} blogs from the db"}


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}/comments')

 













# @app.get('/operations')
# def index(limit):
#     return {'data':f'{limit} blogs from the db'}

# @app.get('/operations/add')
# def app1(a:int,b:int):
#     result = a+b
#     return {'addition': f'of 2 numbers is a and b is {result}'}
    
# @app.get('/operations/mul')
# def multi(a:int,b:int):
#     result = a*b
#     return {'multiplication':f'of 2 numbers a and b is {result}'}

# @app.get('/operations/div')
# def div(a:int, b:int):
#     result = a/b
#     return {'division:':f'of 2 numbers a and b is {result}'}

# @app.get('/operations/mod')
# def module(a:int, b:int):
#     result = a % b
#     return {'mudule':f'of 2 number a and b  is {result} '}

# @app.get('/')
# def index():
#     return {'data':'blog list'}


# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data':'all unpublished blogs'}

# @app.get('/blog/{id}')
# def show(id:int):
#     # fetch blog with id 
#     return {'data':id}

# # @app.get('/blog/{blog_name}/{id}')
# # def blog_name(blog_name,id):
# #     return f" your blog name is {blog_name} and id is {id}"

# @app.get('/blog/{id}/comments')
# def comments(id:int):
#     return {id:{'comments':'hi , this is really good post@!!'
#     }, 'post_no':id}

   