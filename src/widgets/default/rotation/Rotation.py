import matplotlib
from scipy.spatial.transform import Rotation as R
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


class Rotation(FigureCanvasQTAgg):
    required_keys = [('Quaternion', 4)]
    update_interval = 30  # ms

    def __init__(self):
        self.figure = Figure()
        self.origin = [0, 0, 0]
        ax = self.figure.add_subplot(projection='3d')
        ax.set_xlim3d(-1, 1)
        ax.set_ylim3d(-1, 1)
        ax.set_zlim3d(-1, 1)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])
        self.roll = [1, 0, 0]
        self.pitch = [0, 1, 0]
        self.yaw = [0, 0, 1]
        self.quiver = ax.quiver(self.origin, self.origin, self.origin, self.roll, self.pitch, self.yaw,
                                colors=['r', 'g', 'b'], linewidths=3)
        super(Rotation, self).__init__(self.figure)

    def update_data(self, data):
        if data[-1][0] != ():
            rotation_matrix = self.get_rotation_matrix(data[-1][0])
            self.roll = rotation_matrix @ [1, 0, 0]
            self.pitch = rotation_matrix @ [0, 1, 0]
            self.yaw = rotation_matrix @ [0, 0, 1]

    def redraw(self):
        self.quiver.set_segments([[self.origin, self.roll],
                                  [self.origin, self.pitch],
                                  [self.origin, self.yaw]])
        self.figure.canvas.draw()

    def get_rotation_matrix(self, quaternion):
        return R.from_quat(quaternion).as_matrix()