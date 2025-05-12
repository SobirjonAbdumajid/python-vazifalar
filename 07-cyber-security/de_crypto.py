def caesar_cipher(message, shift, action='encrypt'):
    result = ""

    for char in message:
        if char.isalpha():  # Faqat harflar ustida ishlash
            if char.isupper():  # Katta harflar uchun
                if action == 'encrypt':
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                elif action == 'decrypt':
                    result += chr((ord(char) - shift - 65) % 26 + 65)
            else:  # Kichik harflar uchun
                if action == 'encrypt':
                    result += chr((ord(char) + shift - 97) % 26 + 97)
                elif action == 'decrypt':
                    result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char  # Agar belgi harf bo'lmasa, o'zgartirmasdan qo'shish

    return result


# Foydalanuvchidan matn va siljitish miqdorini olish
message = input("Shifrlamoqchi bo'lgan matningizni kiriting: ")
shift = int(input("Siljitish sonini kiriting: "))

# Shifrlashni amalga oshirish
encrypted_message = caesar_cipher(message, shift, action='encrypt')
print("Shifrlangan matn:", encrypted_message)

# Foydalanuvchidan deshifrlashni xohlash-xohlamasligini so‘rash
decrypt_choice = input("Bu matnni deshifrlaymizmi? (ha/yo'q): ").strip().lower()

if decrypt_choice == 'ha':
    decrypted_message = caesar_cipher(encrypted_message, shift, action='decrypt')
    print("Deshifrlangan matn:", decrypted_message)
else:
    print("Deshifrlash amalga oshirilmadi.")
