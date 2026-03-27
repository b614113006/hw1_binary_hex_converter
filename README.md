# hw1_binary_hex_converter
import tkinter as tk
from tkinter import messagebox

MAX_VALUE = 255
HEX_CHARS = "0123456789ABCDEF"

def dec_to_bin(n: int) -> str:
    """Style 9: 將十進位轉換為二進位（連除法） [cite: 104, 287]"""
    if n == 0: return "0"
    res = ""
    temp = n
    while temp > 0:
        res = str(temp % 2) + res
        temp //= 2
    return res

def dec_to_hex(n: int) -> str:
    """Style 9: 將十進位轉換為十六進位（連除法） [cite: 104, 401]"""
    if n == 0: return "0"
    res = ""
    temp = n
    while temp > 0:
        remainder = temp % 16
        res = HEX_CHARS[remainder] + res
        temp //= 16
    return res

def bin_to_dec(b_str: str) -> int:
    """Style 9: 將二進位轉換為十進位（權值相加） [cite: 104, 271, 272]"""
    res = 0
    for i, char in enumerate(b_str[::-1]):
        if char == '1':
            res += (2 ** i)
    return res

def hex_to_dec(h_str: str) -> int:
    """Style 9: 將十六進位轉換為十進位（權值相加） [cite: 104, 494, 500]"""
    res = 0
    h_str = h_str.upper()
    for i, char in enumerate(h_str[::-1]):
        val = HEX_CHARS.find(char)
        res += val * (16 ** i)
    return res

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary / Decimal / Hex Converter")
        
        # 建立 UI 元件 
        tk.Label(root, text="Binary").grid(row=0, column=0)
        tk.Label(root, text="Decimal").grid(row=0, column=1)
        tk.Label(root, text="Hexadecimal").grid(row=0, column=2)
        
        self.entry_bin = tk.Entry(root)
        self.entry_dec = tk.Entry(root)
        self.entry_hex = tk.Entry(root)
        
        self.entry_bin.grid(row=1, column=0, padx=5, pady=5)
        self.entry_dec.grid(row=1, column=1, padx=5, pady=5)
        self.entry_hex.grid(row=1, column=2, padx=5, pady=5)
        
        tk.Button(root, text="Convert", command=self.convert, width=40).grid(row=2, column=0, columnspan=3, pady=5)
        tk.Button(root, text="Clear", command=self.clear, width=40).grid(row=3, column=0, columnspan=3, pady=5)

    def convert(self):
        try:
            # 判斷哪個輸入框有資料並進行轉換
            if self.entry_dec.get():
                val = int(self.entry_dec.get()) # 僅用於讀取輸入文字，非進位轉換
                if val > MAX_VALUE: messagebox.showwarning("加分提醒", "數字已超過255，轉換仍會進行！")
                self.update_fields(val)
            elif self.entry_bin.get():
                val = bin_to_dec(self.entry_bin.get())
                self.update_fields(val)
            elif self.entry_hex.get():
                val = hex_to_dec(self.entry_hex.get())
                self.update_fields(val)
        except Exception as e:
            messagebox.showerror("錯誤", "請輸入有效的數字格式")

    def update_fields(self, decimal_val):
        self.clear()
        self.entry_bin.insert(0, dec_to_bin(decimal_val))
        self.entry_dec.insert(0, str(decimal_val))
        self.entry_hex.insert(0, dec_to_hex(decimal_val))

    def clear(self):
        self.entry_bin.delete(0, tk.END)
        self.entry_dec.delete(0, tk.END)
        self.entry_hex.delete(0, tk.END)

#依各語言不同宣告程式進入點 [cite: 115, 116, 120]
def main():
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
