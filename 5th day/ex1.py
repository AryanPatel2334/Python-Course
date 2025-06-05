##example

suzuki = ["Baleno","Eco","Swift"]
mahindra = ["Thar","Scorpio","Xuv700"]
cars = [suzuki,mahindra]
brands = ["Suzuki","Mahindra"]
print(cars)

for brand,car_list in zip(brands,cars):
    print(f"{brand}Cars:")
    for car in car_list:
        print(f" - {car}")
    print() # empty line for spacing


