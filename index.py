import matplotlib .pyplot as plt
import psutil as p 
app_name_dict = {}
count = 0
for process in p.process_iter():
    count = count + 1 
    if(count <= 6):
        name = process.name()
        cpu_usage = p.cpu_percent()
        app_name_dict.update({name: cpu_usage})

keymax = max(app_name_dict, key=app_name_dict.get)
keymin = min(app_name_dict, key=app_name_dict.get)


key_min_max = [keymax, keymin]

app = app_name_dict.values()
max_app = max(app)

min_app = min(app)
max_min_list = [max_app, min_app]


plt.figure(figsize=(15, 7))
plt.xlabel("Application")        
plt.ylabel("Usage")
plt.bar(key_min_max, max_min_list, width=0.6, color=("purple", "green"))
plt.show()