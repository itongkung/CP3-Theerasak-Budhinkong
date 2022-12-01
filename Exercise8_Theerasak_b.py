youadmin = input()

if youadmin == "admin":
    usernameInput = input("User :")
    passwordInput = input("Pass :")
    if usernameInput == "adminshop" and passwordInput == "pass":
        print("opatong shop")
        print("1. คุณต้องการดูสินค้าทั้งหมดไหม?")
        print("2. คุณต้องการกรอกชื่อและขายเองใช่ไหม?")
        selshopitem = int(input("คุณต้องการเลือก : "))
        if selshopitem == 1:
            A = ("ผักกาด : ราคา 20 บาท")
            B = ("ผักขม : ราคา 40 บาท")
            C = ("ผักชี : ราคา 10 บาท")
            D = ("ผักบุ้ง : ราคา 15 บาท")
            E = ("ผักคะน้า : ราคา 25 บาท")
            print("ID 1", A, "ID 2", B, "ID 3", C, "ID 4", D, "ID 5", E)
            itemid = int(input("เลือก ID สินค้า : "))
            if itemid == 1:
                amitem = int(input("จำนวนที่ต้องการ : "))
                price = int(20)
                maxprice = int(amitem*price)
                vat = 7
                result = maxprice + (maxprice * 7/100)
                print(A ,"ราคาทั้งหมด",result,"บาท รวมภาษีแล้ว")
            if itemid == 2:
                amitem = int(input("จำนวนที่ต้องการ : "))
                price = int(40)
                maxprice = int(amitem*price)
                vat = 7
                result = maxprice + (maxprice * 7/100)
                print(B, "ราคาทั้งหมด", result, "บาท รวมภาษีแล้ว")
            if itemid == 3:
                amitem = int(input("จำนวนที่ต้องการ : "))
                price = int(10)
                maxprice = int(amitem*price)
                vat = 7
                result = maxprice + (maxprice * 7/100)
                print(C, "ราคาทั้งหมด", result, "บาท รวมภาษีแล้ว")
            if itemid == 4:
                amitem = int(input("จำนวนที่ต้องการ : "))
                price = int(15)
                maxprice = int(amitem*price)
                vat = 7
                result = maxprice + (maxprice * 7/100)
                print(D, "ราคาทั้งหมด", result, "บาท รวมภาษีแล้ว")
            if itemid == 5:
                amitem = int(input("จำนวนที่ต้องการ : "))
                price = int(25)
                maxprice = int(amitem*price)
                vat = 7
                result = maxprice + (maxprice * 7/100)
                print(E, "ราคาทั้งหมด", result, "บาท รวมภาษีแล้ว")
        elif selshopitem == 2:
            nameitem = str(input("ชื่อสินค้า : "))
            price = int(input("ราคาสินค้า : "))
            amitem = int(input("จำนวนที่ต้องการ : "))
            maxprice = int(amitem*price)
            vat = 7
            result = maxprice + (maxprice * 7/100)
            print("สินค้า", nameitem, "ราคาทั้งหมด", result, "บาท รวมภาษีแล้ว")
