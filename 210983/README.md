# Steps Followed
1). Made the cartpole environment using gym.  
2). Implemented a basic pid control for the output(theta).  
3). The desired value of the output is zero, so the error is the value of theta.  
4). Calculated the integral by adding values of theta on every iteration.  
5). The derivative was given to us by the env observation(angular velocity).  
6). Tuned the PID coefficients by hit and trial.  