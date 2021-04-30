#!/usr/bin/env python3

"""Tạo ra 1 file chứa n dòng, các dòng lẻ chứa 30 số 1,
các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

Sau khi tạo xong file, return result là list chứa 10 dòng đầu và 10 dòng
cuối theo thứ tự dòng xuất hiện trước đứng trước.
Chú ý: viết code để xử lý được nếu n lớn tùy ý (tức file sau khi tạo ra
có thể tới 20 GB).
Chú ý: n mặc định là 30 triệu dòng.
"""
f = open("big.data", mode="wt")
for i in range(1, 3000000 + 1):    
    if i % 2 != 0:
        f.write("1" * 30)
    else:
        f.write(str(2 * i))
        f.write("\n")
f.close()


