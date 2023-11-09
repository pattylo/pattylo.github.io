---
layout: page
title: LIO-AGV
description: An autonomous AGV equipped with LIDAR
img: assets/img/ugv.jpg
importance: 1
category: fun
---

<div align="justify">
This is a project I did for fun during my leisure time. In particular, I deployed <a href="https://github.com/hku-mars/FAST_LIO">FAST-LIO</a> by Mars-Lab at HKU for state estimation and mapping, and programmed a simple planner and a controller. I also tidied up our controller with <a href="https://global.agilex.ai/">Scout Mini's</a> Gazebo simulation. Below is the GitHub link and the map I built under a bridge under Hong Kong!
</div>

<br />
### [GitHub](https://github.com/HKPolyU-UAV/scout_ros)
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/lidar.png" title="Reciprocal Collision Avoidance." class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<br />
<div align="justify">
Out of curiosity, I also compared LIO with GPS signal near buildings. As the video shown below, due to multipath and NLOS, GPS behaves poorly. And that's why roboticists build SLAM!
</div>

<br />

<div align="justify">
<video width="800" height="600" controls>
  <source src="/assets/video/lidar_gps.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
</div>