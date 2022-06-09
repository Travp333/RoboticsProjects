# Complete the following program that will iteratively predict
# and correct based on the distance and speed measurements and
# a given initial state and acceleration by inserting your code
# in the specified spaces below

import numpy as np
from numpy.linalg import inv

# Mean and standard deviation of initial state
x_mu = 4000     # distance
v_mu = 280      # speed
x_sig = 10.0    # uncetainty in distance
v_sig = 10.0    # uncertainty in speed

# measurements and uncertainties in measuring
x_obses = np.array([4260, 4550, 4860, 5110])  # distances
v_obses = np.array([282, 285, 286, 290])      # speeds

obs_x_sig = 25  # uncetainty in distance measuring
obs_v_sig = 6   # uncertainty in speed measuring

dt = 1.0        # time interval to update
ac = 2.0        # Acceleration

p_x_sig = 20.0  # uncetainty in prediting distance
p_v_sig = 5     # uncertainty in predicting speed

# initial state and covariance matrix
# insert your code here
X = np.array([[x_mu], [v_mu]])
COV = np.array([[x_sig**2, 0], [0, v_sig**2]])

# Matrixes A, B, C, u_t
# insert your code here
A = np.array([[1.0, dt], [0,1.0]])
B = np.array([[0.5*dt**2], [dt]])
C = np.identity(2)
u_t = np.array([[p_x_sig**2, 0], [0, p_v_sig**2]])

# Covariance matrix R_t in predicting
# Insert your code here
R_t = np.array([[p_x_sig**2, 0], [0, p_v_sig**2]])

# Covariance matrix Q_t in measuring
# Insert your code here
Q_t = np.array([[obs_x_sig**2, 0], [0, obs_v_sig**2]])

def predict2D(X, COV):
    X_bar = A.dot(X) + B.dot(u_t)
    COV_bar = A.dot(COV).dot(A.T) + R_t
    return X_bar, COV_bar

def correct2D(X_bar, COV_bar, z_t):
    S = C.dot(COV_bar).dot(C.T)+Q_t
    K_t = COV_bar.dot(C.T).dot(inv(S))
    X = X_bar + K_t.dot((z_t - C.dot(X_bar)))
    COV = (np.identity(2) - K_t.dot(C)).dot(COV_bar)
    return X, COV

for i in range(len(x_obses)):
    X_bar, COV_bar = predict2D(X, COV)
    z_t = np.array([[x_obses[i]], [v_obses[i]]])
    X, COV = correct2D(X_bar, COV_bar, z_t)

print (X)
print (COV)