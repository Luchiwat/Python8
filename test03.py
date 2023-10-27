# OOP
class IotSAU:
    major="SAU"
    name=""

    def showHi():
        print('Hi...')
    
    def untroduceMySelf(self):
        print(f'My name is {self.major}')
        print(f'My major is {self.major}')

obA = IotSAU()
obB = IotSAU()

print(obA.major)
obA.major="WOW"
obA.major="ฟ้าร้อง"
obA.name="ฝนตกแล้ว"

obA.introduceMyself()
obB.introduceMyself()