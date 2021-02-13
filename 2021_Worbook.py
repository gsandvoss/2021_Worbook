import sqlite3

from tkinter import *
window = Tk()
window.title("GSI 2021 Workbook")
window.geometry("740x740")
window.wm_iconbitmap("logo_2_.ico")

with sqlite3.connect("2021 Workbook.db") as db:
    cursor=db.cursor()

#subprogram to search by item number
def select_num1():
    item1 = textbox1.get()
    cursor.execute("SELECT field3 FROM GSI_2021_workbook_02 WHERE field1=?" , [item1])
    outbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field1=?" , [item1])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field1=?" , [item1])
    outbox3.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field1=?" , [item1])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field1=?" , [item1])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field1=?" , [item1])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])
    
    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field1=?" , [item1])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field1=?" , [item1])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field1=?" , [item1])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field1=?" , [item1])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])

    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 





#subprogram to delete all fields
def clear_list():
    textbox1.delete(0, END)
    textbox1.focus()
    outbox1.delete(0, END)
    outbox1.focus()
    outbox2.delete(0, END)
    outbox2.focus()
    outbox3.delete(0,END)
    outbox3.focus()
    outbox4.delete(0,END)
    outbox4.focus()
    outbox5.delete(0,END)
    outbox5.focus()
    outbox6.delete(0,END)
    outbox6.focus()
    outbox7.delete(0,END)
    outbox7.focus()
    outbox8.delete(0,END)
    outbox8.focus()
    outbox9.delete(0,END)
    outbox9.focus()
    outbox11.delete(0,END)
    outbox11.focus()
    selectProduct.set("Select Stoves")
    selectProduct2.set("Select Cookware")
    selectProduct3.set("Select Campfire")
    selectProduct4.set("Select Chef's Tools")
    selectProduct5.set("Select Tableware")
    selectProduct6.set("Select Insulated")
    selectProduct7.set("Select Java")
    selectProduct8.set("Select Partyware")
    selectProduct9.set("Select Base Camp")
    selectProduct10.set("Select Enamelware")
    selectProduct11.set("Select Merch")
    photo = PhotoImage(file = "blank.png")
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 

#subprogram to search by Stoves
def add_product1():

    product1 = selectProduct.get()
    outbox1.insert(END,product1)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product1])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product1])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product1])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product1])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product1])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product1])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product1])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product1])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product1])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product1])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 

#subprogram to search by product: Cookware
def add_product2():

    product2 = selectProduct2.get()
    outbox1.insert(END,product2)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product2])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product2])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product2])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product2])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product2])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product2])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product2])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product2])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product2])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product2])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 


    #subprogram to search by product: Campfire
def add_product3():

    product3 = selectProduct3.get()
    outbox1.insert(END,product3)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product3])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product3])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product3])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product3])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product3])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product3])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product3])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product3])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product3])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product3])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 

        #subprogram to search by product: Chef's Tools
def add_product4():

    product4 = selectProduct4.get()
    outbox1.insert(END,product4)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product4])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product4])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product4])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product4])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product4])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product4])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product4])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product4])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product4])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product4])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 


def add_product5():

    product5 = selectProduct5.get()
    outbox1.insert(END,product5)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product5])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product5])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product5])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product5])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product5])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product5])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product5])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product5])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product5])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product5])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 

def add_product6():

    product6 = selectProduct6.get()
    outbox1.insert(END,product6)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product6])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product6])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product6])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product6])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product6])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product6])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product6])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product6])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product6])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product6])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 

def add_product7():

    product7 = selectProduct7.get()
    outbox1.insert(END,product7)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product7])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product7])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product7])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product7])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product7])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product7])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product7])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product7])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product7])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product7])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 

def add_product8():

    product8 = selectProduct8.get()
    outbox1.insert(END,product8)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product8])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product8])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product8])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product8])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product8])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product8])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product8])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product8])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product8])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product8])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 

def add_product9():

    product9 = selectProduct9.get()
    outbox1.insert(END,product9)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product9])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product9])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product9])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product9])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product9])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product9])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product9])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product9])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product9])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product9])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 

def add_product10():

    product10 = selectProduct10.get()
    outbox1.insert(END,product10)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product10])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product10])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product10])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product10])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product10])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product10])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product10])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product10])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product10])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product10])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 

def add_product11():

    product11 = selectProduct11.get()
    outbox1.insert(END,product11)

    cursor.execute("SELECT field4 FROM GSI_2021_workbook_02 WHERE field3=?" , [product11])
    outbox2.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field1 FROM GSI_2021_workbook_02 WHERE field3=?" , [product11])
    textbox1.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field5 FROM GSI_2021_workbook_02 WHERE field3=?" , [product11])
    outbox3.insert(ANCHOR,cursor.fetchone()[0]) 

    cursor.execute("SELECT field12 FROM GSI_2021_workbook_02 WHERE field3=?" , [product11])
    outbox4.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field13 FROM GSI_2021_workbook_02 WHERE field3=?" , [product11])
    outbox5.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field15 FROM GSI_2021_workbook_02 WHERE field3=?" , [product11])
    outbox6.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field16 FROM GSI_2021_workbook_02 WHERE field3=?" , [product11])
    outbox7.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field17 FROM GSI_2021_workbook_02 WHERE field3=?" , [product11])
    outbox8.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field18 FROM GSI_2021_workbook_02 WHERE field3=?" , [product11])
    outbox9.insert(ANCHOR,cursor.fetchone()[0])

    cursor.execute("SELECT field14 FROM GSI_2021_workbook_02 WHERE field3=?" , [product11])
    outbox11.insert(ANCHOR,cursor.fetchone()[0])
 
    #Photo
    item1 = textbox1.get()
    artref = item1 + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update() 

selectProduct = StringVar (window)
selectProduct.set("Select Stove")
ProductList1 = OptionMenu(window, selectProduct, "Pinnacle Canister Stove", "Pinnacle 4 Season Stove" , "Glacier Camp Stove" , "isoButane 450 g Fuel Cartridge"  , "isoButane 110 g Fuel Cartridge" , "isoButane 230 g Fuel Cartridge", "Dualist HS with a 10K BTU Pinnacle Canister top stove." , "Pinnacle Pro 2 Burner Stove" , "Selkirk 460 Camp Stove" , "Selkirk 540 Camp Stove" , "Glacier Stainless Explorer Set" ) 
ProductList1.place(x = 20, y = 345 , width = "" , height = 30) 


selectProduct2 = StringVar (window)
selectProduct2.set("Select Cookware")
ProductList2 = OptionMenu(window, selectProduct2, "Pinnacle Dualist HS" , "Halulite Minimalist" , "Glacier Stainless Minimalist" ,  "Halulite Ketalist" , "Glacier Stainless Ketalist" , "MicroGripper" , "Pinnacle Soloist" , "Pinnacle Dualist" , "Glacier Stainless Dualist" , "Halulite MicroDualist" , "Pinnacle Camper" , "Pinnacle Backpacker" , "Bugaboo Camper" , "Bugaboo Backpacker" , "Glacier Stainless Camper" , "nForm Pot Gripper" ,"Pinnacle Base Camper Small" , "Pinnacle Base Camper Large" ,  "Bugaboo Base Camper Small" , "Glacier Stainless Base Camper Medium" ,"Bugaboo Base Camper Medium" , "Glacier Base Camper Large" ,"Bugaboo Base Camper Large" , "Escape HS 3 L Pot + Frypan" , "Escape HS 2 L Pot- Blue" , "Escape HS 3 L Pot- Green" , "Halulite 1.8 L Boiler" , "Halulite 1.1 L Boiler" , "Halulite 1.8 L Tea Kettle" , "Glacier Stainless 1.1 L Boiler" , "Halulite 1 L Tea Kettle" , "Glacier Stainless 1 qt. Tea Kettle" , "Glacier Stainless 1 Person Mess Kit" , "Halulite 2 L Pot" , "Halulite 3.2 L Pot" , "Halulite 4.7 L Pot" , "Diamondback Gripper" , "Bugaboo Mess Kit" , "Pinnacle 8in Frypan" , "Bugaboo 10in Frypan" , "Bugaboo 12in Frypan" ,"Gourmet 8in Frypan" , "Gourmet 10in Frypan" , "Glacier Stainless Troop Frypan" , "Gourmet Griddle" , "Bugaboo Griddle" , "GUIDECAST Thin Wall Cast Iron 10in Fry Pan" , "GUIDECAST Thin Wall Cast Iron 7 Qt. Dutch Oven" , "Halulite 2.7 L Pressure Cooker" , "Halulite 5.7 L Pressure Cooker") 
ProductList2.place(x = 20, y = 412 , width = "" , height = 30) 

selectProduct3 = StringVar (window)
selectProduct3.set("Select Campfire")
ProductList3 = OptionMenu(window, selectProduct3, "GUIDECAST Thin Wall Cast Iron 10in Fry Pan" , "GUIDECAST Thin Wall Cast Iron 12in Fry Pan" ,  "Glacier Stainless Troop Cookset" ,  "GUIDECAST Thin Wall Cast Iron 5 Qt. Dutch Oven" ,  "GUIDECAST Thin Wall Cast Iron 7 Qt. Dutch Oven" , "Aluminum 10in Dutch Oven" , "Hard Anodized 10in Dutch Oven" , "Hard Anodized 12in Dutch Oven" , "Hard Anodized 14in Dutch Oven" , "Universal Dutch Oven Lid Lifter" , "Universal Dutch Oven Stand" , "Folding Campfire Grill" , "Steel 9in Frypan" , "Steel 12in Frypan" , "Steel 20in Skillet") 

ProductList3.place(x = 20, y = 480 , width = "" , height = 30) 

selectProduct4 = StringVar (window)
selectProduct4.set("Select Chef's Tools")
ProductList4 = OptionMenu(window, selectProduct4,  "Pack Kitchen 8" , "Gourmet Kitchen Set 11" , "Crossover Kitchen Kit" , "Destination Kitchen Set 24" , "Santoku Cut+Prep" , "RAKAU Picnic Table" , "Santoku Knife Set" , "RAKAU Knife Set" , "Santoku 6in Chef Knife" , "Santoku 4in Paring Knife" , "Ultralight Cutting Board- Small" , "Ultralight Cutting Board- Large" , "Folding Cutting Board" , "Ultralight Salt + Pepper Shaker" , "Spice Missile" , "Spice Rocket" , "Salt + Pepper Shaker" , "Spice Rack" , "Peppermill" , "Compact Scraper" , "Soft Sided Condiment Bottle Set- 2 fl. oz." , "Camp Dish Cloth- Large" , "Pivot Spatula" , "Pack Spatula" , "RAKAU Spatula" , "Pivot Spoon" , "Pack Spoon" , "RAKAU Chef Spoon" , "Pivot Tongs" , "Pack Tongs" , "RAKAU Ladle" , "RAKAU Tongs" , "RAKAU Cutting Board - Small" , "RAKAU Picnic Table" , "Nylon Spatula" , "Pack Spoon/Spatula Set" , "Pack Grater" , "Nylon 3 pc. Ring Set") 

ProductList4.place(x = 20, y = 550 , width = "" , height = 30) 

selectProduct5 = StringVar (window)
selectProduct5.set("Select Tableware")
ProductList5 = OptionMenu(window, selectProduct5, "Cascadian 1 Person Table Set- Red" , "Cascadian 1 Person Table Set- Sky Blue" , "Cascadian 1 Person Table Set- Blue" , "Cascadian 1 Person Table Set- Green" , "Cascadian 1 Person Table Set- Orange" , "Cascadian 1 Person Table Set- Magenta" , "Cascadian 4 Person Table Set- Multi" , "Cascadian 4 Person Table Set- Blue" , "Cascadian Bowl- Red" ,  "Cascadian Bowl- Blue" , "Cascadian Bowl- Green" , "Cascadian Plate- Red" , "Cascadian Plate- Blue" , "Cascadian Plate- Green" , "Cascadian Cup- Red" , "Cascadian Cup-Blue" , "Cascadian Cup- Green" , "Cascadian Mug- Red" , "Cascadian Mug- Blue" , "Cascadian Mug- Green" , "Infinity 4 Person Deluxe Tableset- Multicolor" , "Infinity 1 Person Tableset- Blue" , "Infinity 1 Person Tableset- Green" , "Infinity Bowl- Blue" , "Infinity Bowl- Green" , "Infinity Serving Bowl- Blue" , "Infinity Serving Bowl- Green" , "Infinity Plate- Blue" , "Infinity Plate- Green" , "Infinity Divided Plate- Blue" , "Infinity Divided Plate- Green" , "Infinity Stacking Cup- Blue" , "Infinity Stacking Cup- Green" , "Infinity Mug - Blue" , "Infinity Mug - Green" ,  "Infinity Storage Set" , "Escape 17 fl. oz. Cup- Blue" , "Escape 17 fl. oz. Cup- Green" , "Escape Bowl- Blue" , "Escape Bowl- Green" , "Escape 1 Person Table Set- Blue" , "Escape Bowl + Lid- Blue" , "Escape Bowl + Lid- Green" , "Fairshare Mug - Blue" , "Fairshare Mug - Green" , "Collapsible Fairshare Mug- Blue" , "Collapsible Fairshare Mug- Green" , "Infinity Backpacker Mug- Red" , "Infinity Backpacker Mug- Blue" , "Infinity Backpacker Mug- Green" , "Infinity Backpacker Mug- Black" , "Infinity Backpacker Mug- Sand" , "Ultralight Nesting Bowl + Mug- Blue" , "Ultralight Nesting Bowl + Mug- Orange" , "Gourmet Nesting Mug + Bowl- Red" , "Gourmet Nesting Mug + Bowl- Blue" , "Gourmet Nesting Mug + Bowl- Green" , "Gourmet Nesting Mug + Bowl- Orange" , "Infinity 4 Person Compact Tableset- Multicolor" , "HALUITE 20 fl. oz. Aluminum Bottle Cup with Graduations" , "HALUITE 16 fl. oz. Aluminum Cup with Graduations" , "RAKAU Wooden Cup" , "Bugaboo 20 fl. oz. Bottle Cup- Blue" , "Bugaboo 20 fl. oz. Bottle Cup- Green" , "Bugaboo 14 fl. oz. Cup- Blue" , "Bugaboo 14 fl. oz. Cup- Green" , "Bugaboo 14 fl. oz. Cup- Orange" , "Bugaboo 14 fl. oz. Cup-  Purple" , "Glacier Stainless 20 fl. oz. Bottle Cup" , "Glacier Stainless 24 fl. oz. Bottle Cup" , "Glacier Stainless 14 fl. oz. Cup" , "Glacier Stainless Deep Plate" , "Glacier Stainless Plate" , "Glacier Stainless Bowl w/ Handle" , "Glacier Stainless Sierra Cup" , "RAKAU Compact Wood Fork, Knife and Spoon Set" , "Folding Foon- Blue" , "Folding Foon- Orange" , "Essential Travel Spoon" , "Essential Spoon- Long" , "Glacier Stainless Kung Foon" , "Spoon- Grey" , "Pouch Spoon- Grey" , "Spork" , "Fork- Grey" , "Knife- Grey" , "Halulite 3 pc. Ring Cutlery" , "Glacier Stainless 3 pc. Ring Cutlery" , "Tekk Cutlery Set- Eggshell" , "Tekk Cutlery Set- Blue" , "Glacier Stainless 3 pc. Cutlery Set" , "3 Pc. Ring Cutlery Set- Eggshell"  , "3 Pc. Ring Cutlery Set- Grey") 

ProductList5.place(x = 20, y = 620 , width = "" , height = 30) 

selectProduct6 = StringVar (window)
selectProduct6.set("Select Insulated")
ProductList6 = OptionMenu(window, selectProduct6, "MicroLite 570 Tour- Stainless Steel" , "MicroLite 570 Tour- Aqua" , "MicroLite 570 Tour- Mariner" , "MicroLite 570 Tour- Black" , "MicroLite 350 Flip- Red" , "MicroLite 350 Flip- Sky Blue" , "MicroLite 350 Flip- Black" , "MicroLite 350 Flip- Fuchsia" , "MicroLite 350 Flip- White" , "MicroLite 500 Flip- Haute Red" , "MicroLite 500 Flip- True Blue" , "MicroLite 500 Flip- Campsite" , "MicroLite 500 Flip- Acai" , "MicroLite 500 Flip- Black" , "MicroLite 500 Flip- Orangeade" , "MicroLite 500 Flip- White" , "MicroLite 500 Flip- Brushed" , "MicroLite 720 Flip- Brushed" , "MicroLite 720 Flip- Red Dahlia" , "MicroLite 720 Flip- True Blue" , "MicroLite 720 Flip-Mountain View" , "MicroLite 720 Flip- Black" , "MicroLite 720 Flip- White" , "MicroLite 1000 Twist- Brushed" , "MicroLite 1000 Twist- Red Dahlia" , "MicroLite 1000 Twist- True Blue" , "MicroLite 1000 Twist- Campsite" , "MicroLite 1000 Twist- Acai" , "MicroLite 1000 Twist- Black" , "MicroLite 1000 Twist- Ginger Bread" , "MicroLite 1000 Twist- White" , "MicroLite 720 Twist- Brushed" , "MicroLite 720 Twist- Mountain View" , "MicroLite 720 Twist- Black" , "MicroLite 720 Twist- Orangeade" , "MicroLite 500 Twist- Bonnie Blue" , "MicroLite 500 Twist- Mountain View" , "MicroLite 500 Twist- Black" , "MicroLite 500 Twist- E. Lavender" , "MicroLite 500 Twist- White" , "MicroLite 500 Twist- Blue + Sky Blue" , "MicroLite 500 Twist- Black + Taupe" , "MicroLite 500 Twist- Fuchsia + Purple" , "MicroLite 500 Flip Lid" , "MicroLite 500 Twist Lid" , "MicroLite 720 Flip Lid" , "MicroLite 720 Twist Lid" , "Glacier Stainless 1 L Vacuum Bottle- Stainless" , "Glacier Stainless 1 L Vacuum Bottle- Red" , "Glacier Stainless 1 L Vacuum Bottle- Blue" , "Glacier Stainless 1 L Vacuum Bottle- Black" , "Glacier Stainless 1 L Vacuum Bottle- Sand" , "Glacier Stainless 6.5 fl. oz. Doppio- Espresso" , "Glacier Stainless 6.5 fl. oz. Doppio- Milk" , "Glacier Stainless 6.5 fl. oz. Doppio- Vibrant Yellow" , "Glacier Stainless 6.5 fl. oz. Doppio- Glowing Blue" , "Glacier Stainless 6.5 fl. oz. Doppio- Living Coral" , "Glacier Stainless 16 fl. oz. Vacuum Tumbler- Brushed" , "Glacier Stainless 16 fl. oz. Vacuum Tumbler- Blue Speck", "Glacier Stainless 16 fl. oz. Vacuum Tumbler- Green Spec" , "Glacier Stainless 16 fl. oz. Vacuum Tumbler- Graphite" , "Glacier Stainless 15 fl. oz. Camp Cup- Brushed" , "Glacier Stainless 15 fl. oz. Camp Cup- Blue Speckle" , "Glacier Stainless 15 fl. oz. Camp Cup- Green Speckle" ,"Glacier Stainless 15 fl. oz. Camp Cup- Mineral Yellow" , "Glacier Stainless 15 fl. oz. Camp Cup- Black" , "Glacier Stainless 15 fl. oz. Camp Cup- Mountain View" , "Glacier Stainless 15 fl. oz. Camp Cup- Ginger Bread" , "Glacier Stainless 10 fl. oz. Camp Cup- Brushed" , "Glacier Stainless 10 fl. oz. Camp Cup- Blue Speckle" , "Glacier Stainless Double Walled Espresso Cup" , "Glacier Stainless 9 fl. oz. Tiffin- Stainless" , "Glacier Stainless 14 fl. oz. Tiffin- Stainless") 

ProductList6.place(x = 375, y = 345 , width = "" , height = 30) 

selectProduct7 = StringVar (window)
selectProduct7.set("Select Java")
ProductList7 = OptionMenu(window, selectProduct7, "Commuter JavaPress- Red" , "Commuter JavaPress- Blue" , "Commuter JavaPress- Green" , "Commuter JavaPress- Black" , "Commuter JavaPress- Sand" , "Microlite JavaPress- Bue" , "MicroLite JavaPress- Black" , "MicroLite JavaPress- Sand" , "MicroLite JavaPress- White" , "Glacier Stainless JavaPress- Brushed" , "Glacier Stainless JavaPress- Black" , "Personal JavaPress- Blue" , "30 fl. oz. JavaPress- Blue" , "30 fl. oz. JavaPress- Graphite" , "50 fl. oz. JavaPress- Blue" , "Ultralight Java Drip" , "JavaMill" , "Collapsible JavaDrip- Blue" , "Coffee Rocket" , "Gourmet PourOver Java Set" , "Reusable Java Filter #4" , "30 fl. oz. JavaDrip- Blue" , "MiniEspresso Set 1 Cup" , "MiniEspresso Set 4 Cup" , "Moka Espresso Pot" , "Glacier Stainless 3 cup Perc w/Silicone Handle" , "Glacier Stainless 6 cup Perc w/Silicone Handle" , "Glacier Stainless 9 cup Perc w/Silicone Handle" , "Glacier Stainless 12 cup Perc w/Silicone Handle" , "Resin PercView Top" , "Glass PercView Top" , "Glacier Stainless 8 cup PERC" , "Glacier Stainless 14 cup PERC" , "Glacier Stainless 28 cup PERC" , "Glacier Stainless 36 cup PERC") 

ProductList7.place(x = 375, y = 412 , width = "" , height = 30) 

selectProduct8 = StringVar (window)
selectProduct8.set("Select Partyware")
ProductList8 = OptionMenu(window, selectProduct8, "Glacier Stainless 5 fl. oz. Classic Flask"  , "Glacier Stainless 6 fl. oz. Hip Flask" , "Glacier Stainless 8 fl. oz. Hip Flask" , "Boulder 6 Flask- Purple" , "Boulder 6 Flask- Sand" , "Boulder 10 Flask- Graphite" , "Boulder 10 Flask- Orange" , "10 fl. oz. Flask" , "18 fl. oz. Flask" , "Nesting Wine Glass Set" , "Nesting Red Wine Glass Set" , "Nesting Champagne Flute Set" , "Stemless White Wine Glass" , "Stemless Red Wine Glass" , "Glacier Stainless Stemless Wine Glass" , "Glacier Stainless Nesting Wine Glass" , "Glacier Stainless Nesting Red Wine Glass" , "Glacier Stainless glass - Cabernet" , "Glacier Stainless glass -Mineral Yellow" , "Glacier Stainless glass - Espresso" , "Glacier Stainless glass - Harvest Pumpkin" , "Glacier Stainless glass - White" , "Glacier Stainless tumbler - Haute red" , "Glacier Stainless tumbler - Blue Aster" , "Glacier Stainless tumbler - Peppermint" , "Glacier Stainless tumbler - Acai" , "Glacier Stainless tumbler - White" , "Wine Glass Gift Set- Terroir" , "Soft Sided Wine Carafe- 750 ml" , "Highland Fifth Flask" , "Vortex Blender" , "Pint Glass" , "Glacier Stainless Pint Set- Multi")

ProductList8.place(x = 375, y = 480 , width = "" , height = 30) 

selectProduct9 = StringVar (window)
selectProduct9.set("Select Base Camp")
ProductList9 = OptionMenu(window, selectProduct9, "10 L Water Cube" , "15 L Water Cube" , "Micro Table" , "20 L Water Cube" , "Macro Table" , "Cathole Trowel" , "Small Gear Box" , "Large Gear Box" , "Medium Gear Box" , "Extra Large Gear Box" )

ProductList9.place(x = 375, y = 550 , width = "" , height = 30) 

selectProduct10 = StringVar (window)
selectProduct10.set("Select Enamelware")
ProductList10 = OptionMenu(window, selectProduct10, "12 fl. oz. Cup- Vintage" , "10in Plate- Vintage" , "6in Mixing Bowl- Vintage" , "8 cup Percolator- Vintage" , "Pioneer Camp Set- Blue" , "Pioneer Table Set- Blue" , "Pioneer Cutlery Set- Blue" , "Pioneer Sauce Pan- Blue" , "Glacier Stainless 16 fl. oz. Vacuum Tumbler- Blue Speck" , "Pioneer Fork- Blue" , "Pioneer Fry Pan- Blue" , "Glacier Stainless 10 fl. oz. Camp Cup- Blue Speckle" , "Pioneer Knife- Blue" , "Pioneer Pint- Blue" , "Pioneer Tablespoon- Blue" , "Pioneer 12 fl. oz. Cup- Blue" , "Pioneer 18 fl. oz. Cup- Blue" , "Pioneer 24 fl. oz. Cup- Blue" , "Pioneer 5.75in Mixing Bowl- Blue" ,  "Pioneer 9.5in Mixing Bowl- Blue" , "Pioneer Cereal Bowl- Blue" , "Pioneer 8.5in Plate- Blue" , "Pioneer 10.375in Plate- Blue" , "Sierra Camp Set- Blue" , "Sierra Table Set- Blue" , "36 Cup Coffee Boiler- Blue" , "Perc Insert Fits 8 Cup" , "Perc Insert Fits 12 Cup" , "8 cup Percolator- Blue" , "12 cup Percolator- Blue" , "20 Cup Coffee Boiler- Blue" , "3 Cup Coffee Pot- Blue" , "6 Cup Coffee Pot- Blue" , "8 Cup Coffee Pot- Blue" , "Tea Kettle- Blue" , "4 fl. oz. Cup- Blue" , "12 fl. oz. Cup- Blue" , "18 fl. oz. Cup- Blue" , "24 fl. oz. Cup- Blue" , "42 fl. oz. Cup- Blue" , "6in Mixing Bowl- Blue" , "7.75in Mixing Bowl- Blue" , "Cereal Bowl- Blue" , "8.75in Plate- Blue" , "10in Plate- Blue" ,"12.5in Plate- Blue" , "1.75 qt. Straight Pot w/ Lid- Blue" , "3.5 qt. Straight Pot w/ Lid- Blue" , "3 qt. Convex Kettle- Blue" , "4.25 qt. Convex Kettle- Blue" , "4 qt. Stock Pot- Blue" , "5.75 qt. Stock Pot- Blue" , "1 qt. Saucepan- Blue" , "2 qt. Saucepan- Blue" ,"Dish Pan- Blue" , "8.75in Frypan- Blue" , "Pioneer Camp Set- Green" , "Pioneer Table Set- Green" , "Pioneer Cutlery Set- Green" , "Pioneer Sauce Pan- Green" , "Pioneer Chef's Tools- Green" , "Pioneer Fork- Green" , "Pioneer Fry Pan- Green" , "Pioneer Knife- Green" , "Pioneer Pint- Green" , "Pioneer Spoon- Green" , "Pioneer 12 fl. oz. Cup- Green" , "Pioneer 24 fl. oz. Cup- Green" , "Glacier Stainless 16 fl. oz. Vacuum Tumbler- Green Spec" , "Pioneer 5.75in Mixing Bowl- Green" , "Pioneer 9.5in Mixing Bowl- Green" , "Pioneer 10.375in Plate- Green" , "Tea Kettle- Green" ,"8 cup Percolator- Green" , "12 cup Percolator- Green" , "4 fl. oz. Cup- Green" , "12 fl. oz. Cup- Green" , "6in Mixing Bowl- Green" , "10in Plate- Green" ,"Pioneer Table Set- Black" , "36 Cup Coffee Boiler- Black" , "8 Cup Percolator- Black" , "Pioneer 24 fl. oz. Cup- Black" , "Pioneer Pint- Black" , "Pioneer 10.375in Plate- Black" , "10in Plate- Black" , "Pioneer 12 fl. oz. Cup- Black" , "4 fl. oz. Cup- Black" , "6in Mixing Bowl- Black" , "Pioneer 5.75in Mixing Bowl- Black" , "12 fl. oz. Cup- Black" , "24 fl. oz. Cup- Black")

ProductList10.place(x = 375, y = 623 , width = "" , height = 30) 

selectProduct11 = StringVar (window)
selectProduct11.set("Select Merch")
ProductList11 = OptionMenu(window, selectProduct11, "Merchandising Rack" , "Tableware P.O.P Display" , "Microlite 8inX24in P.O.P. Sign" , "Microlite Curved P.O.P. Sign" , "GSI Outdoors Curved P.O.P. Sign" , "Outside Inside Curved P.O.P. Sign" , "Display Rack 9in Shelf" , "Display Rack 11in Shelf" , "Slat Wall Sign Supports" , "GSI Outdoors 8in Logo Hook" , "GSI Outdoors 36in Wall Logo Sign w/ Velcro")

ProductList11.place(x = 200, y = 675 , width = "" , height = 30) 

#Product ID Entry
textbox1 = Entry(text = "")
textbox1.place(x = 20 , y = 175 , width = 100 , height = 25)
label1 = Label(text = "Enter Item Number")
label1.place(x = 20 , y = 200 , width = 110 , height = 25)

#Search by Item number
button1 = Button(text = "Search by Item" , command = select_num1)
button1.place(x = 20 , y = 230 , width = 100 , height = 25)

#Search by Product - Stoves
button3 = Button(text = "Search Stoves" , command =  add_product1 , bg = "brown" , fg = "white")
button3.place(x = 20 , y = 373 , width = 100 , height = 25)

#Search by Product - Cookware
button4 = Button(text = "Search Cookware" , command =  add_product2 , bg = "orange" , fg = "white")
button4.place(x = 20 , y = 442 , width = 100 , height = 25)

#Search by Product - Campfire
button5 = Button(text = "Search Campfire" , command =  add_product3 , bg = "red" , fg = "white")
button5.place(x = 20 , y = 510 , width = 100 , height = 25)

#Search by Product - Chef's Tools
button6 = Button(text = "Search Chef's Tools" , command =  add_product4 , bg = "yellow" , fg = "black")
button6.place(x = 20 , y = 580 , width = 110 , height = 25)

#Search by Product - Tableware
button7 = Button(text = "Search Tableware" , command =  add_product5 , bg = "lime green" , fg = "black")
button7.place(x = 20 , y = 650 , width = 110 , height = 25)

#Search by Product - Insulated
button8 = Button(text = "Search Insulated" , command =  add_product6 , bg = "hot pink" , fg = "white")
button8.place(x = 375 , y = 373 , width = 100 , height = 25)

#Search by Product - Java
button9 = Button(text = "Search Java" , command =  add_product7 , bg = "purple" , fg = "white")
button9.place(x = 375 , y = 440 , width = 100 , height = 25)

#Search by Product - Partyware
button10 = Button(text = "Search Partyware" , command =  add_product8 , bg = "blue" , fg = "white")
button10.place(x = 375 , y = 509 , width = 100 , height = 25)

#Search by Product - Base Camp
button11 = Button(text = "Search Base Camp" , command =  add_product9 , bg = "dark blue" , fg = "white")
button11.place(x = 375 , y = 580 , width = 120 , height = 25)

#Search by Product - Enamelware
button12 = Button(text = "Search Enamelware" , command =  add_product10 , bg = "dark red" , fg = "white")
button12.place(x = 375 , y = 650 , width = 120 , height = 25)

#Search by Product - Merch
button13 = Button(text = "Search Merch" , command =  add_product11 , bg = "black" , fg = "white")
button13.place(x = 200 , y = 700 , width = 120 , height = 25)

#Delete all info
button2 = Button(text = "Reset Search" , command = clear_list , bg = "dark grey")
button2.place(x = 20 , y = 290 , width = 100 , height = 25)

#Product Name
outbox1 = Listbox()
outbox1.place(x = 230 , y = 30 , width = 370 , height = 25)
label2 = Label(text = "Product Name")
label2.place(x = 220 , y = 5 , width = 110 , height = 25)

#Product UPC
outbox2 = Listbox()
outbox2.place(x = 230 , y = 80 , width = 100 , height = 25)
label3 = Label(text = "Product UPC")
label3.place(x = 215 , y = 55 , width = 110 , height = 25)

#Product Case Pack
outbox3 = Listbox()
outbox3.place(x = 345 , y = 80 , width = 60 , height = 25)
label4 = Label(text = "Case Pack")
label4.place(x = 340 , y = 55 , width = 70 , height = 25)

#Size
outbox5 = Listbox()
outbox5.place(x = 420 , y = 80 , width = 82 , height = 25)
label6 = Label(text = "Size")
label6.place(x = 400 , y = 55 , width = 70 , height = 25)

#Size Int
outbox11 = Listbox()
outbox11.place(x = 520 , y = 80 , width = 80 , height = 25)
label12 = Label(text = "Size Int")
label12.place(x = 505 , y = 55 , width = 75 , height = 25)

#Includes
scrollbar = Scrollbar(orient="horizontal")
outbox4 = Listbox(xscrollcommand=scrollbar.set)
outbox4.place(x = 230 , y = 130 , width = 370 , height = 25)
label5 = Label(text = "Includes")
label5.place(x = 210 , y = 105 , width = 100, height = 25)
scrollbar.config(command=outbox4.xview)
scrollbar.pack(side="bottom", fill="y")
scrollbar.place(x = 230, y =155, width = 370, height = 10)

#Product Photo
photo = PhotoImage(file = "blank.png")
photobox = Label(window, image = photo)
photobox.image = photo
photobox.place(x = 20, y = 10, width = 200 , height = 155)

#Weight
outbox6 = Listbox()
outbox6.place(x = 230 , y = 200, width = 64 , height = 25)
label7 = Label(text = "Weight")
label7.place(x = 230 , y = 170 , width = 50, height = 25)

#Weight Int
outbox7 = Listbox()
outbox7.place(x = 320 , y = 200, width = 64 , height = 25)
label8 = Label(text = "Weight Int")
label8.place(x = 320 , y = 170 , width = 75, height = 25)

#Dims
outbox8 = Listbox()
outbox8.place(x = 230 , y = 250, width = 120 , height = 25)
label9 = Label(text = "Dims")
label9.place(x = 230 , y = 225 , width = 40, height = 25)

#Dims Int
outbox9 = Listbox()
outbox9.place(x = 380 , y = 250, width = 120 , height = 25)
label10 = Label(text = "Dims Int")
label10.place(x = 380 , y = 225 , width = 50, height = 25)

window.mainloop()
db.close()


       