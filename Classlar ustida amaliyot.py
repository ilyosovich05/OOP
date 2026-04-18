"""
Mavzu: Classlar (Klasslar)

Amaliyot egasi: theilyosovich (Karim) 

Amaliyot sanasi: 2026-yil, 5-yanvar

GitHub profil: https://github.com/theilyosovich

"""

class User:
    def __init__(self, ism, familiya, username, phone_number, email,jins, age):
        if "@" not in username or "@" not    in email:
            raise ValueError("Username yaroqsiz: \"@\" belgisi bo'lishi shart!")
        self.name = ism
        self.family = familiya
        self.username = username
        self.telefon_raqam =  phone_number
        self.email = email
        self.age = age
        self.jins = jins
        
    def malumot_ber(self, j_yil):
        return (
    f"\nFoydalanuvchining ism-familiyasi: "
    f"{self.name.title()} {self.family.title()}\n"
    f"Foydalanuvchi yoshi: {j_yil - self.age} yosh\n"
    f"Foydalanuvchi jinsi: {self.jins}\n"
    f"Foydalanuvchi nomi:"
    f" {self.username}\n"
    f"Foydalanuvchi telefon raqami:"
    f" {self.telefon_raqam}\n"
    f"Foydalanuvchi elektron manzili:"
    f" {self.email}\n"
    )
    

user1=User("Karim", "Karimboyev", "@theilyosovich", "+998918623808", "theilyosovich@gmail.com", "Erkak", 2003)
user2=User("Guli", "Ravshanbekova", "@theilyosovich", "+998918623808", "theilyosovich@gmail.com","Ayol", 2004)

user=[user1,user2]

for foydalanuvchi in user:
    print(foydalanuvchi.malumot_ber(2026))

    