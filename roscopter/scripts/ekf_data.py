import numpy as np
import os

f64 = np.float64
Vec3 = (f64, 3)
Vec4 = (f64, 4)
Vec6 = (f64, 6)
XType = np.dtype([
    ('p', Vec3),
    ('q', Vec4)
])

StateType = np.dtype([
	('t', f64),
	('x', XType),
	('v', Vec3),
	('ba', Vec3),
	('bg', Vec3),
	('a', Vec3),
	('w', Vec3),
	('euler', Vec3)
])

CovType = np.dtype([
	('t', f64),
	('P', (f64, (15, 15)))
])

RefType = np.dtype([
	('t', f64),
	('x', XType),
	('euler', Vec3)
])

LlaType = np.dtype([
	('t', f64),
	('hat', Vec3),
	('bar', Vec3)
])

GnssResType = np.dtype([
	('t', f64),
	('r', Vec6),
	('z', Vec6),
	('zhat', Vec6)
])

MocapResType = np.dtype([
	('t', f64),
	('r', Vec6),
	('z', XType),
	('zhat', XType)
])

ZVResType = np.dtype([
	('t', f64),
	('r', Vec4)
])

ImuType = np.dtype([
	('t', f64),
	('a', Vec3),
	('w', Vec3)
])

class Log:
	def __init__(self, prefix):
		self.prefix = prefix
		self.load(prefix)

	def load(self, prefix):
		setattr(self, "x", np.fromfile(os.path.join(prefix, "state.bin"), dtype=StateType))
		setattr(self, "cov", np.fromfile(os.path.join(prefix, "cov.bin"), dtype=CovType))
		setattr(self, "gnssRes", np.fromfile(os.path.join(prefix, "gnss_res.bin"), dtype=GnssResType))
		setattr(self, "mocapRes", np.fromfile(os.path.join(prefix, "mocap_res.bin"), dtype=MocapResType))
		setattr(self, "zvRes", np.fromfile(os.path.join(prefix, "zero_vel_res.bin"), dtype=ZVResType))
		setattr(self, "imu", np.fromfile(os.path.join(prefix, "imu.bin"), dtype=ImuType))
		setattr(self, "lla", np.fromfile(os.path.join(prefix, "lla.bin"), dtype=LlaType))
		setattr(self, "ref", np.fromfile(os.path.join(prefix, "ref.bin"), dtype=RefType))