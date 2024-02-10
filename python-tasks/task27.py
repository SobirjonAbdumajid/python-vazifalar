xona_boyi = float(input('xona boyi: '))
xona_eni = float(input('xona eni: '))
xona_balandligi = float(input('xona balandligi: '))

deraza_soni = float(input('deraza soni: '))
deraza_eni = float(input('xona eni: '))
deraza_boyi = float(input('xona balandligi: '))

result = ((xona_balandligi*xona_eni)*2) + (xona_balandligi*xona_boyi*2)+(xona_eni*xona_boyi)-(deraza_eni*deraza_boyi*deraza_soni)

print(f"Sizga {result*0.45} kg bo'yoq kerak")
