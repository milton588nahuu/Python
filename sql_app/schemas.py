from pydantic import BaseModel
from datetime import date

class Categories(BaseModel):
    CategoryID:int
    CategoryName:int
    Description:str
    class Config:
      orm_mode = True

class Customer(BaseModel):
    CustomerID:int
    CustomerName:str
    ContactName:str
    Address:str
    City:str
    PostalCode:str
    Country:str
    class Config:
      orm_mode = True

class Employees(BaseModel):
    EmployeeID:int
    LastName= str
    FirstName= str 
    BirthDate= date
    Photo= str
    Notes= str
    class Config:
      orm_mode = True

class Shippers(BaseModel):
  ShipperID:int
  ShipperName:str
  Phone:int

class Suppliers(BaseModel):
  SupplierID:int
  SupplierName:str
  ContactName:str
  Address:str
  City:str
  PostalCode:str
  Country:str
  Phone:str
  
class Products(Categories,Shippers):
  ProductID:int
  ProductName:str
  SupplierID: Shippers
  CategoryID: Categories
  Unit:str
  Price:int
  
class Orders(Shippers,Employees,Customer):
  OrderID:int
  CustomerID:Customer
  EmployeeID:Employees
  OrderDate:date
  ShipperID:Shippers
  
class OrderDetails(Orders,Products):
  OrderDetailID:int
  OrderID:Orders
  ProductID:Products
  Quantity:int