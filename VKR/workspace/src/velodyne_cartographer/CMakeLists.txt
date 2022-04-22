
cmake_minimum_required(VERSION 2.8.3)
project(velodyne_cartogtapher)

find_package(catkin 
  REQUIRED 
)
catkin_package()


catkin_install_python(PROGRAMS

   champ_trajectory_1.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
