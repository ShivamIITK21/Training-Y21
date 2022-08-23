# How to run
 1). Create a catkin workspace using **catkin_make** in a suitable directory say, catkin_ws  
 2). Source the setup file using **source devel/setup.bash** or **source devel/setup.zsh** depending on your terminal.  
 3). Move to the workspace and build the packages using **catkin_make**.   
 3). Run **roslaunch gazobo-demo demo.launch** to start the simulation. 
 4). Run **roslaunch two-wheeled-robot_description display.launch** to launch rviz.  
 5). Use the teleop package to control the bot directly using keyboard. In a seperate terminal, run **rosrun teleop_twist_keyboard teleop_twist_keyboard.py**. The map is generated simultaneously in rviz. Also, sensor feed can also be visualized in rviz.

 # Steps followed
 1). Used setup from the previous gazebo task.  
 2). Added code for sensors in the xacro and gazebo files for the robot, added views in rviz for the same.  
 3). Created a gmapping node in the launch file of the robot which subscribes to **twr/laser/scan**.  
 4). Added a map view in rviz and saved the map using **rosrun map_server map_saver -f mymap**.  
