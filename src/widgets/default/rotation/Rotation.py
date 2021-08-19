import matplotlib
from scipy.spatial.transform import Rotation as R
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


class Rotation(FigureCanvasQTAgg):
    required_sources = ['Roll', 'Pitch', 'Yaw']
    number_of_sources = len(required_sources)
    refresh_rate = 25  # Hz

    def __init__(self):
        self.figure = Figure()
        self.origin = [0, 0, 0]
        # TODO Fix warning
        ax = self.figure.gca(projection='3d')
        ax.set_xlim3d(-1.5, 1.5)
        ax.set_ylim3d(-1.5, 1.5)
        ax.set_zlim3d(-1.5, 1.5)
        self.roll = [1, 0, 0]
        self.pitch = [0, 1, 0]
        self.yaw = [0, 0, 1]
        self.quiver = ax.quiver(self.origin, self.origin, self.origin, self.roll, self.pitch, self.yaw,
                                colors=['r', 'g', 'b'], linewidths=3)
        super(Rotation, self).__init__(self.figure)

    def update_data(self, data):
        rotation_matrix = R.from_euler('xyz', data[-1], degrees=True).as_matrix()
        self.roll = rotation_matrix @ [1, 0, 0]
        self.pitch = rotation_matrix @ [0, 1, 0]
        self.yaw = rotation_matrix @ [0, 0, 1]

    def redraw(self):
        self.quiver.set_segments([[self.origin, self.x],
                                  [self.origin, self.y],
                                  [self.origin, self.z]])
        self.figure.canvas.draw()
