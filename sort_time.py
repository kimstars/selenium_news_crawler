from datetime import datetime, timedelta

def convert_relative_time_to_seconds(time_str):
    if 'ngày' in time_str:
        return int(time_str.split()[0]) * 24 * 60 * 60
    elif 'giờ' in time_str:
        return int(time_str.split()[0]) * 60 * 60
    elif 'tuần' in time_str:
        return int(time_str.split()[0]) * 7 * 24 * 60 * 60
    elif 'tháng' in time_str:
        return int(time_str.split()[0]) * 30 * 24 * 60 * 60
    else:
        return 0

def convert_date_str_to_seconds(date_str):
    try:
        date_object = datetime.strptime(date_str, '%d/%m/%Y')
        current_time = datetime.now()
        time_difference = current_time - date_object
        return int(time_difference.total_seconds())
    except ValueError:
        return 0

def sort_time_strings(time_strings):
    def key_function(time_str):
        if '/' in time_str:
            return convert_date_str_to_seconds(time_str)
        else:
            return convert_relative_time_to_seconds(time_str)

    return sorted(time_strings, key=key_function, reverse=True)

# Ví dụ sử dụng
time_strings = ["5 ngày trước", "15 giờ trước", "12 giờ trước", "1 tuần trước", "16 tháng trước", "25/01/2023"]
sorted_times = sort_time_strings(time_strings)

print("Chuỗi thời gian trước khi sắp xếp:", time_strings)
print("Chuỗi thời gian sau khi sắp xếp:", sorted_times)
