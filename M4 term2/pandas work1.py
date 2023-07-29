import pandas as pd

df = pd.read_excel("Stock.xlsx", index_col = "Name")

def edit():
    global df
    select = input('เลือก 1. เพิ่มจำนวนสินค้า\n     2. เพิ่มสินค้าฃ\n     3. ลบสินค้า\n     :')

    if select == '1':
        find = input('เลือกสินค้า : ')
        change = input('เพิ่ม หรือ ลด : ')
        add = int(input("ปริมาณเท่าไหร่ : "))
        if change == 'เพิ่ม':
            df.loc[find, "Amount"] += add
        elif change == 'ลด':
            df.loc[find, "Amount"] -= add

    elif select == '2':
        name1 = input('ชื่อ : ')
        type1 = input('ประเภท : ')
        price1 = input('ราคา : ')
        amount1 = input('จำนวน : ')
        
        product = []
        product.append([name1,type1,price1,amount1])
        cols = ["Name","Category","Price","Amount"]
        
        newdf = pd.DataFrame(data = product, columns=cols)
        newdf.set_index("Name",inplace=True)
        df = df.append (newdf)
        
    elif select == '3':
        find = input('เลือกสินค้า : ')
        df = df.drop(find)
    else:
        print("ออก")
        return

    redo = input("แก้ไขต่อ หรือ ไม่")
    if redo == "แก้ไขต่อ":
        edit()
    else:
        print("ออก")
        return

edit()
print(df)

save = input("บันทึก หรือ ไม่")
if save == "บันทึก":
    df.to_excel("Stock_0.xlsx")
    print("เรียบร้อย")
else:
    print("ออก")