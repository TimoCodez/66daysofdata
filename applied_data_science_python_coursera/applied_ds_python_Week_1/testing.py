# Testing some course jupyter notebook stuff with VSC

# string formatting
import datetime as tm
import time as tm
import datetime as dt
sales_records = {
    'price': 4.20,
    'num_items': 4,
    'person': 'John'
}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_records['person'], sales_records['num_items'],
      sales_records['price'], sales_records['num_items'] * sales_records['price']))
# same as above, but with differently formatted as f string
person = 'Jack'
price = 4.20
num_items = 4

print(f'{person} bought {num_items} item(s) at a price of {price} each for a {num_items * price} total')

# class objects and map()
# example of class


class Person:
    department = 'School of Information'  # a class variable

    def set_name(self, new_name):  # a method
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location


person = Person()
person.set_name('Christopher Brooks')
person.set_location('Ann Arbor, MI, USA')
print('{} live in {} and works in the department {}'.format(
    person.name, person.location, person.department))

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
cheapest

for item in cheapest:
    print(item)


# split using map() function
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
          'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)


print(list(map(split_title_and_name, people)))
