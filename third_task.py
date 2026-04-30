import csv
#=================================== wonna firstly crete csv file 
# products = [
#     ['Milk',2,80],
#     ['Cheese',1,500],
#     ['Bred',2,70],
#     ]

# with open ('products.csv', 'w', newline='') as myFile:
#     fileWriter = csv.writer(myFile)
#     fileWriter.writerows(products)

totalPrice = 0   
with open ('products.csv', newline='') as myFile:
    fileReader = csv.reader(myFile)
    for row in fileReader:
        totalPrice += int(row[1]) * int(row[2])
        print(f"{row[0]} - {row[1]} pcs, for {row[2]} rubles")
        

print(f'Total price: {totalPrice} rubles')