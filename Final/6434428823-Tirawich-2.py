# -*- coding: utf-8 -*-
"""

6434428823 Tirawich Kasemchaiyanan

"""

village = [('zone1', 'S', 20), ('zone1', 'M', 10), ('zone1', 'L', 5), ('zone2'
, 'S', 20), ('zone2', 'M', 25), ('zone3', 'L', 20)]

ip = input('Enter a zone name to view data : ')
zone_list = []
house_list = []
zone = [x[0] for x in village]
if ip not in zone:
    print('Not found')
else:
    for i in range(len(village)):
        if ip == village[i][0]:
            zone_list.append((village[i][1],village[i][2]))
            house_list.append(village[i][2])
    print('List of houses in',ip,':',zone_list)
    print('There are',len(zone_list),'sizes of house in',ip)
    print('There are',sum(house_list),'houses in',ip) 