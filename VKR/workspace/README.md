## ROS workspace 

В данном воркспэйсе находятся основные пакеты для симуляции робота собаки в Gazebo и тестировки разных видов 3D SLAM на базе этой симуляции. 

recuirments (from workspace): 
``` 
rosdep install --from-paths src --ignore-src -r -y
sudo add-apt-repository ppa:borglab/gtsam-release-4.0
sudo apt update
sudo apt install libgtsam-dev libgtsam-unstable-dev
sudo apt install ros-melodic-velodyne-description

```
И не забыть обновать сабмодули