# %%
import numpy as np
import datetime
import math
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
%matplotlib qt
plt.style.use('bmh')
from mpl_toolkits import mplot3d

print('Libraries Loaded!')
# %%
# Evo Calculator

def evo_cost(distance, time: datetime.timedelta):

    minutes = math.ceil((time.seconds//60))
    hours = math.ceil(time.seconds // 3600)
    days = math.ceil(time.seconds // 3600 / 24)

    minute_cost = minutes * 0.41
    hour_cost = hours * 14.99
    day_cost = days * 89.99

    time_cost = min(minute_cost, hour_cost, day_cost)

    extras = (days * 1.5 + 1) if hours > 8 else 1

    combined_cost = time_cost + extras

    taxes = combined_cost*0.05 + combined_cost*0.07

    total_cost = combined_cost+taxes
    return round(total_cost,2)



# %%
evo_cost(30, datetime.timedelta(hours=12))
# %%
def modo_cost(distance, time: datetime.timedelta):
    minutes = max(time.seconds/60,1)
    hours = max(time.seconds / 3600,1)
    days = max(time.seconds / 3600 / 24,1)

    hour_cost = hours * 4
    day_cost = days * 48

    time_cost = min(hour_cost, day_cost)

    under_25_cost = min(distance, 25) * 0.4
    over_25_cost = max(distance - 25, 0) * 0.28

    distance_cost = under_25_cost + over_25_cost

    extras = 1.5

    combined_cost = time_cost + distance_cost + extras

    taxes = combined_cost*0.05 + combined_cost*0.07

    time_cost = combined_cost + taxes

    return round(time_cost, 2)
# %%
modo_cost(30, datetime.timedelta(hours=2, minutes=30))
# %%
# list of times and distances
dists = np.arange(10,201, 10)
times = [datetime.timedelta(minutes=30)]
while times[-1] < datetime.timedelta(hours=10):
    times.append(times[-1] + datetime.timedelta(minutes=30))
    
# %%
modo_costs = np.zeros((len(dists),len(times)))
for i, time in enumerate(times):
    for j, dist in enumerate(dists):
        modo_costs[j, i] = modo_cost(dist, time)

times_plotable = [mdates.date2num(datetime.datetime(2020,1,1) + x) for x in times]

X, Y = np.meshgrid(dists, times_plotable)

evo_costs = np.zeros((len(dists),len(times)))
for i, time in enumerate(times):
    for j, dist in enumerate(dists):
        evo_costs[j, i] = evo_cost(dist, time)

# %%
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, modo_costs)
ax.plot_surface(X, Y, evo_costs)
plt.show()

# %%

# %%
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
y = x.copy().T # transpose
z = np.cos(x ** 2 + y ** 2)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
plt.show()