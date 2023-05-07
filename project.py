import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Prasanna@61')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute('create database Inventory_Management')
cur.execute('use Inventory_Management')
# Create the 'manufacture' table
m='CREATE TABLE manufacture (manufacture_id INTEGER PRIMARY KEY, item_name VARCHAR(20),company varchar(20),item_color VARCHAR(20),quantity INTEGER(4),defective_items INTEGER(4))'
cur.execute(m)
# Create the 'goods' table
g='CREATE TABLE goods (goods_id INTEGER(4) PRIMARY KEY, manufacture_id INTEGER, manufacture_date DATE,FOREIGN KEY(manufacture_id) REFERENCES manufacture(manufacture_id))'
cur.execute(g)

# Create the 'purchase' table
p='CREATE TABLE purchase (purchase_id INTEGER(4) PRIMARY KEY,  store_name varchar(20),purchase_amount FLOAT, purchase_date DATE)'
cur.execute(p)
# Create the 'sale' table
s='CREATE TABLE sale (sale_id INTEGER(4) PRIMARY KEY,store_name VARCHAR(30),sale_date DATE,goods_id INTEGER(4), profit_margin FLOAT,FOREIGN KEY(goods_id) REFERENCES goods(goods_id))'
cur.execute(s)
# insert multiple values into manufacture table
m1='insert into manufacture(manufacture_id ,item_name ,company,item_color ,quantity ,defective_items) values (%s,%s,%s,%s,%s,%s)'
val1 = (1, 'wooden chair','PNR ENTERPRISES' ,'brown', 100, 0), (3, 'wooden table','SS EXPORT' 'Gray', 70, 1),(2, 'red toy','F3 TOYS','red', 250, 0),(4,'Shirt','ADIDAS','black',400,1)
cur.executemany(m1,val1)
mydb.commit()
#Insert multiple entries to the 'goods' table
g1='insert into goods(goods_id , manufacture_id , manufacture_date)values (%s,%s,%s)'
val2 = (1, 1, '2023-04-23'),(2, 1, '2023-04-21'),(3, 2, '2023-04-30'),(4, 3, '2023-04-16')
cur.executemany(g1,val2)
mydb.commit()
# Insert multiple entries to the 'purchase' table
p1='insert into purchase(purchase_id , store_name,purchase_amount,purchase_date)values(%s,%s,%s,%s)'
val3 = (1, 'ORay', 500, '2023-04-30'), (2, 'MyKids', 1000, '2023-04-25'),(3, 'OnlineMart', 750, '2023-04-13')
cur.executemany(p1,val3)
mydb.commit()
# Insert multiple entries to the 'sale' table
s1='INSERT INTO sale(sale_id ,store_name ,sale_date,goods_id , profit_margin )values(%s,%s,%s,%s,%s)'
val4 = (1, 'MyCare', '2023-04-01', 1, 100),(2, 'ORay', '2023-04-03', 2, 50),(3, 'MyKids', '2023-04-05', 3, 75),(4, 'OnlineMart', '2023-04-06', 4, 80)
cur.executemany(s1,val4)
mydb.commit()

#Queries
s='DELETE purchase FROM purchase WHERE item_name = "Shirt" AND purchase_date = "2023-04-01" AND store_name = "ORay"'
cur.execute(s)
mydb.commit()


t='UPDATE manufacture SET quantity = 500 WHERE item_color = "red" AND manufacture_id IN (SELECT manufacture_id FROM goods WHERE goods_id IN (SELECT goods_id FROM sale WHERE store_name = "MyKids")'
cur.execute(t)
mydb.commit()


u='SELECT * FROM  goods JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id WHERE item_name = "wooden chair" AND manufacture_date< "2023-05-01"'
cur.execute(u)
rows=cur.fetchall()
for i in rows:
    print(i)
mydb.commit()

v='SELECT sale.profit_margin FROM sale JOIN goods ON sale.goods_id = goods.goods_id JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id JOIN purchase ON goods.purchase_id = purchase.purchase_id WHERE item_name = "wooden table" AND store_name = "MyCare",company = "SS Export"'
cur.execute(v)
row = cur.fetchone()
print(row[0])
mydb.commit()