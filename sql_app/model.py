from sqlalchemy import Column,Table,Integer, String,Date,ForeignKey
from sql_app.database import engine,meta as meta_data

categories = Table("Categories",meta_data,
    Column("CategoryID",Integer, primary_key=True,autoincrement=True),
    Column("CategoryName",String(255)),
    Column("Description",String(255)))

Customers=Table("Customers",meta_data,
    Column("CustomerID",Integer, primary_key=True,autoincrement=True),
    Column("CustomerName",String(255)),
    Column("ContactName",String(255)),
    Column("Address",String(255)),
    Column("City",String(255)),
    Column("PostalCode",String(255)),
    Column("Country",String(255))
)


Employees = Table("Employees",meta_data,
    Column("EmployeeID",Integer, primary_key=True,autoincrement=True),
    Column("LastName",String(255)),
    Column("FirstName",String(255)),
    Column("BirthDate",Date),
    Column("Photo",String(255)),
    Column("Notes",String(255))
)


OrderDetails =Table("OrderDetails",meta_data,
    Column("OrderDetailID",Integer, primary_key=True,autoincrement=True),
    Column("OrderID",Integer,ForeignKey("Orders.OrderID")),
    Column("ProductID",Integer,ForeignKey("Products.ProductID")),
    Column("Quantity",Integer)
)
    
    

Orders=Table("Orders",meta_data,
    Column("OrderID",Integer,primary_key=True,autoincrement=True),
    Column("CustomerID",Integer,ForeignKey("Customers.CustomerID")),
    Column("EmployeeID",Integer,ForeignKey("Employees.EmployeeID")),
    Column("OrderDate",Date),
    Column("ShipperID",Integer,ForeignKey("Shippers.ShipperID"))
    )
    
    
Products= Table("Products",meta_data,
    Column("ProductID",Integer,primary_key=True,autoincrement=True),
    Column("ProductName",String(255)),
    Column("SupplierID",Integer,ForeignKey("Suppliers.SupplierID")),
    Column("CategoryID",Integer,ForeignKey("Categories.CategoryID")),
    Column("Unit",String(255)),
    Column("Price",Integer,default=0)
                )
    


Shippers=Table("Shippers",meta_data,
    Column("ShipperID",Integer,primary_key=True,autoincrement=True),
    Column("ShipperName",String(255)),
    Column("Phone",Integer))

Suppliers=Table("Suppliers",meta_data,
    Column("SupplierID",Integer,primary_key=True,autoincrement=True),
    Column("SupplierName",String(255)),
    Column("ContactName",String(255)),
    Column("Address",String(255)),
    Column("City",String(255)),
    Column("PostalCode",String(255)),
    Column("Country",String(255)),
    Column("Phone",String(255)))

meta_data.create_all(engine)