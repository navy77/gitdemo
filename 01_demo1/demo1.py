# ประกาศว่าจะใช้ไลบรารี requests ก่อน
import requests
import json

# API endpoint ของกรมอุตุนิยมวิทยาญี่ปุ่น (พยากรณ์อากาศโตเกียว) #
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"

try:
    # เข้าถึง API และดึงข้อมูลจริงๆ
    response = requests.get(url)
    
    # แปลงข้อมูลที่ได้รับ (รูปแบบ JSON) เป็นรูปแบบที่ Python สามารถจัดการได้
    weather_data = response.json()
    
    # จัดรูปแบบและแสดงข้อมูล
    publishing_office = weather_data[0]["publishingOffice"]
    report_datetime = weather_data[0]["reportDatetime"]
    target_area = weather_data[0]["timeSeries"][0]["areas"][0]["area"]["name"]
    weather_info = weather_data[0]["timeSeries"][0]["areas"][0]["weathers"][0]

    print(f"หน่วยงานที่ประกาศ: {publishing_office}")
    print(f"วันและเวลาที่ประกาศ: {report_datetime}")
    print(f"พื้นที่เป้าหมาย: {target_area}")
    print(f"สภาพอากาศวันนี้: {weather_info}")

except requests.exceptions.RequestException as e:
    print(f"เกิดข้อผิดพลาดในการสื่อสาร: {e}")
except json.JSONDecodeError:
    print("การแยกวิเคราะห์ข้อมูลสภาพอากาศล้มเหลว")
except Exception as e:
    print(f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")

# หมายเหตุ: ข้อมูลที่ได้รับจาก API อาจมีการเปลี่ยนแปลงตามเวลาจริง และอาจมีโครงสร้างที่แตกต่างกันในบางกรณี ดังนั้นควรตรวจสอบโครงสร้างของข้อมูลที่ได้รับก่อนนำไปใช้งานจริง