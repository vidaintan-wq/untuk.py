import math
import pandas as pd

def format_pi(degrees):
    """Mengubah derajat menjadi bentuk phi bila sesuai"""
    mapping = {
        0: "0",
        30: "π/6",
        45: "π/4",
        60: "π/3",
        90: "π/2",
        180: "π",
        270: "3π/2",
        360: "2π"
    }
    return mapping.get(degrees, "")

def hitung_rasio_trigonometri():
    # Daftar sudut dalam derajat (termasuk π = 180°)
    sudut_derajat = [0, 30, 45, 60, 90, 180, 270, 360]

    data = []

    for sudut in sudut_derajat:
        rad = math.radians(sudut)
        pi_label = format_pi(sudut)

        # Hitung sin cos tan
        try:
            sin_val = round(math.sin(rad), 6)
        except:
            sin_val = "undef"

        try:
            cos_val = round(math.cos(rad), 6)
        except:
            cos_val = "undef"

        try:
            tan_val = round(math.tan(rad), 6)
        except:
            tan_val = "undef"

        # hitung kebalikan
        csc_val = "undef" if sin_val == 0 else round(1/sin_val, 6)
        sec_val = "undef" if cos_val == 0 else round(1/cos_val, 6)
        cot_val = "undef" if tan_val == 0 else round(1/tan_val, 6)

        data.append({
            "Sudut (°)": sudut,
            "Sudut (π rad)": pi_label,
            "sin(0)": sin_val,
            "cos(0)": cos_val,
            "tan(0)": tan_val,
            "csc(0)": csc_val,
            "sec(0)": sec_val,
            "cot(0)": cot_val
        })

    # Tampilkan hasil tabel menggunakan library pandas
    df = pd.DataFrame(data)
    print("=== TABEL RASIO TRIGONOMETRI BESERTA RADIAN ===\n")
    print(df.to_string(index=False))

if __name__ == "__main__":
    hitung_rasio_trigonometri()
