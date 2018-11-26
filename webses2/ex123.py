from mongoengine import Document, StringField, IntField
from ex1mlab import River
import ex1mlab

#Ex1
ex1mlab.connect() # Ket noi den database

#Ex2

river_r = River.objects(continent="Africa")
for r in river_r:
    print(r.name, sep="\n")

#Ex3

river_leng_s = River.objects(continent="S. America", length__lt=1000)
for l in river_leng_s:
    print(l.name, sep = "\n")
