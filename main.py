import gst_billing

while True :
    # Main Display Screen
    print("=============================================================================")
    print("                              ABC ELECTRONICS                                ")
    print("=============================================================================")
     
    print("\nChoose from the following options :")
    print()
    print("1.Display Products")
    print("2.View Sale for a Period")
    print("3.Search ")
    print("4.Add Product in the stock")
    print("5.Delete Product from the stock")
    print("6.Update the stock")
    print("7.Generate GST Invoice")
    print("8.Exit")
     
    print()
    print("=============================================================================")
    num = int(input("Enter your choice : "))
    print("=============================================================================")


    if (num<0 or num==0 or num>8 ) :
        print("Invalid! Try again.")

    elif (num==8): # Exit 
        print("EXITING ...\n")
        break
          
    elif (num==1): # View Stock
        gst_billing.view()
        
    elif (num==2): # View Sale
        gst_billing.sales()

    elif (num==3): # Search Product
        print()
        print("SEARCH\nChoose from the following Search options :")
        print()
        print("1.Product Search ")
        print("2.Customer Search ")
        print()
        print("=============================================================================")
        num3 = int(input("Enter your choice : "))
        print("=============================================================================")
        print()
        
        if (num3 < 0 or num3 > 2) :
          print("Invalid! Try again.")
        elif (num3 == 1) :
          gst_billing.search()
        elif (num3 == 2) :
          gst_billing.cust_search()


    elif (num==4): # Add Product
        print()   
        gst_billing.add()

    elif (num==5): # Delete Product
        print()   
        gst_billing.delete()
        
    elif (num == 6): # Update Stock
        print()
        print("\t\tUPDATE\nChoose from the following Update options :")
        print()
        
        print("1.Update Quantity")
        print("2.Update Rates")
        print("3.Update GST")
        print()
        print("=============================================================================")
        num2 = int(input("Enter your choice : "))
        print("=============================================================================")
        print()

        if (num2 < 0 or num2 > 3) :
          print("Invalid! Try again.")
        elif num2 == 1:
          gst_billing.qty()
        elif num2 == 2:
          gst_billing.rate()
        elif num2 == 3:
          gst_billing.gst()

        
    elif (num == 7): # Generate invoice
        gst_billing.bill()

