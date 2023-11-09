---
layout: page
title: LEDVO
description: LEDVO - "LE"arning "D"ynamic Factors for Optimization-based "V"isual "O"dometry
img: assets/img/ledvo.jpg
importance: 1
redirect:
category: current research
related_publications:
---


<div align="justify">
This research addresses the relative pose estimation problem of aerial vehicles; in particular from the perspective of ground-based sensing and control. Over the years, a wide range of research could be found dealing with this problem, nevertheless, we tackle the problem with no airborne information: through fusing vision, dynamic model, and offboard control inputs. Such adopted method is believed to simplify the communication requirements, while ensuring the estimation robustness, hence further ensure the stability of a offboard control framework. Particularly, we first formulate the problem as a factor graph optimization and restrict the variable size with sliding window. As we depose bideirectional communication, we replace IMU factor with dynamic factor via including the outer-loop control input, which is aided with learning-based model. More information will be released soon.
</div>
<br />
<!-- ### [GitHub](https://github.com/HKPolyU-UAV/ALAN) -->
<br />
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/ledvo_full.jpg" title="The overall motivation and concept of LEDVO." class="img-fluid rounded z-depth-1" %}
    </div>
</div>

