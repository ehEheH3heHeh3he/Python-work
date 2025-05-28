def start():
    
    # print("Enter the stock list (item name and price per line, type END_MENU when finished):")
    stock_list = []
    while True:
        item = input()
        stock_list.append(item)
        if item == "END_MENU":
            break

    # print("Enter the items you want to request (one per line, type END_REQUEST when finished):")
    requests = []
    while True:
        item = input()
        requests.append(item)
        if item == "END_REQUEST":
            break

    menu = {}
    for item_data_str in stock_list:
        if item_data_str == "END_MENU":
            break
        item_data = item_data_str.split()
        if len(item_data) == 2:
            item_name = item_data[0]
            try:
                price = int(item_data[1])
                menu[item_name] = price
            except ValueError:
                print(f"Warning: Invalid price for {item_name}. Skipping.")

    if not requests or (len(requests) == 1 and requests[0] == "END_REQUEST"):
        print("No Request")
        return

    for request in requests:
        if request == "END_REQUEST":
            break
        if request in menu:
            print(f"{request}: {menu[request]} THB")
        else:
            print(f"{request}: Not Found")

if __name__ == "__main__":
    start()