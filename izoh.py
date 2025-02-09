import math

def Invers_task(point):
    """Berilgan (x, y) nuqta uchun robot qo‘lining burchaklarini hisoblash"""
    x, y = point
    L1 = 10  # Birinchi bo'g'in uzunligi
    L2 = 10  # Ikkinchi bo'g'in uzunligi

    # Berilgan nuqtaning robot qo‘li yetib borishi mumkinligini tekshirish
    D = x**2 + y**2
    if D > (L1 + L2)**2 or D < (L1 - L2)**2:
        raise ValueError("Berilgan nuqtaga robot qo‘li yetib bora olmaydi!")

    # A2 ni hisoblash va validatsiya qilish
    A2 = (D - L1**2 - L2**2) / (2 * L1 * L2)
    if not -1 <= A2 <= 1:
        raise ValueError(f"A2 qiymati ({A2}) acos uchun noto‘g‘ri!")

    f21 = math.acos(A2)  # Ikkinchi bo‘g‘in burchagi

    # Birinchi bo‘g‘in burchagini hisoblash
    k1 = L1 + L2 * math.cos(f21)
    k2 = L2 * math.sin(f21)
    f11 = math.atan2(y, x) - math.atan2(k2, k1)

    return math.degrees(f11), math.degrees(f21)  # Gradusda qaytarish

def main():
    """Foydalanuvchidan nuqta kiritib, natijani chiqaruvchi funksiya"""
    try:
        x = float(input("X koordinatasini kiriting: "))
        y = float(input("Y koordinatasini kiriting: "))

        f11, f21 = Invers_task((x, y))
        print(f"Hisoblangan burchaklar: f11 = {f11:.2f}°, f21 = {f21:.2f}°")

    except ValueError as e:
        print(f"Xatolik: {e}")

if __name__ == "__main__":
    main()
