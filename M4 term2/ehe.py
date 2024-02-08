import pandas as pd

# อ่านข้อมูลจากไฟล์ Excel ชื่อ Stock.xlsx มาเก็บในตัวแปร stock
stock = pd.read_excel("Stock.xlsx", index_col = "Name")

# แสดงข้อมูลในตาราง stock เป็นรูปแบบของตาราง
print(stock.to_string())

# ฟังก์ชันสำหรับแสดงเมนูและรับค่าการเลือกเมนู
def get_selected() -> int:
    # แสดงเมนู
    print("==============================")
    choice = [
        "1. Search and changes the data",
        "2. Add a new product",
        "3. Delete a product",
        "4. Exit"
    ]
    print(*choice, sep = "\n")
    print("==============================")
    # รับค่าการเลือกเมนู
    # ที่ทำเป็น while True คือ ถ้าผู้ใช้กรอกข้อมูลผิด จะถามใหม่ไปเรื่อยๆ จนกว่าจะกรอกถูก
    while True:
        selected = input("Enter your choice: ")
        try:
            selected = int(selected)
            # ตรวจสอบว่าผู้ใช้กรอกเลขที่ไม่มีในเมนูหรือไม่
            if selected > len(choice) or selected < 1:
                print(f"Please enter a number from 1 to {len(choice)}")
                continue
            else:
                return selected
        except ValueError:
            # ถ้าผู้ใช้กรอกข้อมูลผิด (ไม่ใช่ตัวเลข) จะแสดงข้อความแจ้งเตือนและถามใหม่
            print("Cannot convert to number")

# ฟังก์ชันสำหรับรับค่าจำนวนเต็ม
# จะเหมือน get_selected() แต่ไม่แสดงเมนูและรับค่าตัวเลขเฉยๆแทน
def try_input_int(msg: str, error_msg: str = "Cannot convert to number") -> int:
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print(error_msg)

# รายชื่อสินค้าที่มีการเปลี่ยนแปลง จะใช้ในการ preview ก่อนบันทึก
changes: list[str] = []

# ฟังก์ชันสำหรับแก้ไขข้อมูล
def edit():
    # ใช้ัตัวแปร stock นอกฟังก์ชันต้องใช้ global
    global stock
    # รับค่าการเลือกเมนู
    opt = get_selected()
    if opt == 1:
        name = input("Enter the name of the product: ")
        if name not in stock.index:
            print("Product not found")
        else:
            print("Product found")
            print(f"Amount: {stock.loc[name, 'Amount']}")
            opt = input("Add or remove? (A/R): ")
            if opt == "A":
                amount = try_input_int("Enter the amount: ")
                stock.loc[name, "Amount"] += amount
                print("Add successfully")
            else:
                amount = try_input_int("Enter the amount: ")
                if amount > stock.loc[name, "Amount"]:
                    print("Not enough amount")
                else:
                    stock.loc[name, "Amount"] -= amount
                    print("Remove successfully")
            changes.append(name)
    elif opt == 2:
        name = input("Enter the name of the product: ")
        if name in stock.index:
            print("Product already exists")
        else:
            category = input("Enter the category of the product: ")
            price = try_input_int("Enter the price of the product: ")
            amount = try_input_int("Enter the amount of the product: ")
            stock.loc[name] = [category, price, amount]
            changes.append(name)
            print("Add successfully")
    elif opt == 3:
        name = input("Enter the name of the product: ")
        if name not in stock.index:
            print("Product not found")
        else:
            stock = stock.drop(name)
            changes.append(name)
            print("Delete successfully")
    else:
        print("Exit")
        return

    # ถามว่าต้องการแก้ไขต่อหรือไม่
    more = input("Do you want to continue? (Y/N): ")
    if more == "Y":
        # เรียกใช้ฟังก์ชันตัวเองเพื่อทำซ้ำ
        edit()
    else:
        print("Exit")
        return

# เรียกใช้ฟังก์ชันแก้ไขข้อมูล
edit()

# แสดงข้อมูลที่เปลี่ยนแปลง
changed_table = stock.loc[changes]
print(changed_table.to_string())

# ถามว่าต้องการบันทึกหรือไม่
save = input("Do you want to save the changes? (Y/N): ")
if save == "Y":
    stock.to_excel("Stock.xlsx")
    print("Save successfully")
else:
    print("Discarded changes")