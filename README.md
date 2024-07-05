# urdf2g
parser Unified Robot Description Format with Antlr

最近参加了一个公司的ROS培训，看到了 check_urdf 和 urdf_to_graphiz 这两个命令，一瞬间就想到了 Antlr 解析。找了下 ROS 库里的源码——[urdfdom](https://github.com/ros/urdfdom)，看到里面用到是 CPP 写的，闲着没事用 Antlr 实现下，巩固下学到的 Antlr。
