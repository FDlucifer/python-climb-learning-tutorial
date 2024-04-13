# pip install natsort

import os
from natsort import natsorted, realsorted, humansorted, os_sorted

list1 = ['5', '6', '1', '11', '16', '8']

print(sorted(list1))
print(natsorted(list1))

list2 = ['4 ft 2 in', '6 ft 2 in', '1 ft 7 in', '11 ft 8 in', '16 ft 2 in']

print(sorted(list2))
print(natsorted(list2))

list3 = ['version-1.2.3', 'version-2.4', 'version-11.2.8', 'version-12.2', 'version-4.5']

print(sorted(list3))
print(natsorted(list3))
print(realsorted(list3))
print(humansorted(list3))

print(os.listdir('/'))
print(os_sorted(os.listdir('/')))
