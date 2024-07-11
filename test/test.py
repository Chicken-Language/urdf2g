# -*- coding: utf-8 -*-
import re
import antlr4
from gen.xml.XMLLexer import XMLLexer
from gen.xml.XMLParser import XMLParser


urdf = """
<?xml version="1.0"?>
<robot name="simple_robot">

  <!-- Define the base link -->
  <link name="base_link">
    <visual>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <box size="1 1 0.1"/>
      </geometry>
      <material name="gray">
        <color rgba="0.5 0.5 0.5 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <geometry>
        <box size="1 1 0.1"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="1.0"/>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <inertia ixx="0.1" ixy="0.0" ixz="0.0" iyy="0.1" iyz="0.0" izz="0.1"/>
    </inertial>
  </link>

  <!-- Define the second link -->
  <link name="link1">
    <visual>
      <origin xyz="0 0 0.5" rpy="0 0 0"/>
      <geometry>
        <cylinder radius="0.1" length="1.0"/>
      </geometry>
      <material name="blue">
        <color rgba="0 0 1 1"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0.5" rpy="0 0 0"/>
      <geometry>
        <cylinder radius="0.1" length="1.0"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.5"/>
      <origin xyz="0 0 0.5" rpy="0 0 0"/>
      <inertia ixx="0.025" ixy="0.0" ixz="0.0" iyy="0.025" iyz="0.0" izz="0.025"/>
    </inertial>
  </link>

  <!-- Define the joint connecting the base_link and link1 -->
  <joint name="joint1" type="revolute">
    <parent link="base_link"/>
    <child link="link1"/>
    <origin xyz="0 0 0.05" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
    <limit effort="10.0" lower="-1.57" upper="1.57" velocity="1.0"/>
  </joint>

</robot>
"""

# extraneous input '<?xml ' expecting {COMMENT, SEA_WS, '<', PI}
urdf = re.sub(r"<\?xml.*>", "", urdf)


intput = antlr4.InputStream(urdf)
lexer = XMLLexer(intput)
tokens = antlr4.CommonTokenStream(lexer)
parser = XMLParser(tokens)
tree = parser.document()

if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")



