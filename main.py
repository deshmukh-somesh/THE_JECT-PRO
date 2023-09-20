#import 
from fastapi import FastAPI
 #instance
app = FastAPI()

#decorate
@app.get('/')
#function
def hello():
    return {'data':{'name':'somesh'}}

    