import re
class Menu():

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{} menu available from {} to {}".format(self.name,self.start_time,self.end_time)  

  def calculate_bill(self, purchased_items):
    price = []
    for i in purchased_items:
      price.append(self.items[i])
    return sum(price)


brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu('brunch',brunch_items,"11am","4pm")
    
print(brunch)


early_bird_items = {
 'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu('early bird',early_bird_items,"3pm","6pm")

print(early_bird)

dinner_items = {
   'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu('dinner',dinner_items,"5pm","11pm")

print(dinner)

kids_items = {
   'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu('kids',kids_items,"11am","9pm")

print(kids)


print(Menu.calculate_bill(brunch, ['pancakes', 'home fries', 'coffee']))
print(Menu.calculate_bill(early_bird, ['salumeria plate', 'mushroom ravioli (vegan)']))

# Creating the Franchises
class Franchise():

  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return "Adress: {}".format(self.adress)
  
  def available_menus(self, time):
    int_start_times = []
    int_end_times = []
    for i in self.menus:
        start_hour = int(re.match(r'(\d+)', i.start_time).group(1))
        end_hour = int(re.match(r'(\d+)', i.end_time).group(1))
        if 'pm' in i.start_time and start_hour != 12:
            start_hour += 12
        if 'pm' in i.end_time and end_hour != 12:
            end_hour += 12
        if 'am' in i.start_time and start_hour == 12:
            start_hour = 0
        if 'am' in i.end_time and end_hour == 12:
            end_hour = 0
        int_start_times.append(start_hour)
        int_end_times.append(end_hour)

    available_menus = []
    time = int(re.match(r'(\d+)', time).group(1))
    for i in range(len(int_start_times)):
      if time >= int_start_times[i] and time <= int_end_times[i]:
        available_menus.append(self.menus[i])
    return available_menus


flagship_store  = Franchise("1232 West End Road",[brunch,early_bird,dinner,kids])
new_installment = Franchise("12 East Mulberry Street",[brunch,early_bird,dinner,kids])

print(flagship_store.available_menus("12am"))

class Business():

  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises

first_business = Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas = Menu('arepas',arepas_items,"10am","8pm")
arepas_place = Franchise("189 Fitzgerald Avenue",[arepas])
arepas_business = Business("Take a' Arepa",[arepas_place])