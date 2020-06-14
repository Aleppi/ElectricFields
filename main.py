import matplotlib.pyplot as plt

import charge
import fieldlines

poscharge = charge.Charge(1, [-0.5,0])
negcharge = charge.Charge(-1, [0.5,0])

charges = [poscharge, negcharge]
        
l = fieldlines.Field_lines(charges, max_x=2, max_y=2, num_of_lines=20, step=0.05)
l.plot_lines()
plt.show()