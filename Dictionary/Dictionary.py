import sys
from datetime import date
import operator
data = {
    'hotel_name': 'Address Dubai Mall',
    'hotel_id': 1102,
    'hotel_room': 676,
    'date': date.today().strftime("%d/%m/%Y"),
    'room_type': ['Hall', 'Living room', 'Bedroom', 'oyo room '],
    'breakfast_menu': {'Oats Idli', 'Oats Upma', 'Aloo Paratha', 'Dosa', 'Appam', 'Poha'},
    'lunch_menu': {'Masala Bhindi', 'Chana Kulcha', 'Shahi Egg Curry', 'Gujarati Kadhi', 'Allahabad Ki Tehri', 'Low Fat Dahi Chicken', 'Curd, Ridge gourd dry sabji'},
    'earning': {
        'checkin': 234160,
        'breakfast': 65475,
        'lunch': 65332,
        'dinner': 84532
    }
}

print(data)

print(data.keys())
print(data.items())
print(data.get('hotel_name'))
print(data.get('room_type'))
data['dinner']='kuch nahi'
print(data)


for idx, item in enumerate(data.get('room_type'), start=1):
    print(idx, item)

for idx, item in enumerate(data.get('breakfast_menu'), start=1):
    print(idx, item)

print(data.get('hotel_id', 'Not Found'))

print(data.get('earning'))

sort_data = dict(sorted(data.get('earning').items(), key=operator.itemgetter(1), reverse=True))

print(sort_data)

l = data.get('earning')
print(type(l))

sum = 0
for i in data.get('earning').values():
    sum += int(i)
print(sum)

# print(sys.getsizeof(data))

print(sys.argv)

lis = [
    {"name": "Nandini", "age": 18},
    {"name": "Manjeet", "age": 20},
    {"name": "Nikhil" , "age": 19}
]

print(lis)


print(sorted(lis, key=operator.itemgetter('age')))



