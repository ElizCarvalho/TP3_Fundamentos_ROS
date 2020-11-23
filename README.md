# TP3 Fundamentos ROS - Comunicação ROS1 e ROS2

[Script em python do talker para ROS1](https://github.com/ElizCarvalho/TP3_Fundamentos_ROS/blob/master/catkin_ws/src/ros1_talker/src/talker.py)

[Script em python do listener para ROS2](https://github.com/ElizCarvalho/TP3_Fundamentos_ROS/blob/master/ros2_ws/src/ros2_package_subs/ros2_package_subs/ros2_node_subs.py)

---

#### > Evidência de comunicação entre ROS1 e ROS2:
![alt text](https://github.com/ElizCarvalho/TP3_Fundamentos_ROS/blob/master/evidencias/ros1-talker%20To%20ros2-listener.png "Evidência de comunicação entre ROS1 e ROS2")

#### > Evidência de comunicação entre ROS1 e ROS2 usando RQT_GRAPH:
![alt text](https://github.com/ElizCarvalho/TP3_Fundamentos_ROS/blob/master/evidencias/ros1-talker%20To%20ros2-listener-RQT_GRAPH.png "Evidência de comunicação entre ROS1 e ROS2 usando RQT_GRAPH")

#### > Evidência de comunicação entre ROS1 e ROS2. Talker em ROS1 e Turtlesim_node em ROS2::
![alt text](https://github.com/ElizCarvalho/TP3_Fundamentos_ROS/blob/master/evidencias/ros1-talker%20To%20ros2-listener-TURTLESIM_NODE_ROS2.png "Evidência de comunicação entre ROS1 e ROS2. Talker em ROS1 e Turtlesim_node em ROS2")

---

### Step by step ->  Criação/Teste de execução: 

##### Terminal 1 (ROSCORE ROS1):
```shell
$ mkdir -p ~/tp3_fund_ros
$ initros1
$ roscore
```
##### Terminal 2 (Talker ROS1):
```shell
$ initros1
$ mkdir -p ~/tp3_fund_ros/catkin_ws/src
$ cd ~/tp3_fund_ros/catkin_ws/src
$ catkin_init_workspace
$ cd ~/tp3_fund_ros/catkin_ws
$ catkin_make
$ echo "source ~/tp3_fund_ros/catkin_ws/devel/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
$ echo $ROS_PACKAGE_PATH
$ cd ~/tp3_fund_ros/catkin_ws/src
$ catkin_create_pkg ros1_talker rospy geometry_msgs
$ cd ~/tp3_fund_ros/catkin_ws/src/ros1_talker/src
$ gedit talker.py 
$ chmod +x talker.py
$ cd ~/tp3_fund_ros/catkin_ws
$ catkin_make
$ source devel/setup.bash
$ rosrun ros1_talker talker.py
```

##### Terminal 3 (Lintener RO2):
```shell
$ initros2
$ sudo apt install python3-colcon-common-extensions
$ mkdir -p ~/tp3_fund_ros/ros2_ws/src
$ cd ~/tp3_fund_ros/ros2_ws/src
$ ros2 pkg create --build-type ament_python --node-name ros2_node_subs ros2_package_subs
$ cd ~/tp3_fund_ros/ros2_ws
$ colcon build
$ . install/local_setup.bash
$ ros2 run ros2_package_subs ros2_node_subs 
```

##### Terminal 4 (BRIDGE):
```shel
$ initros2
$ sudo apt install ros-foxy-ros1-bridge
$ colcon build --symlink-install --packages-select ros1_bridge --cmake-force-configure
$ export ROS_MASTER_URI=http://localhost:11311
$ ros2 run ros1_bridge dynamic_bridge
```

---

### Step by step ->  Execução:

##### Terminal 1 (ROSCORE ROS1):
```shell
$ initros1
$ roscore
```

##### Terminal 2 (Talker ROS1):
```shell
$ initros1
$ cd ~/tp3_fund_ros/catkin_ws/
$ source devel/setup.bash
$ rosrun ros1_talker talker.py
```

##### Terminal 3 (BRIDGE):
```shell
$ initros2
$ export ROS_MASTER_URI=http://localhost:11311
$ ros2 run ros1_bridge dynamic_bridge
```

##### Terminal 4 (Lintener RO2):
```shell
$ initros2
$ cd ~/tp3_fund_ros/ros2_ws/
$ . install/local_setup.bash
$ ros2 run ros2_package_subs ros2_node_subs 
```

##### Terminal 5 (RQT_GRAPH em ROS1):
```shell
$ initros1
$ rosrun rqt_graph rqt_graph
```

##### Terminal 6 (RQT_GRAPH em ROS2):
```shell
$ initros2
$ ros2 run rqt_graph rqt_graph
```

##### Terminal 6 (TURTLESIM_NODE em ROS2):
```shell
$ initros2
$ ros2 run turtlesim turtlesim_node
```



