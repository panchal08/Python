from datetime import datetime

# Getting the current date and time
start_dateo = "2022-11-01 00:00:00"
end_dateo = "2022-11-30 23:59:59"

start_dateo=datetime.strptime(start_dateo, "%Y-%m-%d %H:%M:%S")
end_dateo=datetime.strptime(end_dateo, "%Y-%m-%d %H:%M:%S")

dt = datetime.now()

# int(start_dateo.timestamp() * 1000)
# int(end_dateo.timestamp() * 1000)

params = {
            "from": int(start_dateo.timestamp() * 1000),
            "to": int(end_dateo.timestamp() * 1000)
        }

print(params)
