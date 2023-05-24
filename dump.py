import json
import mysql.connector
from datetime import datetime

# Kết nối tới cơ sở dữ liệu MySQL
db = mysql.connector.connect(
    host="localhost",
    user="weather",
    password="123456Pp@",
    database="weatherapi"
)

# Đường dẫn đến các tệp JSON
temperature_file = "temp-18-5.json"
humidity_file = "humidity-18-5.json"

# Đọc dữ liệu từ tệp nhiệt độ (temperature.json)
with open(temperature_file, 'r') as f:
    temperature_data = json.load(f)

# Đọc dữ liệu từ tệp độ ẩm (humidity.json)
with open(humidity_file, 'r') as f:
    humidity_data = json.load(f)

# Tạo con trỏ để thực thi các câu lệnh SQL
cursor = db.cursor()

# Lặp qua dữ liệu nhiệt độ và độ ẩm và chèn vào cơ sở dữ liệu
for temp_record, humid_record in zip(temperature_data, humidity_data):
    temp_value = temp_record['value']
    temp_created_at = temp_record['created_at']
    
    humid_value = humid_record['value1']
    # humid_created_at = humid_record['created_at']
    
    # Chuyển đổi định dạng datetime
    temp_datetime_obj = datetime.strptime(temp_created_at, "%Y-%m-%dT%H:%M:%S.%fZ")
    temp_formatted_datetime = temp_datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    
    # Câu lệnh INSERT để chèn dữ liệu nhiệt độ và độ ẩm vào bảng (không bao gồm cột id)
    
    # Table weather_records
    # sql = "INSERT INTO weather_records (date_time, humidity, temperature) VALUES (%s, %s, %s)"
    # values = (temp_formatted_datetime, humid_value, temp_value)

    # Table fake_records

    sql = "INSERT INTO fake_records (humidity, temperature) VALUES (%s, %s)"
    values = (humid_value, temp_value)
    # Thực thi câu lệnh SQL
    cursor.execute(sql, values)

# Lưu các thay đổi vào cơ sở dữ liệu
db.commit()

# Đóng kết nối
db.close()
