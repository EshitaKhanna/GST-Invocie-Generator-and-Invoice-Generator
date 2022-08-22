# GST-Invocie-Generator-and-Stock Management System
A system that enables an organization to manage the stock and create GST Invoices using Python and MySQL.


The basic functionality underlying the system is as follows:
The system allows the user to view, add, delete, and update the stock. 
It also includes important functionalities of generating GST invoices, searching a product, knowing the customer details, and seeing the sale in a particular period. 

Its main window gives the user 8 choices to work on: 
1. Display Products 
2. View Sale for a Period 
3. Search 
4. Add Product in the stock 
5. Delete Product from the stock 
6. Update the stock 
7. Generate GST Invoice 
8. Exit 
The system can also handle errors like “Out of Stock”, “No such product found”, “Invalid mobile number” etc., and display it to the user for better performance.

# SAMPLE 
=============================================================================
                              ABC ELECTRONICS                                
=============================================================================

Choose from the following options :

1.Display Products
2.View Sale for a Period
3.Search 
4.Add Product in the stock
5.Delete Product from the stock
6.Update the stock
7.Generate GST Invoice
8.Exit

=============================================================================
Enter your choice : 1
=============================================================================

STOCK
The Stock available is :

Product Name:  DT365
Product Code:  asus_dt365_908
Brand:  ASUS
Specifications:  32 GB| 6 GB RAM| Silver
Quantity:  2
Rate_in_Rs:  10000
Discount Available:  2890
GST:  19


Product Name:  YY_Laptop
Product Code:  dell_010_12
Brand:  DELL
Specifications:  16 GB RAM | 1 TB Hard drive| 12.0" display|Black
Quantity:  17
Rate_in_Rs:  49000
Discount Available:  2000
GST:  18


Product Name:  XX_Laptop
Product Code:  Hp_001_14
Brand:  HP
Specifications:  8 GB RAM | 1 TB Hard drive | 14.0" display| Grey
Quantity:  12
Rate_in_Rs:  45000
Discount Available:  2500
GST:  18


Product Name:  iPad
Product Code:  i_gr_421
Brand:  APPLE
Specifications:  32 GB| Stylus| Wi_Fi| 10" display| Grey
Quantity:  19
Rate_in_Rs:  29999
Discount Available:  1600
GST:  18


Product Name:  XS_ iphone
Product Code:  i_xs_0123
Brand:  APPLE
Specifications:  128 GB| 12 MP |Gold
Quantity:  34
Rate_in_Rs:  70000
Discount Available:  5000
GST:  19


Product Name:  TY_87SHeadphone
Product Code:  JBL_W276
Brand:  JBL
Specifications:  Wired|Mic|Black
Quantity:  75
Rate_in_Rs:  2000
Discount Available:  375
GST:  18


Product Name:  ZXC_OLED_Tv
Product Code:  LG_OL_23
Brand:  L.G.
Specifications:  8K| Ultra HD | 55" display
Quantity:  19
Rate_in_Rs:  80000
Discount Available:  8000
GST:  20


Product Name:  WebCam
Product Code:  log_mic_646
Brand:  Logitech
Specifications:  16 MP| Night Vision| Mic
Quantity:  39
Rate_in_Rs:  15950
Discount Available:  250
GST:  17


Product Name:  M12 Smart Phone
Product Code:  sam_M12_0033
Brand:  SAMSUNG
Specifications:  32 GB| 4 GB RAM| Red
Quantity:  6
Rate_in_Rs:  12599
Discount Available:  1500
GST:  19


Product Name:  PC_TL3 Wireless
Product Code:  SEN_PCTL34
Brand:  SENNHEISAR
Specifications:  Wireless|Mic|Blue
Quantity:  55
Rate_in_Rs:  22999
Discount Available:  200
GST:  18


=============================================================================
                              ABC ELECTRONICS                                
=============================================================================

Choose from the following options :

1.Display Products
2.View Sale for a Period
3.Search 
4.Add Product in the stock
5.Delete Product from the stock
6.Update the stock
7.Generate GST Invoice
8.Exit

=============================================================================
Enter your choice : 2
=============================================================================
Enter the period (YYMMDD) for which you want to see the sale. 

From : 210101
To : 210618

Date:  2021-06-13
Time:  0:05:54
Customer Name:  XYZ
Mobile Number:  1234567890
Invoice No.:  99939
Items Purchased:  {'iPad': 1, 'WebCam': 2}
Amount Paid:  70541



Date:  2021-06-13
Time:  0:19:34
Customer Name:  PQR
Mobile Number:  9999007530
Invoice No.:  50338
Items Purchased:  {'M12 Smart Phone': 1, 'YY_Laptop': 1, 'PC_TL3 Wireless': 2}
Amount Paid:  122709



Date:  2021-06-16
Time:  12:23:20
Customer Name:  ABX
Mobile Number:  7418523690
Invoice No.:  38974
Items Purchased:  {'ZXC_OLED_Tv': 1, 'YY_Laptop': 1}
Amount Paid:  141860


=============================================================================
                              ABC ELECTRONICS                                
=============================================================================

Choose from the following options :

1.Display Products
2.View Sale for a Period
3.Search 
4.Add Product in the stock
5.Delete Product from the stock
6.Update the stock
7.Generate GST Invoice
8.Exit

=============================================================================
Enter your choice : 3
=============================================================================

SEARCH
Choose from the following Search options :

1.Product Search 
2.Customer Search 

=============================================================================
Enter your choice : 1
=============================================================================

Product Name : iPad

The details are as follows : 

Product Name:  iPad
Product Code:  i_gr_421
Brand:  APPLE
Specifications:  32 GB| Stylus| Wi_Fi| 10" display| Grey
Quantity:  19
Rate_in_Rs:  29999
Discount Available:  1600
GST:  18


=============================================================================
                              ABC ELECTRONICS                                
=============================================================================

Choose from the following options :

1.Display Products
2.View Sale for a Period
3.Search 
4.Add Product in the stock
5.Delete Product from the stock
6.Update the stock
7.Generate GST Invoice
8.Exit

=============================================================================
Enter your choice : 3
=============================================================================

SEARCH
Choose from the following Search options :

1.Product Search 
2.Customer Search 

=============================================================================
Enter your choice : 2
=============================================================================

Mobile Number : 9999007530

The customer details are as follows : 

Customer Name:  PQR
Mobile Number:  9999007530
Date:  2021-06-13
Time:  0:19:34
Invoice Number:  50338
Items Purchased:  {'M12 Smart Phone': 1, 'YY_Laptop': 1, 'PC_TL3 Wireless': 2}
Total Amount Paid:  122709


=============================================================================
                              ABC ELECTRONICS                                
=============================================================================

Choose from the following options :

1.Display Products
2.View Sale for a Period
3.Search 
4.Add Product in the stock
5.Delete Product from the stock
6.Update the stock
7.Generate GST Invoice
8.Exit

=============================================================================
Enter your choice : 7
=============================================================================

                                               INVOICE                                                 
		                                   ABC ELECTRONICS                  
_______________________________________________________________________________________________________________
ADDRESS : C-58,Gandhi Road
	  New Delhi
	  Delhi - 1100XX
GST NO. : 0123456789                                                               DATE : 2021-06-17
E-MAIL :  abc@helpdesk.com                                                         INVOICE NO. : 62136
_______________________________________________________________________________________________________________

CUSTOMER NAME : ABX
MOBILE NO. : 7418523690

Enter the product name : PC_TL3 Wireless
Enter the quantity : 2
Amount =  54041.64

Do you want to enter more products ? y/n y

Enter the product name : DT365
Enter the quantity : 1
Amount =  8460.9

Do you want to enter more products ? y/n n

Products prchased :  {'PC_TL3 Wireless': 2, 'DT365': 1}
Total amount to be paid = Rs. 62502.54 

_______________________________________________________________________________________________________________
Generating Invoice...


_______________________________________________________________________________________________________________

                                                INVOICE                                                 
		                                   ABC ELECTRONICS                  
_______________________________________________________________________________________________________________
ADDRESS : C-58,Gandhi Road
	  New Delhi
	  Delhi - 1100XX
GST NO. : 0123456789                                                               DATE : 2021-06-17
E-MAIL :  abc@helpdesk.com                                                         INVOICE NO. : 62136
_______________________________________________________________________________________________________________

CUSTOMER NAME :  ABX
MOBILE NO. :  7418523690
_______________________________________________________________________________________________________________


+--------------------+--------------------+-------+--------------+--------------+------------+----------------+
|    PRODUCT CODE    |    PRODUCT NAME    |  QTY  |     RATE     |   DISCOUNT   |   GST(%)   |     AMOUNT     |
+====================+====================+=======+==============+==============+============+================+
|     SEN_PCTL34     |  PC_TL3 Wireless   |   2   |    22999     |     200      |     18     |    54041.6     |
+--------------------+--------------------+-------+--------------+--------------+------------+----------------+
|   asus_dt365_908   |       DT365        |   1   |    10000     |     2890     |     19     |     8460.9     |
+--------------------+--------------------+-------+--------------+--------------+------------+----------------+

Amount payable : Rs.  62502.54

_______________________________________________________________________________________________________________


                                   Thanks for shopping!                            

* Items once sold will not be exchanged or taken back. 
* Subject to Delhi Jurisdiction
* This is a computer generated invoice.
_______________________________________________________________________________________________________________

=============================================================================
                              ABC ELECTRONICS                                
=============================================================================

Choose from the following options :

1.Display Products
2.View Sale for a Period
3.Search 
4.Add Product in the stock
5.Delete Product from the stock
6.Update the stock
7.Generate GST Invoice
8.Exit

=============================================================================
Enter your choice : 8
=============================================================================
EXITING ...


