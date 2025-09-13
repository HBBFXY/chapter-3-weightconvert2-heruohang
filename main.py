# 在这个文件里编写代码
earth_weight = float(input("请输入地球重量："))
print("年份\t地球重量\t月球重量")
for year in range(1, 11):
    moon_weight = earth_weight * 0.165
    print("{}年\t{:.2f}\t{:.2f}".format(year, earth_weight, moon_weight))
    earth_weight += 0.5
