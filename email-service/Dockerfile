# Sử dụng Python 3.12 làm base image
FROM python:3.12-slim

# Tạo thư mục làm việc trong container
WORKDIR /app

# Copy file yêu cầu vào container
COPY requirements.txt /app/

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn của dự án vào container
COPY . /app/

# Mở cổng ứng dụng (thường là 8000 với FastAPI)
EXPOSE 8000

# Lệnh khởi động ứng dụng
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
