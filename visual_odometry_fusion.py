import cv2
import numpy as np

#calculate optical flow from images
def optical_flow (imag1, img2):

    return optical_flow_matrix

# calculate fundamental matrix from optical flow vectors
def estimate_fundamental_matrix(optical_flow_matrix):

    return fundamental_matrix

#calculate Rotation,translation from fundamental matrix
def Decompose_fundamental_matrix(fundamental_matrix):

    return rotation, translation

# code entry point
if __name__ = "__main__":

    # when camera image stream not ended loop
    while(1):
        
        img11 = np.zeros((1920, 1280))
        
        img21 = np.zeros((1920, 1280))
        
        img12 = np.zeros((1920, 1280))
        
        img22 = np.zeros((1920, 1280))
        
        img13 = np.zeros((1920, 1280))
        
        img23 = np.zeros((1920, 1280))
        
        img14 = np.zeros((1920, 1280))
        
        img24 = np.zeros((1920, 1280))

        #fundamental matrix of camera 1 of surround view system
        fundamental_matrix1 = estimate_fundamental_matrix(optical_flow(img11, img21))
        #fundamental matrix of camera 2 of surround view system
        fundamental_matrix2 = estimate_fundamental_matrix(optical_flow(img12, img22))
        #fundamental matrix of camera 3 of surround view system
        fundamental_matrix3 = estimate_fundamental_matrix(optical_flow(img13, img23))
        #fundamental matrix of camera 4 of surround view system
        fundamental_matrix4 = estimate_fundamental_matrix(optical_flow(img14, img24))

        # Odometry data of camera 1
        Rotation1, translation1 = Decompose_fundamental_matrix(fundamental_matrix1)
        # Odometry data of camera 2
        Rotation2, translation2 = Decompose_fundamental_matrix(fundamental_matrix2)
        # Odometry data of camera 3
        Rotation3, translation3 = Decompose_fundamental_matrix(fundamental_matrix3)
        # Odometry data of camera 4
        Rotation4, translation4 = Decompose_fundamental_matrix(fundamental_matrix4)
        
        # scale value -> absolute scale estimation paper based scale value 
        """
         TO BE ANALYZED FROM PAPER: "ABSOLUTE SCALE ESTIMATION AND CORRECTION FROM MONOCULAR CAMERA ODOMETRY" BEFORE IMPLEMENTING HERE
        """

        # make vector from R,t matrices to assign first input of 1st LSTM  cell
        flatten_camera_odometry1 = row_flattent(Rotation1, translation1)
        # make vector from R,t matrices to assign second input of 2nd LSTM  cell
        flatten_camera_odometry2 = row_flattent(Rotation2, translation2)
        # make vector from R,t matrices to assign third input of 3rd LSTM  cell
        flatten_camera_odometry3 = row_flattent(Rotation3, translation3)
        # make vector from R,t matrices to assign fourth input of 4th LSTM  cell
        flatten_camera_odometry4 = row_flattent(Rotation4, translation4)
        
        #  LSTM fusion
        LSTM_cell_1_input = flatten_camera_odometry1
        LSTM_cell_2_input = flatten_camera_odometry2
        LSTM_cell_3_input = flatten_camera_odometry3
        LSTM_cell_4_input = flatten_camera_odometry4

        # forward pass LSTM fusion neural network
        LSTM_output = LSTM_forward_pass(LSTM_cell_1_input, LSTM_cell_2_input, LSTM_cell_3_input, LSTM_cell_4_input)

        # append all estimated Rotation, translation from LSTM fusion neural network
        array_of_fused_odometries.append(LSTM_output)