# Script-to-sort-images

Khi download các file ảnh trên mạng tên của các ảnh không được được đánh số thứ tự. Điều này gây khó khăn trong việc đếm số ảnh cũng như theo dõi. Mình sẽ thực hiện đánh số các ảnh download về, loại bỏ các ảnh lỗi có `size = 0`. Nếu download đồng loạt các ảnh về, việc lẫn vào trong đó một số ảnh có nội dung không đúng là điều không thể tránh khỏi. Để loại bỏ nó có thể phải đi mở từng ảnh để loại bỏ, hoặc trong quá trình gán nhãn có thể loại bỏ nó. Nếu số lượng ảnh quá nhiều việc làm trên có thể rất mất nhiều thời gian.

Hướng dẫn chạy:
```python
python sort_images.py --source source --destination destination --format .jpg
```
Liên hệ: huytranvan2010@gmail.com
# Tài liệu tham khảo
https://hktsoft.net/ham-format-trong-python/

