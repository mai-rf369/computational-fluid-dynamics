import matplotlib.cm
import matplotlib.pyplot
import numpy

class Main:
	def __init__(self):
		self.ts = 0.0
		self.te = 10.0
		self.dt = 0.1
		self.xs = 0.0
		self.xe = 1.0
		self.dx = 0.01
		self.c = 0.1
		
		self.nt = None
		self.t = None
		self.nx = None
		self.x = None
		self.u = None
		
		self.initialize()
		self.process()
		self.visualize()
	
	def initialize(self):
		self.nt = int((self.te - self.ts) / self.dt) + 1
		self.t = numpy.linspace(self.ts, self.te, self.nt)
		self.nx = int((self.xe - self.xs) / self.dx) + 1
		self.x = numpy.linspace(self.xs, self.xe, self.nx)
		self.u = numpy.empty((self.nt, self.nx), dtype = float)
		for xc in range(self.nx):
			if (
				xc * self.dx + self.xs >= 0.2
				and
				xc * self.dx + self.xs < 0.4
			):
				self.u[0, xc] = 1.0
			else:
				self.u[0, xc] = 0.0
	
	def process(self):
		for tc in range(1, self.nt):
			for xc in range(1, self.nx - 1):
				self.u[tc, xc] = (
					self.u[tc - 1, xc]
					-
					(self.c * self.dt * (self.u[tc - 1, xc + 1] - self.u[tc - 1, xc - 1])) / (2 * self.dx)
				)
	
	def visualize(self):
		figure = matplotlib.pyplot.figure()
		manager = matplotlib.pyplot.get_current_fig_manager()
		axes = figure.add_subplot(1, 1, 1)
		
		for tc in range(self.nt):
			axes.clear()
			axes.set_title("Time {:.2f}/{:.2f}".format(self.t[tc], self.t[self.nt - 1]))
			axes.set_xlabel("X [m]")
			axes.set_ylabel("U")
			
			axes.plot(self.x, self.u[tc, :], linewidth = 1.0, color = "blue", alpha = 1.0)
			axes.scatter(self.x, self.u[tc, :], marker = "o", s = 5, color = "black", alpha = 1.0)
			
			figure.suptitle("Forward in Time and Centered in Space Scheme")
			figure.tight_layout()
			matplotlib.pyplot.pause(0.01)
			figure.savefig("./animation/image_{}.png".format(tc))

if __name__ == "__main__":
	main = Main()
