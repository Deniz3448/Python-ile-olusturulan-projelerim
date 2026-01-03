Random Code Generator (Python)

This project generates a random code consisting of letters and digits using Python.
The generated code is guaranteed to contain at least one letter and one digit.

Features
- Generates a 6-character code by default
- Ensures at least:
  - One letter
  - One digit
- Randomly shuffles characters
- Code length can be customized via a parameter

Usage
print(generate_code())

To generate a code with a custom length:
print(generate_code(10))

Function Description
def generate_code(length=6)

Parameter:
length — Length of the generated code (minimum value is 2)

If the length is less than 2, the function raises a ValueError.

Requirements
- Python 3.x
- random
- string
(No external libraries required)

Use Cases
- Verification codes
- Reference numbers
- Simple token generation
- Random data generation for testing

License
This project is intended for educational and personal use.
--------------------------------------------------

Rastgele Kod Üretici (Python)

Bu proje, Python kullanarak harf ve rakamlardan oluşan rastgele bir kod üretir.
Üretilen kodun en az bir harf ve bir rakam içermesi garanti edilir.

Özellikler
- Varsayılan olarak 6 karakterlik kod üretir
- En az şunları içerir:
  - Bir harf
  - Bir rakam
- Karakterleri rastgele karıştırır
- Kod uzunluğu parametre ile değiştirilebilir

Kullanım
print(generate_code())

Özel uzunlukta kod üretmek için:
print(generate_code(10))

Fonksiyon Açıklaması
def generate_code(length=6)

Parametre:
length — Üretilecek kodun uzunluğu (minimum değer 2’dir)

Uzunluk 2’den küçükse fonksiyon ValueError hatası fırlatır.

Gereksinimler
- Python 3.x
- random
- string
(Harici kütüphane gerekmez)

Kullanım Alanları
- Doğrulama kodları
- Referans numaraları
- Basit token üretimi
- Test amaçlı rastgele veri üretimi

Lisans
Bu proje eğitim ve kişisel kullanım amaçlıdır.
