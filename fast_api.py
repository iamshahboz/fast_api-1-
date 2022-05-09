from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel



application = FastAPI()

'''In order to be able to write api. Make sure that you have understandings of HTTP resonses
GET: to get data,
POST: to sent or create a data,
UPDATE: to update data,
DELETE: to delete data
PATCH: to change the specific value 
'''
books = {
    1: {
        "name": "Rich Dad Poor Dad",
        "author":"Robert Kiyosaki",
        "published": 2017,
        "price": 27
    },
    2: {
        "name": "A promised land",
        "author": "Barak Obama",
        "published": 2020,
        "price": 18
    },
    3: {
        "name": " Cross Country",
        "author": "James Patterson",
        "published": 2008,
        "price": 10
    }


}

class Books(BaseModel):
    name: str
    author: str
    published: int
    price: int

class UpdateBook(BaseModel):
    name : Optional[str]= None
    author: Optional[str] = None
    published: Optional[int] = None
    price: Optional[int] = None




@application.get("/")
def myapi():
    return {"Hooray":"I created first api with Fast API"}

@application.get("/get-book/{book_id}")
def get_book(book_id:int=Path(None,description="The id of the book you want to view",gt=0,lt=50)):
    return books[book_id]


'''for description you can add 
gt-greater than
lt-less than
ge-greter or equal
le-less or equal'''

@application.get("/get-by-name")
def get_book(name: Optional[str]=None):
    for book_id in books:
        if books[book_id]["name"]==name:
            return books[book_id]
    return {"Book with this name":"has not been found"}

@application.post("/new-book/{book_id}")
def new_book(book_id: int, book:Books):
    if book_id in books:
        return {"Error":"This book already exists"}

    books[book_id] = book
    return books[book_id]

@application.put("/update-book/{book_id}")
def update_book(book_id:int,book:UpdateBook):
    if book_id not in books:
        return {"Error":"No book with this id"}

    if book.name !=None:
        books[book_id].name = book.name

    if book.author !=None:
        books[book_id].author = book.author

    if book.published !=None:
        books[book_id].published = book.published
    
    if book.price !=None:
        books[book_id].price = book.price
    
    return books[book_id]

@application.delete("/delete-book/{book_id}")
def delete_book(book_id:int):
    if book_id not in books:
        return{"Error":"there is no such a book"}
    del books[book_id]
    return {"Message":"book has been deleted successfuly"}
    

    
   









    



