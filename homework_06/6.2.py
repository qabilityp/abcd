def format_time(total_seconds):
    if total_seconds < 0 or total_seconds > 8640000:
        print('Erorr')
        return
    days, b = divmod(total_seconds, 24 * 60 * 60)
    hours, b = divmod(b, 60 * 60)
    minutes, seconds = divmod(b, 60)
    if 11 <= days % 100 <= 14:
        print(f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    elif days % 10 == 1:
        print(f"{days} день, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    elif 2 <= days % 10 <= 4:
        print(f"{days} дні, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    else:
        print(f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")


format_time(0)
format_time(224930)
format_time(466289)
format_time(950400)
format_time(1209600)
format_time(1900800)
format_time(8639999)
format_time(22493)
format_time(7948799)
format_time(-1)