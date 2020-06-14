import matplotlib.pyplot as plt

import charge
import fieldlines

poscharge = charge.Charge(0, [-1,0])
negcharge = charge.Charge(-1, [1,0])

charges = [poscharge, negcharge]
        
l = fieldlines.Field_lines(charges, max_x=2, max_y=2, num_of_lines=30, step=0.05)
l.plot()
plt.show()