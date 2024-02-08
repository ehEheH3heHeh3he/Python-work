import pandas as pd

df = pd.read_excel("Stock.xlsx", index_col = "Name")
df0 = pd.read_excel("Stock.xlsx")
new_df = df

print(df)

def main():
    print(new_df)
    print("\n1. ค้นหาสินค้า\n2. เพิ่มสินค้า\n3. ลบสินค้า\n4. หยุดการทำงาน")
    Choice = int(input("โปรดกรอกตัวเลือก: "))
    if Choice == 1:
        findPdt()
    elif Choice == 2:
        addPdt()
    elif Choice == 3:
        removePdt()
    elif Choice == 4:
        stop()
    else:
        print("กรุณาพิมพ์ใหม่อีกครั้ง")
        main()

def findPdt(): # Choice == 1:
    Name = input("โปรดกรอกชื่อสินค้า: ")
    if Name in df.index:
        amt_p = int(df0.Amount[df0.Name == Name])
        print(f"{Name} มีจำนวน {amt_p}")
        op = input("นำออกหรือนำเข้า (A/R): ")
        if op == "A":
            amt = int(input("ใส่จำนวนที่ต้องการเพิ่ม: "))
            new_amt = amt_p + amt
            print(f"{Name} มีจำนวน {new_amt}")
            findSave = input("ต้องการเพิ่มจำนวนสินค้า (Y/N): ")
            if findSave == "Y":
                new_df.replace(to_replace={amt_p : new_amt}, inplace = True)
                print(new_df)
                print("รายการสำเร็จ")
                main()
            else:
                print("ยกเลิกการเพิ่มจำนวนสินค้า")
                main()
        elif op == "R":
            amt = int(input("ใส่จำนวนที่ต้องการลด: "))
            new_amt = amt_p - amt
            print(f"{Name} มีจำนวน {new_amt}")
            findSave = input("ต้องการลดจำนวนสินค้า (Y/N): ")
            if findSave == "Y":
                new_df.replace(to_replace={amt_p : new_amt}, inplace = True)
                print("รายการสำเร็จ")
            else:
                print("ยกเลิกการลดจำนวนสินค้า")
                main()
        else:
            print("error")
            Restart = input("เริ่มทำการใหม่หรือไม่ (Y/N): ")
            if Restart == "Y":
                findPdt()
            else:
                main()
    else:
        print("ไม่พบรายการสินค้า กรุณาลองใหม่อีกครั้ง")
        Restart = input("เริ่มทำการใหม่หรือไม่ (Y/N): ")
        if Restart == "Y":
            findPdt()
        else:
            main()
        
def addPdt(): # Choice == 2:
    global new_df
    newName = input("โปรดกรอกชื่อสินค้า: ")
    newCategory = input("โปรดกรอกประเภทสินค้า: ")
    newPrice = input("โปรดกรอกราคาสินค้า: ")
    newAmt = input("โปรดกรอกจำนวนสินค้า: ")
    newPdt = [[newName, newCategory, newPrice, newAmt]]
    cols = ["Name", "Category", "Price", "Amount"]
    newDf = pd.DataFrame(data=newPdt,columns=cols)
    print(newDf, '\n')
    newSave = input("ต้องการบันทึกหรือไม่ (Y/N): ")
    if newSave == "Y":
        newDf.set_index("Name", inplace = True)
        new_df = new_df.append(newDf)
        print(new_df)
        main()
    elif newSave == "N":
        print("ยกเลิกการเพิ่มสินค้า")
        Restart = input("เริ่มทำการใหม่หรือไม่ (Y/N): ")
        if Restart == "Y":
            addPdt()
        else:
            main()

def removePdt(): # Choice == 3:
    delName = input("โปรดกรอกชื่อสินค้าที่ต้องการลบ: ")
    if delName in df.index:
        delSave = input("ยืนยันการลบสินค้า (Y/N): ")
        if delSave == "Y":
            new_df.drop(delName, axis = 0, inplace = True)
            print(new_df)
            main()
        elif delSave == "N":
            print("ยกเลิกการลบสินค้า")
            main()
        else:
            Restart = input("เริ่มทำการใหม่หรือไม่ (Y/N): ")
            if Restart == "Y":
                removePdt()
            else:
                main()
    else:
        print("ไม่พบรายการสินค้า กรุณาลองใหม่อีกครั้ง")
        Restart = input("เริ่มทำการใหม่หรือไม่ (Y/N): ")
        if Restart == "Y":
            removePdt()
        else:
            main()

def stop(): #Choice == 4:
    save = input("ต้องการบันทึกหรือไม่ (Y/N): ")
    if save == "Y":
        # new_df.to_excel("Stock_1.xlsx")
        print(new_df)
        print("บันทึกสำเร็จ")
    elif save == "N":
        print("ยกเลิกการบันทึก")
        pass
    else:
        print("กรุณาพิมพ์ใหม่อีกครั้ง")
        stop()

main()