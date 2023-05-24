import mysql.connector
import json
from datetime import datetime

# Thiết lập kết nối MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="weather",
    password="123456Pp@",
    database="weatherapi"
)

# Tạo con trỏ truy cập cơ sở dữ liệu
cursor = connection.cursor()

# Thực hiện truy vấn
query = "SELECT * FROM fake_records"
cursor.execute(query)

# Nhận kết quả truy vấn
results = cursor.fetchall()

# Hàm chuyển đổi datetime thành chuỗi có thể chuyển đổi thành JSON
def datetime_converter(obj):
    if isinstance(obj, datetime):
        return obj.__str__()

# Chuyển đổi kết quả thành danh sách từ điển
data = []
for row in results:
    # Lấy thông tin các cột
    column_names = cursor.column_names
    row_data = dict(zip(column_names, row))
    data.append(row_data)

# Ghi dữ liệu vào tệp JSON
with open('fake_record.json', 'w') as json_file:
    json.dump(data, json_file, indent=4, default=datetime_converter)
