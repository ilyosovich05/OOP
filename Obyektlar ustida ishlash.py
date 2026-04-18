"""Ushbu amaliyotda obyektlar bilan ishlayman.Class,obyekt,xususiyat va metodlar tushunchalarini
mustahkamlayman."""

from uuid import uuid4 
"""uuid moduli ID yaratish uchun foydalaniladi."""

class Inson:
    """Shaxs haqida ma'lumtlarni saqlovchi klass"""
    def __init__(self, ism, familiya, t_yil, jins, manzil=None):
        
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.jins = jins
        self.manzil=manzil
        
    def get_info(self):
        return (f"""\nIsm: {self.ism}
Familiya: {self.familiya}
Tugilgan yili: {self.t_yil}
Jins: {self.jins}""")

class Talaba(Inson):
    """TInson klasidan voris qilib olingan Talaba klassi"""
    def __init__(self,ism, familiya, t_yil, jins,universitet, fakultet, yonalish, bosqich, manzil=None):
        super().__init__(ism, familiya, t_yil, jins, manzil) #Ota klasidan chaqirib oladi.
        self.universitet = universitet
        self.fakultet = fakultet
        self.yonalish = yonalish
        self.bosqich = bosqich
        self.__id = uuid4() #Inkapsulatsiya qilingan xususiyat
        
    def get_eduinfo(self):
        """Talaba ma'lumotlarini beruvchi metod"""
        return (f"""\n{self.familiya} {self.ism} {self.universitet}
{self.fakultet} fakulteti {self.yonalish} yo'nalishining {self.bosqich}-bosqich talabasi.
\nTalaba ID : {self.__id}\n""")
                
    def get_id(self):
        """Inkapsulatsiya qilingan talaba IDsini chaqiruvchi metod"""
        return self.__id

class Manzil:
    """Manzil ma'lumotlarini saqlovchi klass"""
    def __init__(self,viloyat,tuman,mahalla,kocha,uy):
        self.viloyat=viloyat
        self.tuman=tuman
        self.mahalla=mahalla
        self.kocha=kocha
        self.uy=uy
        
    def get_manzil(self):
        return f"""{self.viloyat} viloyati {self.tuman} tumani {self.mahalla} mahallasi {self.kocha} ko'chasi {self.uy}-uy"""


odam1_manzil = Manzil("Xorazm", "Xonqa", "Obod", "Qanoat", 19)        
odam1=Inson("Karimboy", "Karimboyev", 2003, "Erkak", manzil=odam1_manzil)
talaba1=Talaba(odam1.ism, odam1.familiya, odam1.t_yil, odam1.jins, "Urganch Davlat Universiteti", "Fizika-matematika", "Amaliy matematika", 4)

""" **.odam1.__dict__ usuli yordamida super klassdan ma'lumotlarni oladigan qilsa xam bo'ladi"""
#talaba1=Talaba(**odam1.__dict__, universitet="Urganch Davlat Universiteti", fakultet="Fizika-matematika",yonalish= "Amaliy matematika", bosqich=4)



print(f"""SHAXS HAQIDA MA'LUMOT: 
{odam1.get_info()}

TALABA HAQIDA MA'LUMOT: 
{talaba1.get_eduinfo()}

TALABA MANZILI: 
{odam1.manzil.get_manzil()}""")



