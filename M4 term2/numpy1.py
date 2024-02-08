import numpy as np

sales = np.array([[75, 120, 70, 90, 80],
                  [80, 90, 100, 70, 50],
                  [50, 45, 70, 65, 50]])
daily = np.sum(sales, axis = 0)
week = np.sum(sales, axis = 1)

print('Total sales','\n',
      'Monday   ', daily[0], 'Plates','\n',
      'Tuesday  ', daily[1], 'Plates','\n',
      'Wensday  ', daily[2], 'Plates','\n',
      'Thursday ', daily[3], 'Plates','\n',
      'Friday   ', daily[4], 'Plates','\n',
      )

print('Each week individual sales','\n',
      'Fried rice', week[0], 'Plates','\n'
      ' Spaketti  ', week[1], 'Plates','\n'
      ' Steak     ', week[2], 'Plates','\n'
      )

print('Max sales', week[0], 'Plates')