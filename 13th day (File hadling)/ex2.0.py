#Read from excel file

with open("excel.csv","r") as file:
    content = file.read()
    print(content)
