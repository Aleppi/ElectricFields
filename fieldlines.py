import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

class Field_lines:
    def __init__(self, charges, max_x=5, max_y=5, num_of_lines=10, step=0.05):
        self.charges = charges
        self.max_x = max_x
        self.max_y = max_y
        self.num_of_lines = num_of_lines
        self.step = step
        
    def total_field(self, r):
        total_field = np.zeros(2)
        for n in self.charges:
            r_pos_diff = r - n.pos
            total_field += n.q*r_pos_diff/(la.norm(r_pos_diff)**3)
        return total_field

    def calculate_lines(self):
        with np.errstate(divide='raise', invalid='raise'):
            neg_pos = np.array([i.pos for i in self.charges if i.q < 0])
            lines_arr = []
            if (np.all(np.sign([i.q for i in self.charges]) == np.sign(self.charges[0].q))):
                # All charges have the same sign, so no lines end
                pass 
            for n in self.charges:
                if n.q > 0:
                    for i in range(self.num_of_lines):
                        r = n.pos + np.array([np.cos(i*2*np.pi/self.num_of_lines), np.sin(i*2*np.pi/self.num_of_lines)])*self.step
                        line = [[r[0], r[1]]]
                        while np.abs(r[0]) <= self.max_x and np.abs(r[1]) <= self.max_y:
                            if len(neg_pos):
                                if np.any(np.array([la.norm(i) for i in r-neg_pos]) < self.step):
                                    break
                            with np.errstate(divide='raise', invalid='raise'):
                                try:
                                    r += self.total_field(r)/la.norm(self.total_field(r))*self.step
                                    line.append([r[0], r[1]])
                                except FloatingPointError:
                                    break
                        lines_arr.append(np.array(line))
            lines_arr = np.array(lines_arr)
            return lines_arr
        
    def plot_lines(self):
        fig, ax = plt.subplots()
        ax.set_xlim([-self.max_x, self.max_x])
        ax.set_ylim([-self.max_y, self.max_y])
        lines = self.calculate_lines()
        for i in lines:
            ax.plot(i[:,0], i[:,1], color='black')