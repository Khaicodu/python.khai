def read_and_process_input_file(input_file_name):
    """
    Đọc dữ liệu từ tệp đầu vào và tính tổng cho mỗi dãy số.
    Trả về tổng của tất cả các số và một danh sách các tổng của mỗi dãy số.
    """
    total_sum = 0
    line_sums = []

    with open(input_file_name, 'r') as fin:
        n = int(fin.readline().strip())  # Đọc số dòng n
        for _ in range(n):
            line = fin.readline().strip()  # Đọc dãy số
            nums = [float(x) for x in line.split()]  # Chuyển dãy số thành danh sách số thực
            line_sum = sum(nums)  # Tính tổng của dãy số
            line_sums.append(line_sum)  # Thêm tổng của dãy vào danh sách
            total_sum += line_sum  # Cập nhật tổng của tất cả các số

    return total_sum, line_sums

def write_output_file(output_file_name, total_sum, line_sums):
    """
    Ghi tổng và các tổng dãy số vào tệp đầu ra.
    """
    with open(output_file_name, 'w') as fout:
        fout.write(f"{total_sum}\n")  # Ghi tổng của tất cả các số
        for line_sum in line_sums:
            fout.write(f"{line_sum}\n")  # Ghi tổng của mỗi dãy số

def main():
    input_file_name = 'fin.txt'
    output_file_name = 'fout.txt'

    total_sum, line_sums = read_and_process_input_file(input_file_name)
    write_output_file(output_file_name, total_sum, line_sums)

      # Hiển thị nội dung của tệp đầu vào
    print("Nội dung của tệp đầu vào (fin.txt):")
    with open(input_file_name, 'r') as fin:
        print(fin.read())

    # Hiển thị nội dung của tệp đầu ra
    print("Nội dung của tệp đầu ra (fout.txt):")
    with open(output_file_name, 'r') as fout:
        print(fout.read())


if __name__ == "__main__":
    main()
