import math

print("=== Program Bangun Ruang dengan Sin, Cos, Tan, Phi ===")

r = 7
t = 15
volume_kerucut = (1/3) * math.pi * (r ** 2) * t
print(f"\n1) Volume Kerucut")
print(f" r = {r} cm, t = {t} cm")
print(f" Volume = {volume_kerucut:.2f} cm³")

tinggi_limas = 12
sudut_atas = 30
sisi_miring = tinggi_limas / math.sin(math.radians(sudut_atas))
luas_sisi_miring = sisi_miring * sisi_miring
print(f"\n2) Luas Sisi Miring Limas")
print(f" Tinggi = {tinggi_limas} cm, Sudut = {sudut_atas}°")
print(f" Luas sisi miring = {luas_sisi_miring:.2f} cm²")

alas_prisma = 10
sudut_prisma = 45
sudut_prisma = alas_prisma
tinggi_prisma = alas_prisma * math.tan(math.radians(sudut_prisma))

sisi_miring_prisma = alas_prisma / math.cos(math.radians(sudut_prisma))
print(f"\n3) Perhitungan Prisma")
print(f" Alas = {alas_prisma} cm, Sudut = {sudut_prisma}°")
print(f" Tinggi Prisma = {tinggi_prisma:.2f}cm")
print(f" Sisi miring prisma = {sisi_miring_prisma:.2f} cm")

print("\n=== Selesai ===")