import random
import time

names = ['Sunny', 'Bunny', 'Chinny', 'Vinny']
subjects = ['Python', 'Java', 'Blockchain']


def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        results.append(person)
    return results


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(subjects)
        }
        yield person


# t1 = time.time()
# people = people_list(10000000)
# t2 = time.time()
# print('Took {}'.format(t2-t1))
#
# t1 = time.time()
# people = people_generator(10000000)
# t2 = time.time()
# print('Took {}'.format(t2-t1))

# people = people_generator(10)
# for x in people:
#     print(x)
#
# people = people_list(10)
# print(people)

l=[x*x for x in range(10)]
print(type(l))

g=(x*x for x in range(10000000000000000))
print(type(g))