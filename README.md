

Bu Python dasturi, robota manipulyatorining kinematik masalalarini yechish uchun mo'ljallangan. U ikki asosiy funksiyani o'z ichiga oladi: **direct_task** (to'g'ri kinematika) va **Invers_task** (teskari kinematika). Dastur quyidagi qismlardan iborat:



---



### 1. **Global o'zgaruvchilar**

```python

d0 = 30 # O'rnatilgan ma'lumotlar

l1 = 200.0

l2 = 200.0

h0 = 140

f1_min = -45.0 * math.pi/180.0

f1_max = 30 * math.pi / 180

f2_min = -60 * math.pi / 180

f2_max = 70 * math.pi / 180

f_between = 140.0 * math.pi / 180.0

```

- Bu o'zgaruvchilar robota manipulyatorining fizik konstantalari sifatida ishlatiladi:

 - `d0`: Manipulyatorning boshlang'ich pozitsiyasi.

 - `l1`, `l2`: Robota manipulyatorining brakhet uzunliklari.

 - `h0`: Manipulyatorning boshlang'ich balandligi.

 - `f1_min`, `f1_max`, `f2_min`, `f2_max`: Robota manipulyatorining cheklarini belgilaydi.

 - `f_between`: Brakhetlar orasidagi maksimal burchak.



---



### 2. **Direct_task funksiyasi**

```python

def direct_task(in_values):

  Ey_ = d0 - l1 * math.sin(in_values[0]) + l2 * math.cos(in_values[1])

  Ex = Ey_ * math.cos(in_values[2])

  Ey = Ey_ * math.sin(in_values[2])

  Ez = h0 + in_values[3] + l1 * math.cos(in_values[0]) + l2 * math.sin(in_values[1])

  return [Ex, Ey, Ez]

```

- **Maqsad**: To'g'ri kinematika masalasini yechish (obektiv koordinatalarini hisoblash).

- **Kirish parametrlari**:

 - `in_values`: Manipulyatorning obyektiv vaziyati (brakhet burchaklari va uzunlik).

- **Hisoblash jarayoni**:

 - `Ey_`: Manipulyator boshqarmasining X-Y tekisda joylashgan nuqtasi.

 - `Ex`, `Ey`: Manipulyator boshqarmasining global koordinatalarida X va Y qiymatlari.

 - `Ez`: Manipulyator boshqarmasining Z koordinatasida balandligi.

- **Natija**: `[Ex, Ey, Ez]` — manipulyator boshqarmasining global koordinatalari.



---



### 3. **Invers_task funksiyasi**

```python

def Invers_task(in_vector):

  ...

```

- **Maqsad**: Teskari kinematika masalasini yechish (koordinatalar asosida brakhet burchaklarini hisoblash).

- **Kirish parametrlari**:

 - `in_vector`: Manipulyator boshqarmasining global koordinatalari `[X, Y, Z]`.

- **Hisoblash jarayoni**:

 - `ALPHA`: Boshqarma vektorining Y/X nisbati.

 - `f3`: Manipulyatorning osi bo'yicha burilish burchagi.

 - `L4`: Manipulyatorning to'g'riroq uzunligi.

 - Funksiya bir necha iteratsiya bilan teskari kinematika masalasini yechadi va barcha cheklarni tekshiradi (`f1_min`, `f1_max`, `f2_min`, `f2_max`, `f_between`).

- **Natija**: `[f1, f2, f3, L4]` — manipulyatorning brakhet burchaklari va uzunligi.



---



### 4. **Main funksiyasi**

```python

def main():

  ...

```

- **Maqsad**: Manipulyatorning harakatini simulatsiya qilish.

- **Qadam-qadam tushuntirish**:

 1. **Boshlang'ich ma'lumotlar**:

   - `obob_coord`: Manipulyatorning boshlang'ich obyektiv vaziyati.

   - `coord_E`: Direct_task funksiyasi yordamida manipulyatorning boshlang'ich global koordinatalari.

 2. **Traektoriya yaratish**:

   - `r0`: Traektoriyaning boshlang'ich nuqtasi.

   - `rN`: Traektoriyaning oxirgi nuqtasi.

   - `trajectory`: Bir necha nuqtadan iborat traektoriya yaratiladi.

 3. **Teskari kinematika hisoblash**:

   - Har bir traektoriya nuqtasi uchun `Invers_task` funksiyasi chaqiriladi.

   - Harakat tezligi va vaqt hisoblanadi.

 4. **Natijalarni chiqarish**:

   - Manipulyatorning harakatini vaqt bo'yicha aniqlab, natijalarni konsolga chiqaradi.



---



### 5. **Dastur ishlashi**

Dastur manipulyatorning harakatini bir necha qadamda simulatsiya qiladi:

1. Boshlang'ich holatni belgilash.

2. Traektoriya yaratish.

3. Har bir traektoriya nuqtasi uchun teskari kinematika masalasini yechish.

4. Harakat tezligini va vaqtni hisoblash.

5. Natijalarni ekranga chiqarish.



---



### 6. **Kodning muhim jihatlari**

- **To'g'ri va teskari kinematika**:

 - To'g'ri kinematika: Obektiv vaziyatdan global koordinatalarga o'tish.

 - Teskari kinematika: Global koordinatalardan obektiv vaziyatga o'tish.

- **Cheklar**:

 - Brakhet burchaklari va manipulyator uzunligi cheklaridan foydalaniladi.

- **Iteratsion usul**:

 - Teskari kinematika masalasini yechishda bir necha iteratsiya amalga oshiriladi.



---



### 7. **Natija**

Dastur manipulyatorning harakatini aniqlash uchun ishlatilishi mumkin. U harakat tezligini, vaqtni va manipulyatorning barcha vaziyatlarini hisoblaydi va konsolga chiqaradi. Bu robotika sohasida foydali bo'lishi mumkin.