import pandas as pd

df = pd.read_excel("Stock.xlsx",index_col="Name")
print(df.to_string())
# df["delivery"] = 100

# # print (res)

# # df = pd.read_excel("Stock.xlsx",index_col="Name")
# product = [["sf","cinema",210,1,0],["major","cinema",190,1,0]]
# cols = ["Name","Category","Price","Amount","delivery"]

# newdf = pd.DataFrame(data = product, columns=cols)
# newdf.set_index("Name",inplace=True)
# df = df.append (newdf)

# df["total"] = df["Price"]*df["Amount"]+df["delivery"]
# res = df.sort_values("total")
# cols={'total':'total price'}
# df[1:2].Amount +=1
#print(df[1:2].index)