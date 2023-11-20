---
layout: page
title: MPC
description: A MPC Controller for Quadrotor UAV
img: assets/img/mpc_project.jpg
importance: 1
category: work
related_publications: jiang2022neural
---

<div align="justify">
A dynamic model that considers both linear and complex nonlinear effects extensively benefits the model-based controller development. However, predicting a detailed aerodynamic model with good accuracy for unmanned aerial vehicles (UAVs) is challenging due to their irregular shape and low Reynolds number behavior. This work proposes an approach to model the full translational dynamics of a quadrotor UAV by a feedforward neural network, which is adopted as the prediction model in a model predictive controller (MPC) for precise position control. The raw flight data are collected by tracking various pre-designed trajectories with PX4 autopilot. The neural network model is trained to predict the linear accelerations from the flight log. The neural network-based model predictive controller is then implemented with the automatic control and dynamic optimization toolkit (ACADO) to achieve real-time online optimization. Software in the loop (SITL) simulation and indoor flight experiments are conducted to verify the controller performance. The results indicate that the proposed controller leads to a 40% reduction in the average trajectory tracking error compared to the traditional PID controller.
</div>
<br />
<div align="justify">
Currently, this MPC controller has been the main controller in our lab, and we open sourced it to the community (I only help with the maintenance). The included functions are: NL-MPC and SYS-ID. My collegue later on included backstepping controller and sliding mode controller. Feel free to try out our code!
</div>
<br />
### [GitHub](https://github.com/HKPolyU-UAV/airo_control_interface)
<br />
### Video
<div align="justify">
<a href="https://www.youtube.com/watch?v=KYH02a_53fs
" target="_blank"><img src="https://img.youtube.com/vi/KYH02a_53fs/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="800" height="600" border="10" /></a>
</div>
<br />
<br />
