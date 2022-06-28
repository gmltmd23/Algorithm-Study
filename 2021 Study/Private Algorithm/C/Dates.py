def preprocessDate(dates):
    months = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06",
              "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}
    result = []

    for date in dates:
        date_arr = date.split()
        date_arr[0] = re.findall('\d+', date_arr[0])[0]
        if len(date_arr[0]) == 1:
            date_arr[0] = "0" + date_arr[0]
        date_arr[1] = months[date_arr[1]]
        result.append("-".join(date_arr[::-1]))
    return result