# demo3.py
# โปรแกรมตัวอย่าง: คำนวณผลรวมของตัวเลขที่ผู้ใช้ป้อนเข้ามา

def main():
    try:
        # รับค่าจากผู้ใช้
        numbers = input("ป้อนตัวเลขคั่นด้วยช่องว่าง: ").strip()

        # แปลงเป็น list ของจำนวนเต็ม
        num_list = [int(n) for n in numbers.split()]

        # คำนวณผลรวมของตัวเลข
        total = sum(num_list)

        # แสดงผล
        print(f"ผลรวมของ {num_list} คือ {total}")

    except ValueError:
        print("กรุณาป้อนตัวเลขเท่านั้น (คั่นด้วยช่องว่าง)")

if __name__ == "__main__":
    main()