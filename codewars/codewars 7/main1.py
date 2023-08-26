def format_duration(seconds):
    if seconds == 0:
        return "now"
    if seconds < 31536000:
        if seconds < 86400:
            if seconds < 3600:
                if seconds < 60:
                    data = [0, 0, 0, 0, seconds]
                data = [0, 0, 0, seconds // 60, seconds % 60]
            data = [
                0,
                0,
                seconds // 3600,
                (seconds % 3600) // 60,
                ((seconds % 3600) % 60),
            ]
        data = [
            0,
            seconds // 86400,
            (seconds % 86400) // 3600,
            ((seconds % 86400) % 3600) // 60,
            ((seconds % 86400) % 3600) % 60,
        ]
    data = [
        seconds // 31536000,
        (seconds // 31536000) // 86400,
        ((seconds % 31536000) % 86400) // 3600,
        (((seconds % 31536000) % 86400) % 3600) // 60,
        (((seconds % 31536000) % 86400) % 3600) % 60,
    ]
    final_string = ""
    positions = ["year", "day", "hour", "minute", "second"]
    for i in range(len(data)):
        if data[i] == 0:
            if i != len(data) - 1:
                continue
        elif data[i] == 1:
            final_string += f"{data[i]} {positions[i]}"
        else:
            final_string += f"{data[i]} {positions[i]}s"
        if i != len(data) - 1:
            non_zero_successors = sum([1 if x != 0 else 0 for x in data[i + 1 :]])
            if non_zero_successors >= 2:
                final_string += ", "
            elif non_zero_successors == 1:
                final_string += " and "
        else:
            return final_string
