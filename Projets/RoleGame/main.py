from roles.WizardThief import WizardThief
from roles.WarriorThief import WarriorThief
from roles.FakePerson import FakePerson
from roles.PersonInterface import PersonInterface

print(WizardThief.mro())

p = WizardThief('Victor')
print(p.name)
print(p.money)
print(p.position)
p.position = (5, 6)
print(p.position)
# print(p._WizardThief_position)
p.visibility = 10
print(p.visibility)

w = WarriorThief("Henry")
#print(w.name)

#print (issubclass(WarriorThief, PersonInterface))
#print (issubclass(FakePerson, PersonInterface))

# print(dir(WizardThief))

class_methods = [m for m in dir(WizardThief) if not m.startswith("__") and callable(getattr(WizardThief, m))]
# print(class_methods)

def f():
    print("Hello")

df = globals()['f']

print(df())

