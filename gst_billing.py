# view products
# def view() - see all the records

# searching a product
# def search() - search a product

# customer details
# cust_search() -  searches the records of a customer

# updating the stock
# def add() - adding products
# def delete() - deleting products
# def qty() - updating quantity
# def rate() - updating rate
# def gst() - updating gst

# view sales for a period 
# def sales() - see the sale for a paticular period


import mysql.connector as sql
mycon = sql.connect(host = <host_name> , user = <user>, password = <password>, database = "gst")
cursor = mycon.cursor()


'''
# CONNECTION INFORMATION

# database = "gst"

# CONNECTING TO THE DATABASE
# connect() establishes database connection 
mycon = sql.connect(host = <host_name> , user = <user>, password = <password>, database = "gst")

if mycon.is_connected():
    print("Successfully connected to database!\n ")

#cursorobject = connectionobject.cursor()    creates a cursor and stores data of the table in cursor object
cursor = mycon.cursor()
'''

 
# =============================================================================
#                      To see all the products in stock
# =============================================================================
def view():

    print ("\nSTOCK\nThe Stock available is :\n")
    cursor.execute("select * from Stock")
    data = cursor.fetchall()   # takes the stored data from cusor object 
    for row in data:           # takes all the data from each row
        print("Product Name: ", row[0])
        print("Product Code: ", row[1])
        print("Brand: ", row[2])
        print("Specifications: ", row[3])
        print("Quantity: ", row[4])
        print("Rate_in_Rs: ", row[5])
        print("Discount Available: ", row[6])
        print("GST: ", row[7])
        print("\n")

# =============================================================================
#                      To see the sales between a period
# =============================================================================
        
def sales():
    
    print("Enter the period (YYMMDD) for which you want to see the sale. ")
    period_from = input("\nFrom : ")
    period_to = input("To : ")

    sales = "select * from Sale where Date between %s and %s" %(period_from,period_to)

    cursor.execute(sales)
    data = cursor.fetchall()
    
    for row in data:
        print("\nDate: ", row[0])
        print("Time: ", row[1])
        print("Customer Name: ", row[2])
        print("Mobile Number: ", row[3])
        print("Invoice No.: ", row[4])
        print("Items Purchased: ", row[5])
        print("Amount Paid: ", row[6])
        print("\n")
  
  
# =============================================================================
#                      To add product(s) in stock
# =============================================================================

def add():
 
    count = int(input("Enter the number of products to be added : "))

    # inserting into the table
    for i in range (count):
        st = "insert into Stock(Product_Name,Product_Code,Brand,Specifications,Quantity,Rate_in_Rs,Discount_Available,GST) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        
        Product_Name = input("Enter the Product Name :")
        Product_Code = input("Enter the Product Code :")
        Brand = input("Enter the Brand :")
        Specifications = input("Enter the Specifications (each spec separated by '|' :")
        Quantity = int(input("Enter the Quantity :"))
        Rate_in_Rs = float(input("Enter the Rate (in Rs.) :"))
        Discount_Available = input("Enter the Discount Available :")
        GST = input("Enter the GST :")

        row =(Product_Name,Product_Code,Brand,Specifications,Quantity,Rate_in_Rs,Discount_Available,GST)  # stores all the inputs in the form of a tuple
        #print (row)
        
        cursor.execute(st,row)   # executes the SQL statement
        mycon.commit()    # commit is written so that changes(insertion/deletion) reflect in the database

        print("\nRecord inserted successfully.")

# =============================================================================
#                      To delete product(s) in stock
# =============================================================================

def delete():
   
    count = int(input("Enter the number of products to be deleted : "))
    
    for i in range (count):
        p_name = input("Enter the product name to be deleted from stock : ")
        delete = "DELETE from Stock where Product_Name = '%s'" %(p_name)   # deletes the product 

        cursor.execute(delete)
        mycon.commit()
    print("\nRecord deleted.")
# =============================================================================
#                      To update the quantity of product
# =============================================================================
def qty():
    
    p_name = input("Enter the product to be updated : ")
    new_qty = input("Enter the new quantity : ")
    
    update = "UPDATE Stock set Quantity = '%s' where Product_Name = '%s'" %(new_qty,p_name)  # changes the quantity of the product
    cursor.execute(update)
    mycon.commit()

    print ("Quantity updated.")

# =============================================================================
#                      To update the rate of product
# =============================================================================
def rate():
    
    
    p_name = input("Enter the product name to be updated : ")
    new_rate = input("Enter the new rate : ")
    
    update = "UPDATE Stock set Rate_in_Rs = '%s' where Product_Name = '%s'" %(new_rate,p_name)  # changes the rate of the product
    cursor.execute(update)
    mycon.commit()

    print ("Rate updated.")

# =============================================================================
#                      To update the GST of product
# =============================================================================

def gst():
        
    p_name = input("Enter the product name to be updated : ")
    new_gst = input("Enter the new GST : ")
    
    update = "UPDATE Stock set GST = '%s' where Product_Name = '%s'" %(new_gst,p_name)  # changes the GST on the product
    cursor.execute(update)
    mycon.commit()

    print ("GST updated.")
    
# =============================================================================
#                      To search a product in the stock
# =============================================================================

def search():
        
    p_name = input("Product Name : ")

    name = "select Product_Name from Stock"
    cursor.execute(name)
    data = cursor.fetchall()
    in_stock =[]
    
    for row in data:
        row1 = (list(row))
        for i in row1 :
            in_stock.append(i)
    if p_name in in_stock :
        search = "select * from Stock where Product_Name = '%s'"%(p_name)
        cursor.execute(search)
        data = cursor.fetchall()   # takes the stored data from cusor object 
        for row in data:           # takes all the data from each row
            print("\nThe details are as follows : ") 
            print("\nProduct Name: ", row[0])
            print("Product Code: ", row[1])
            print("Brand: ", row[2])
            print("Specifications: ", row[3])
            print("Quantity: ", row[4])
            print("Rate_in_Rs: ", row[5])
            print("Discount Available: ", row[6])
            print("GST: ", row[7])
            print("\n")

    else :
        print("\nNo such product found. \n")
  
# =============================================================================
#                      To search the customre details 
# =============================================================================
def cust_search():
    
    cust_mobile_no = int(input("Mobile Number : "))
    
    name = "select Mobile_No from Sale"
    cursor.execute(name)
    data = cursor.fetchall()
    in_sale =[]
    
    for row in data:
        row1 = (list(row))
        for i in row1 :
            in_sale.append(i)
      
    if (cust_mobile_no in in_sale) :
        search = "select * from Sale where Mobile_No = '%s'"%(cust_mobile_no)
        cursor.execute(search)
        data = cursor.fetchall()   # takes the stored data from cusor object 
        for row in data:           # takes all the data from each row
            print("\nThe customer details are as follows : ") 
            print("\nCustomer Name: ", row[2])
            print("Mobile Number: ", row[3])
            print("Date: ", row[0])
            print("Time: ", row[1])
            print("Invoice Number: ", row[4])
            print("Items Purchased: ", row[5])
            print("Total Amount Paid: ", row[6])
            print("\n")
    else :
        print("\nNo records found. \n")

        
# =============================================================================
#                      To generate a GST Invoice
# =============================================================================
def bill():
    
    # invoice
    import datetime
    import random
    from tabulate import tabulate
    import mysql.connector as sql
    import pytz
    
    # shop details and date
    shop_name = "\t\t                                   ABC ELECTRONICS                  "
    shop_address = "C-58,Gandhi Road\n\t  New Delhi\n\t  Delhi - 1100XX"
    gst_no = "0123456789"
    email = "abc@helpdesk.com"
 
    date = datetime.date.today()
  
    # using now() to get current time
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).time()
    invoice_no = random.randint(10000,99999)
 
    print("\n                                                       INVOICE                                                 ")
    print(shop_name)
    print("_______________________________________________________________________________________________________________")
    print("ADDRESS :",shop_address)
 
    print("GST NO. :",gst_no,end="                                                               ")
    print("DATE :",date)
 
    print("E-MAIL : ",email,end ="                                                         ")
    print("INVOICE NO. :",invoice_no)
    print("_______________________________________________________________________________________________________________\n")
 
 
    # customer details
    customer_name = input("CUSTOMER NAME : ")
    mobile_no = input("MOBILE NO. : ")
    length = len(mobile_no)
    if (length < 10):
        print("Invalid mobile number ! Enter the correct number. ")
        mobile_no = input("MOBILE NO. : ")
               
    #print("_______________________________________________________________________________________________________________\n")
    
   
    name = "select Product_Name from Stock"
    cursor.execute(name)
    data = cursor.fetchall()
    in_stock =[]
    
    for row in data:
        row1 = (list(row))
        for i in row1 :
            in_stock.append(i)
    #print("\n",in_stock)

    
    final_amt = 0
    dic = {}
    flag = "y"
    list1 = []
    while(flag == "y" or flag == "Y"):

        # takes the value to product name and quantity purchased
        p_name = input("\nEnter the product name : ")
        quantity = int(input("Enter the quantity : "))

        qty1 = "select Quantity from Stock where Product_Name LIKE ('%s')"%(p_name)
        cursor.execute(qty1)
        data = cursor.fetchall()
        for row in data:
            for row1 in row:
                qty = int(row1)
            #print(qty)

                
        # checks if the product entered is in the stock or not
        
        if p_name in in_stock :
            if (qty == 0 or qty <0) :
                print("\nOUT OF STOCK !")
                
            else :
                # fetches the Rate from the table Stock
                price = "select Rate_in_Rs from Stock where Product_Name LIKE ('%s')" %(p_name)
                cursor.execute(price)
                data = cursor.fetchall()
                for row in data:
                    for row1 in row:
                        rate = int(row1)    # prints the Rate as an integer
                    #print(rate)
                        
                # fetches the Product Code from the table Stock
                code = "select Product_Code from Stock where Product_Name LIKE ('%s')" %(p_name)
                cursor.execute(code)
                data = cursor.fetchall()
                for row in data:
                    for row1 in row:
                        code1 = row1
                    #print(code1)
                        
                # fetches the Discount Available from the table Stock        
                discount = "select Discount_Available from Stock where Product_Name LIKE ('%s')"%(p_name)
                cursor.execute(discount)
                data = cursor.fetchall()
                for row in data:
                    for row1 in row:
                        dis = int(row1)
                    #print(dis)
                        
                # fetches the GST(%) from the table Stock
                gst = "select GST from Stock where Product_Name LIKE ('%s')"%(p_name)
                cursor.execute(gst)
                data = cursor.fetchall()
                for row in data:
                    for row1 in row:
                        GST = int(row1)
                    #print(GST)
                        
                # calculation for the amount 
                discounted_price = ((rate*quantity)-dis)
                gst_amount =(discounted_price*GST)/100
                amount = gst_amount + discounted_price

                print("Amount = ",amount)

                # decreasing the quantity in the Stock table after product is purchased
                qty1 = "select Quantity from Stock where Product_Name LIKE ('%s')"%(p_name)
                cursor.execute(qty1)
                data = cursor.fetchall()
                for row in data:
                    for row1 in row:
                        qty = int(row1)
                        
                new_qty = qty - quantity
                update = "UPDATE Stock set Quantity = '%s' where Product_Name = '%s'" %(new_qty,p_name) 
                cursor.execute(update)
                mycon.commit()

                # calculates the total amount to be paid
                final_amt += amount

                # stores items purchased by the customer in the form of dictionary
                dic[p_name] = quantity

                #print(code1,p_name,qty,rate,dis,GST,amount)
                list2 = [code1,p_name,quantity,rate,dis,GST,amount]
                list1.append(list2)
                
                flag = input("\nDo you want to enter more products ? y/n ")
                
                
             
        # if product entered is not found in the Stock table
        else:
            print("\nProduct not found. Try again")
            continue
        
    if (flag == 'n' or flag == 'N'):
        print("\nProducts prchased : ",dic) 
        print("Total amount to be paid = Rs.",final_amt,"\n")

        items = str(dic)


        # storing the details of the purchase in the Sale table
        st = "insert into Sale(Date,Time,Customer_Name,Mobile_No,Invoice_No,Items,Total_Amount) values(%s,%s,%s,%s,%s,%s,%s)"
        row =(date,current_time,customer_name,mobile_no,invoice_no,items,final_amt)  # stores all the inputs in the form of a tuple
        #print (row)
        cursor.execute(st,row)   # executes the SQL statement
        mycon.commit()    # commit is written so that changes(insertion/deletion) reflect in the database
        print("_______________________________________________________________________________________________________________")
        print("Generating Invoice...")
        print()
        print()

        
        # invoice
        
        # shop details and date
        print("_______________________________________________________________________________________________________________")
        print("\n                                                       INVOICE                                                 ")
        print(shop_name)
        print("_______________________________________________________________________________________________________________")
        print("ADDRESS :",shop_address)
 
        print("GST NO. :",gst_no,end="                                                               ")
        print("DATE :",date)
 
        print("E-MAIL : ",email,end ="                                                         ")
        print("INVOICE NO. :",invoice_no)
        print("_______________________________________________________________________________________________________________\n")
 
 
 
        # customer details
        print("CUSTOMER NAME : ",customer_name)
        print("MOBILE NO. : ",mobile_no)
        print("_______________________________________________________________________________________________________________\n\n")

        headers = ["  PRODUCT CODE  ","  PRODUCT NAME  ","QTY","   RATE   "," DISCOUNT "," GST(%) ","   AMOUNT   "]
        print(tabulate(list1,headers = headers, tablefmt = 'grid',colalign = ("center","center","center","center","center","center","center",)))

        print("\nAmount payable : Rs. ",final_amt)

        
        # end part
        print("\n_______________________________________________________________________________________________________________\n")
        
        print("\n                                   Thanks for shopping!                            ")
        print("\n* Items once sold will not be exchanged or taken back. ")
        print("* Subject to Delhi Jurisdiction")
        print("* This is a computer generated invoice.")
        print("_______________________________________________________________________________________________________________\n")






