num = 0 
products = []
price = []
class shop :
    def __init__(self,products,price):
        self.products = products
        self.price = price
    def showshop(self):
        print(i+1,'.',self.products,'ราคา',self.price,' บาท')
    def show() :
        print('')
        print('*'*20,'ร้านนุกนิกยินดีต้อนรับ','*'*20)
        print('\tแสดงรายการสินค้า [a]')
        print('\tเพิ่มรายการสินค้า[s]')
        print('\tออกจากระบบ[x]')


while True :
    shop.show() 
    menu = input('กรุณาเลือกคำสั่ง :')
    if menu == 'a':
        for i in range(num):
            print('')
            x = shop(products[i],price[i])
            x.showshop()
    if menu == 's' :
        while True :
            print('เพิ่มรายการสินค้า หากต้องการยกเลิกให้กรอก exit')
            n = input('เพิ่มชื่อสินค้า :\t')
            if  n == 'exit' :
                break
            else:
                products.append(n) 
                p = input('ใส่ราคาของ'+n+': ')
                price.append(p)
                print('*'*10+'บันทึกข้อมูลสินค้าแล้ว'+'*'*10)
                num +=1
                e = input('\nต้องการเพิ่มสินค้าอีกหรือไม่(y/n): ')
                if e == 'n' :
                    break

    if menu == 'x' :
        e = input('ต้องการออกจากระบบหรือไม่(y/n): ')
        if e == 'y' :
            print('*****ออกจากโปรแกรมเรียนร้อยแล้ว*****')
            break