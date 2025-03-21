def crc8(data, initial_value=0x7):
    crc = initial_value
    for byte in data:
        crc ^= byte
    return crc

# Kirish ma'lumotlari baytlar formatida
input_data = bytes([0x11, 0x01, 0x01, 0xF4, 0x00, 0x64])

# CRC8 hisoblash
result = crc8(input_data)
print(f"Hisoblangan CRC8: {result:#04x}")  # Natijani 0x formatida chiqarish
