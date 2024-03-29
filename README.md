![alt](https://www.uit.edu.vn/sites/vi/files/banner_uit.png)

# CS336.O11

- Tên môn học : Truy vấn thông tin đa phương tiện
- Lớp : CS336.O11
- Giảng viên: Đỗ Văn Tiến

## Thực hiện bởi nhóm: **3 cô gái mộng mơ**

| STT | Thành viên                                        |   MSSV   |
| :-: | :------------------------------------------------ | :------: |
|  1  | [Nguyen Nguyen Giap](https://github.com/Paignn)   | 21522025 |
|  2  | [Nguyen Bui Thanh Mai](https://github.com/mainbt) | 21522320 |
|  3  | [Le Thi Nhu Y](https://github.com/lethinhuy203)   | 21522818 |

## Mô tả đồ án

Đồ án hướng tới việc tạo một visual search engine trên web app để giúp gia tăng trải nghiệm người dùng trên các trang web thương mại điện tử về thời trang.

### Tech Stack

- Django, SQLite, FAISS, PyTorch

### System Flow

![alt](https://i.ibb.co/X4KT6R7/System-Design-System-Flow.png)

## Repo tree

```bash
.
├── webthoitrang/ (tạm gọi là root của Django Project này)
│   ├── app/
│   ├──   ├── faiss_retrieval/ : Module FAISS
│   ├──   ├── static/ : Các file tĩnh (CSS, images, JavaScript)
│   ├──   ├── utils/ : Module chứa các helper functions
│   ├──   ├── templates/ : Chứa các templates cho app
│   ├──   └── *.py files : Các file xử lý
│   ├── webthoitrang/
│   ├── media/
│   ├──   ├── train/
│   ├──   ├── test/
│   ├──   └── uploaded-images/
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
└── README.md
```

## **Cách cài đặt**

**Important Note**: Lần đầu tiên chạy server thì sẽ tốn thời gian từ 2 phút đến 2 tiếng tùy theo tốc độ mạng để khởi tạo môi trường, install các modules cần thiết. Các lần tiếp theo thì không, vui lòng kiên nhẫn.

### **Chuẩn bị**

    - Cài đặt Git Bash
    - Cài đặt Python version `>= 3.10`
    - Cài đặt PIP version `>= 21.2.x`
    - Bật repo `CS406.O11` và pwd trên terminal của Git Bash đang ở tại đây

### **Cách 1**: Dùng SHELL scripts trên Git Bash

- Không reset database

```
sh ./webthoitrang/run.sh
```

- Reset Database:

```
sh ./webthoitrang/run.sh reset-db
```

### **Cách 2**: Chạy từng bước

#### Setup

- Vào thư mục root của Django project
  ```
  cd webthoitrang/
  ```
- Thiết lập môi trường ảo
  - Windows and MacOS
    ```
    python -m venv venv
    source venv/Scripts/activate
    ```
  - Others: Updating..........
- Install các packages cần thiết
  ```
  pip install -r requirements.txt
  ```
- Download các file indexes
  ```
  gdown 1Xfr6oqZHQrpFOhEqLkt1fuIbSAuxsKgq
  mv fclip_B32* app/faiss_retrieval/indexes
  ```
- Download và unzip `train_set.zip` và `test_set.zip` trong thư mục `media`
  ```
  gdown 1y5xndjRW3iVxL254jYPd6Vm86KuJQ75S
  gdown 1fix1hdVz3cAKv9vXjS1iJl6b6k1f-gjq
  mv *_set.zip media/
  unzip -q media/train_set.zip media/
  unzip -q media/test_set.zip media/
  ```

#### Thực thi server

- Chuẩn bị database (không cần thực hiện hoặc chỉ cần thực hiện lần đầu tiên):
  ```
  python manage.py makemigrations
  python manage.py migrate
  sh reset_db.sh
  ```
- Chạy server (tại thư mục root của Django project này)
  ```
  python manage.py runserver --noreload
  ```

### **Tạo account admin**

    python manage.py createsuperuser

    Và sau đó tạo account
