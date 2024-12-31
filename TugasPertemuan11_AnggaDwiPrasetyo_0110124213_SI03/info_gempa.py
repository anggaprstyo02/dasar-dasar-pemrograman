from gempa import *

print("Hello reporter Wafi mengabarkan")
gempa1 = Gempa(1.2, "Banten", "Sr")
gempa2 = Gempa(6.1, "Palu", "Sr")
gempa3 = Gempa(5.6, "Cianjur", "Sr")
gempa4 = Gempa(3.3, "Jayapura", "Sr")
gempa5 = Gempa(4.4, "Garut", "Sr")

gempa1.dampak()
gempa2.dampak()
gempa3.dampak()
gempa4.dampak()
gempa5.dampak()