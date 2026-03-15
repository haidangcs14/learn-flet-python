# Flet File Picker (Giải thích dễ hiểu)

## 1. File Picker là gì?

**File Picker** là một service trong Flet cho phép ứng dụng mở trình quản lý file của hệ điều hành để người dùng:

* Chọn file
* Chọn thư mục
* Chọn nơi lưu file

Nói đơn giản:
File Picker giống cửa sổ **Open file / Save file** thường thấy trong các ứng dụng desktop.

---

# 2. Tạo FilePicker

Trước khi sử dụng, cần tạo một đối tượng FilePicker.

```python
import flet as ft

file_picker = ft.FilePicker()
```

Sau đó có thể dùng đối tượng này để mở hộp thoại chọn file.

---

# 3. Các chức năng chính của FilePicker

## 3.1 Chọn file

Mở cửa sổ để người dùng chọn file từ máy.

```python
files = await file_picker.pick_files()
```

Kết quả trả về là **danh sách các file được chọn**.

Cho phép chọn nhiều file:

```python
files = await file_picker.pick_files(allow_multiple=True)
```

---

## 3.2 Lọc loại file

Có thể giới hạn loại file được chọn:

```python
files = await file_picker.pick_files(
    file_type=ft.FilePickerFileType.IMAGE
)
```

Một số loại file:

| Type   | Ý nghĩa                 |
| ------ | ----------------------- |
| ANY    | mọi loại file           |
| IMAGE  | file ảnh                |
| AUDIO  | file âm thanh           |
| VIDEO  | file video              |
| CUSTOM | tự định nghĩa extension |

---

## 3.3 Chọn nơi lưu file

Mở cửa sổ **Save file** để người dùng chọn tên file và vị trí lưu.

```python
path = await file_picker.save_file()
```

Lưu ý:

* Hàm này **chỉ trả về đường dẫn**
* File **không tự được tạo**
* Bạn phải tự ghi dữ liệu vào file

---

## 3.4 Chọn thư mục

Cho phép người dùng chọn một folder.

```python
directory = await file_picker.get_directory_path()
```

Nếu người dùng bấm cancel → trả về `None`.

---

# 4. Thông tin file sau khi chọn

Mỗi file trả về có các thuộc tính:

| Thuộc tính | Ý nghĩa                 |
| ---------- | ----------------------- |
| name       | tên file                |
| path       | đường dẫn file          |
| size       | kích thước file (bytes) |

Ví dụ:

```python
files = await file_picker.pick_files()

for f in files:
    print(f.name)
    print(f.path)
    print(f.size)
```

---

# 5. Upload file trong Flet

Quy trình upload file gồm 3 bước:

```
User chọn file
     ↓
FilePicker.pick_files()

Tạo upload URL
     ↓
page.get_upload_url()

Upload file
     ↓
FilePicker.upload()
```

---

# 6. Upload Storage trong Flet

Sau khi chọn file, bạn cần **nơi lưu file**.

Có 2 cách:

1. Storage có sẵn của Flet
2. Storage bên ngoài (S3, MinIO...)

---

# 7. Storage có sẵn của Flet

Flet cung cấp upload storage nội bộ.

Bạn cần tạo **upload URL**:

```python
upload_url = page.get_upload_url("image.png", 60)
```

Ý nghĩa:

| Tham số   | Ý nghĩa                 |
| --------- | ----------------------- |
| image.png | tên file                |
| 60        | URL có hiệu lực 60 giây |

Đây là **presigned URL** cho phép upload file.

---

# 8. Bật upload storage

Khi chạy app phải khai báo thư mục upload:

```python
ft.run(main, upload_dir="uploads")
```

Cấu trúc project:

```
project/
   main.py
   uploads/
```

Sau khi upload:

```
uploads/
   image.png
```

---

# 9. Upload vào thư mục con

Có thể tạo folder trong storage:

```python
upload_url = page.get_upload_url("users/avatar.png", 600)
```

Kết quả:

```
uploads/
   users/
      avatar.png
```

Nếu folder chưa tồn tại → Flet tự tạo.

---

# 10. Hiển thị file upload trong app

Có thể đặt upload trong thư mục assets.

```python
ft.run(
    main,
    assets_dir="assets",
    upload_dir="assets/uploads"
)
```

Cấu trúc:

```
assets/
   uploads/
      picture.png
```

Sau đó hiển thị:

```python
ft.Image(src="/uploads/picture.png")
```

---

# 11. Dùng storage bên ngoài

Bạn không bắt buộc dùng storage của Flet.

Có thể upload tới:

* AWS S3
* MinIO
* Backblaze
* Wasabi

Chỉ cần tạo **presigned upload URL** từ dịch vụ đó rồi truyền vào `upload()`.

---

# 12. Ví dụ upload file đơn giản

```python
import flet as ft

def main(page: ft.Page):
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    def upload_files(e):
        files = []
        for f in file_picker.result.files:
            files.append(
                ft.FilePickerUploadFile(
                    name=f.name,
                    upload_url=page.get_upload_url(f.name, 600)
                )
            )

        file_picker.upload(files)

    page.add(
        ft.ElevatedButton(
            "Pick files",
            on_click=lambda _: file_picker.pick_files(allow_multiple=True),
        ),
        ft.ElevatedButton("Upload", on_click=upload_files)
    )

ft.run(main, upload_dir="uploads")
```

---

# 13. Tóm tắt

| Chức năng         | Hàm                  |
| ----------------- | -------------------- |
| Chọn file         | pick_files()         |
| Chọn nơi lưu file | save_file()          |
| Chọn thư mục      | get_directory_path() |
| Tạo upload URL    | get_upload_url()     |
| Upload file       | upload()             |
| Thư mục lưu file  | upload_dir           |

---

# Kết luận

**FilePicker trong Flet** là công cụ giúp ứng dụng:

* Chọn file từ máy
* Chọn thư mục
* Chọn nơi lưu file
* Upload file lên storage

Nó hoạt động thông qua **file dialog của hệ điều hành**, giúp người dùng thao tác file dễ dàng trong ứng dụng.
