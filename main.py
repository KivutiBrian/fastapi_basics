from fastapi import FastAPI, Body
from typing import Optional


# custom imports
from schema import detail_schema

# obj
app = FastAPI()

details = []

def add_two_numbers(num: int, num2: int) -> int:
    return num+num2


@app.get('/')
def home():
    return {"message":"Learning FastAPI"}


@app.get('/name/awesome/asd')
def name():
    return {"name": "Kivuti Brian"}

# PATH PARAMETERS
# /name/<Fahad>
# /name/<Kivuti>
@app.get('/name/{first_name}')
def unique_name(first_name: str):
    return {"data": first_name}


@app.get('/age/{number}')
def unique_name(number: int):
    return {"data": number}


@app.get('/weight/{number}')
def unique_name(number: float):
    return {"data": number}

# QUERY PARAMETERS
@app.get('/test')
def home(test_value: Optional[str] = None):
    if test_value:
        return {"result":test_value}

    return {"result":"Just testing, no query passed"}

@app.get('/details')
def get_details():
    return {
        "data": details
    }


@app.post('/details',
summary="post details basdasfd asdasdfjklansdfaed ad",
response_model= detail_schema.BaseDetail,
status_code=201
)
def post_details(detail: detail_schema.BaseDetail):
    details.append(detail)
    return detail


"""
HTTP METHOD
*GET
*POST
*PUT/PATCH
*DELETE

1xx - informational
2xx - success
3xx - redirects
4xx - client error
5xx - Server error

"""

# @app.post('/details')
# def post_details(
#     first_name: str = Body(...),
#     last_name: str = Body(...),
#     phone_number: str = Body(...),
#     age:int = Body(...) 
# ):
#     details.append(
#         {
#             "first":first_name,
#             "last": last_name,
#             "phone_number": phone_number,
#             "age": age
#         }
#     )
#     return {
#         "data": details
#     }



# REQUEST BODY -> POST REQUEST
# FORM DATA
# REQUEST FILE
# DB CONNECTION -> Mongo/Postgres/sqlite
# 









