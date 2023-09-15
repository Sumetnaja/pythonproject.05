#รับข้อมูลจำนวนเต็ม 5  จำนวนจากผู้ใช้ และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามาเป็นเท่าใด แล้วแสดงผลทางหน้าจอ

#ขอ 4 ฟังก์ชั่น ดังนั้นหาให้ได้ 4 feature

#============================
# Program Average 5 Number
#============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
#============================
# Sum of 5 number is : <output> (ขอทศนิยม 4 ตำแหน่ง)
# Average of 5 number is : <output> (ขอทศนิยม 4 ตำแหน่ง)
#============================

def inputNum ( ) :
    num_one = float( input('ป้อนหมายเลขที่ 1 : ') )
    num_two = float( input('ป้อนหมายเลขที่ 2 : ') )
    num_three = float( input('ป้อนหมายเลขที่ 3 : ') )
    num_four = float( input('ป้อนหมายเลขที่ 4 : ') )
    num_five = float( input('ป้อนหมายเลขที่ 5 : ') )
    return num_one, num_two, num_three, num_four, num_five

def calSumNumber ( num_one, num_two, num_three, num_four, num_five ) :
    sum_num = num_one + num_two + num_three + num_four + num_five
    return sum_num

def calAverNumber ( sum_num ) :
    aver_num = sum_num / 2
    return aver_num

def showResult( sum_num, aver_num ) :
    print(f'Sum of 5 number is : {sum_num} ')
    print(f'Average of 5 number is : {aver_num:.4f} ')

print('----------------------------')
print('--Program Average 5 Number--')
print('----------------------------')
num_one, num_two, num_three, num_four, num_five = inputNum( )
sum_num = calSumNumber( num_one, num_two, num_three, num_four, num_five )
aver_num = calAverNumber( sum_num )
print('----------------------------')
showResult( sum_num, aver_num )
print('----------------------------')