---
layout: page
title: EDP-Planner
description: An Autonomous Object Searching UAV System
img: assets/img/edp.jpg
importance: 5
category: work
---

<div align="justify">
This was also a project I did for my Bachelor Thesis, along with Summer Yiu and Bryant Tang,
which is specifically designed for static object searching.
In which, we designed an edge detector-based local path planner, named EDP, for obstacle avoidance.
Furthermore, the planner is based on naive solution of minimum snap trajectory;
the naive solution is defined in terms of waypoint selection as well as time allocation.
Futhermore, by utilizing state-of-the-art <a href="https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects">YOLO object detector</a>, depth image, and low-pass filter, the static objects are searched. Feel free to check out our code on github!
</div>
<br />


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/edp2.jpg" title="Simulation in Gazebo." class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<br />

### [GitHub](https://github.com/pattylo/EDP-Planner)