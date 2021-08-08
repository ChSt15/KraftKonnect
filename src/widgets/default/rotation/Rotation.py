import matplotlib
import numpy as np
from matplotlib.animation import TimedAnimation, FuncAnimation
from scipy.spatial.transform import Rotation as Rot

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class Rotation(FigureCanvasQTAgg):
    required_sources = ['x-Axis']
    number_of_sources = len(required_sources)

    def __init__(self):
        self.figure = Figure()
        self.origin = [0, 0, 0]
        # ax = self.figure.add_subplot()
        # TODO Fix warning
        ax = self.figure.gca(projection='3d')
        ax.set_xlim3d(-1.5, 1.5)
        ax.set_ylim3d(-1.5, 1.5)
        ax.set_zlim3d(-1.5, 1.5)
        self.quiver = ax.quiver(self.origin, self.origin, self.origin, [1, 0, 0], [0, 1, 0], [0, 0, 1], colors=['r', 'g', 'b'], linewidths=3)
        # self.quiver = ax.quiver(self.origin, self.origin, [1, 0, 0], [0, 1, 0], [0, 1, 2],
        #   headaxislength=0, headlength=0, linewidth=0.1, width=.005)
        self.i = 0
        super(Rotation, self).__init__(self.figure)

    # Adds Data-points to plot. data must contain tuples with timestamp (x) and value (y).
    def update_data(self, data):
        self.i = self.i +1
        rotation_matrix = self.quaternion_to_rotation_matrix(Rot.from_euler('xyz', [self.i+2, self.i+10, self.i+30], degrees=True).as_quat())#self.quaternion_to_rotation_matrix((0.02, 0.001, 0.005, 0.03))
        self.i += 1
        x = rotation_matrix @ [1, 0, 0]
        y = rotation_matrix @ [0, 1, 0]
        z = rotation_matrix @ [0, 0, 1]
        theta_x = np.arctan2(rotation_matrix[2, 1], rotation_matrix[2, 2])*180/np.pi
        theta_y = np.arctan2(-rotation_matrix[2, 0], np.sqrt(rotation_matrix[2, 1]**2+rotation_matrix[2, 2]**2))*180/np.pi
        theta_z = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0])*180/np.pi
        # self.quiver.set_UVC([x[0], y[0], z[0]], [x[1], y[1], z[1]], [x[2], y[2], z[2]])
        self.quiver.set_segments([[self.origin, x],
                                  [self.origin, y],
                                  [self.origin, z]])
        self.figure.canvas.draw()


    def rotation_matrix_by_angle(self, degree):
        radians = degree / 180 * np.pi
        return np.array([
            [np.cos(radians), -np.sin(radians), 0],
            [np.sin(radians), np.cos(radians), 0],
            [0, 0, 1]
        ])

    def quaternion_to_rotation_matrix(self, quaternion):
        q0, q1, q2, q3 = tuple(quaternion)
        return np.array([
            [2 * (q0 ** 2 + q1 ** 2) - 1, 2 * (q1 * q2 - q0 * q3), 2 * (q1 * q3 + q0 * q2)],
            [2 * (q1 * q2 + q0 * q3), 2 * (q0 ** 2 + q2 ** 2) - 1, 2 * (q2 * q3 - q0 * q1)],
            [2 * (q1 * q3 - q0 * q2), 2 * (q2 * q3 + q0 * q1), 2 * (q0 ** 2 + q3 ** 2) - 1]
        ])
