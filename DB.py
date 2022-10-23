import sqlite3
class DB:
    def __int__(self,name):
        self.conn = sqlite3.connect(name)
        self.c=self.conn.cursor()
        self.c.execute('''
                  INSERT INTO Product (product_id, product_name)''')

        self.c.execute('''
                  INSERT INTO Discount (Discount_id, Discount_name,Discount_size,product_name)''')
        self.conn.commit()

    def AddDiscount(self,Discount_id, Discount_name,Discount_size,product_name):
        ExecuteValue="INSERT INTO Discount ("+Discount_id+","+Discount_name+","+Discount_size+","+product_name+")"
        self.c.execute(ExecuteValue)
        self.conn.commit()


    def AddProduct(self,product_id, product_name):
        ExecuteValue = "INSERT INTO Discount (" + product_id + "," + product_name +")"
        self.c.execute(ExecuteValue)
        self.conn.commit()