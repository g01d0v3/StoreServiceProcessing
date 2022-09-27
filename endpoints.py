from typing import List
import fastapi
from pydantic import BaseModel
from datetime import date

api = fastapi.FastAPI()


class Products(BaseModel):
    product: str
    price: float


class Cheque(BaseModel):
    id: int
    date: date
    products: List[Products]
    provider: str = 'OOO Лысый Group'


# def random_id():
#     return ''.join(random.sample(string.digits, 8))


@api.get('/')
def __home_page():
    return 'Welcome'


@api.get('/{id}', response_model=Cheque)
def __cheque_page(id:  int, check: Cheque):
    return Cheque


@api.get('/products')
def __products_page():
    return "there's will be product list"


