# i = 0
# total = 0
# while i < 5:
#     new_number = int(input('enter a number: '))
#     total += new_number
#     i = i + 1
# print("total is :", total)


# for i in range(5):
#     new_number = int(input('enter a number: '))
#     total += new_number

# print("total is :", total)

# exercise برنامه ای بنویسید که مجموع اعداد بین پنج تا صدوبیست و پنج را محاسبه و نمایش دهد


zeros = 0
i = 0

while i < 5:
    new_number = int(input('enter a number : '))
    if new_number == 0:
        zeros += 1
    i += 1

print("number of zeros:", zeros)

# exercise 2 : برنامه بالا را با کمک حلقه فور بنویسید