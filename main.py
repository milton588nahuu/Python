from fastapi import FastAPI,Request

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sql_app.database import engine
from sql_app import model
# from sql_app import schemas


app = FastAPI() 


templates = Jinja2Templates(directory="./sql_app/templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/employees",response_class=HTMLResponse)
async def employees(request:Request):
  with engine.connect() as conn:
    lista_by_body = conn.execute(model.Employees.select()).fetchall()
    names_camp = conn.execute(model.Employees.select()).keys()
    name="Employees"
  return templates.TemplateResponse("index.html",{"request":request,
                                                  "name":name,
                                                  "names_camp":names_camp,
                                                  "lista_by_body":lista_by_body})

@app.get("/categories",response_class=HTMLResponse)
def categories(request:Request):
  with engine.connect() as conn:
    lista_by_body = conn.execute(model.categories.select()).fetchall()
    names_camp = conn.execute(model.categories.select()).keys()
    name="Categories"
    
  return templates.TemplateResponse("index.html",{"request":request,
                                                  "name":name,
                                                  "names_camp":names_camp,
                                                  "lista_by_body":lista_by_body})


@app.get("/customers",response_class=HTMLResponse)
def customers(request:Request):
  with engine.connect() as conn:
    lista_by_body = conn.execute(model.Customers.select()).fetchall()
    names_camp = conn.execute(model.Customers.select()).keys()
    name="Customers"
    
  return templates.TemplateResponse("index.html",{"request":request,
                                                  "name":name,
                                                  "names_camp":names_camp,
                                                  "lista_by_body":lista_by_body})

@app.get("/orders",response_class=HTMLResponse)
def orders(request:Request):
  with engine.connect() as conn:
    lista_by_body = conn.execute(model.Orders.select()).fetchall()
    names_camp = conn.execute(model.Orders.select()).keys()
    name="Orders"
    
  return templates.TemplateResponse("index.html",{"request":request,
                                                  "name":name,
                                                  "names_camp":names_camp,
                                                  "lista_by_body":lista_by_body})


@app.get("/orderdetails",response_class=HTMLResponse)
def orderdetailss(request:Request):
  with engine.connect() as conn:
    lista_by_body = conn.execute(model.OrderDetails.select()).fetchall()
    names_camp = conn.execute(model.OrderDetails.select()).keys()
    name="Orderdetails"
    
  return templates.TemplateResponse("index.html",{"request":request,
                                                  "name":name,
                                                  "names_camp":names_camp,
                                                  "lista_by_body":lista_by_body})


@app.get("/products",response_class=HTMLResponse)
def products(request:Request):
  with engine.connect() as conn:
    lista_by_body = conn.execute(model.Products.select()).fetchall()
    names_camp = conn.execute(model.Products.select()).keys()
    name="Products"
    
  return templates.TemplateResponse("index.html",{"request":request,
                                                  "name":name,
                                                  "names_camp":names_camp,
                                                  "lista_by_body":lista_by_body})

@app.get("/shippers",response_class=HTMLResponse)
def shippers(request:Request):
  with engine.connect() as conn:
    lista_by_body = conn.execute(model.Shippers.select()).fetchall()
    names_camp = conn.execute(model.Shippers.select()).keys()
    name="Shippers"
    
  return templates.TemplateResponse("index.html",{"request":request,
                                                  "name":name,
                                                  "names_camp":names_camp,
                                                  "lista_by_body":lista_by_body})

@app.get("/suppliers",response_class=HTMLResponse)
def suppliers(request:Request):
  with engine.connect() as conn:
    lista_by_body = conn.execute(model.Suppliers.select()).fetchall()
    names_camp = conn.execute(model.Suppliers.select()).keys()
    name="Suppliers"
  
    return templates.TemplateResponse("index.html",{"request":request,
                                                  "name":name,
                                                  "names_camp":names_camp,
                                                  "lista_by_body":lista_by_body})


@app.get("/query",response_class=HTMLResponse)
async def query(camp:str,table:str,request:Request):
    names_camp = []
    names_camp.append(camp)  
    with engine.connect() as conn:
      
      lista_by_body = conn.execute(f"SELECT {camp} FROM {table}").fetchall()
      name= table
      

    return templates.TemplateResponse("index.html",{"request":request,
                                                      "name":name,
                                                      "names_camp":names_camp,
                                                      "lista_by_body":lista_by_body})






