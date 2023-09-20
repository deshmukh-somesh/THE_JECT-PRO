from fastapi import FastAPI

app =FastAPI()

@app.get('/about')
def about():
    return {'data':{'name':'deshmukh','address':'Latur,Maharashtra'}}


@app.get('/')
def home():
    return f"you are on home page!"

@app.get('/contact')
def contact():
    return {'contact':'9588466392'}

    