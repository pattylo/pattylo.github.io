---
layout: page
title: ESESO-UUV
description: ESESO - Error-State Extended State Observer for Unmanned Underwater Vehicles (UUV)
img: assets/img/uuv.png
importance: 1
redirect:
category: current research
related_publications:
---


<div align="justify">
This research addresses the trajectory tracking problem of an unmanned underwater vehicle (UUV) within 4 degrees of freedom (DOF) subject to external disturbances and measurement noise. An adaptive control framework consisting of an adaptive model predictive control (MPC) and an error- state extended state observer (ESESO) is proposed. The MPC is utilized to stabilize the system while the ESESO is proposed to estimate both the state and the lump disturbance. In contrast to most conventional ESOs, we explicitly formulate a sensor-fusion problem by tracking the error state of the observer. The ESESO feeds back the filtered state to the MPC to achieve the adaptability of the closed-loop system. The stability analysis in the Lyapunov sense for both ESESO and adaptive MPC is conducted, whose asymptotic stability is shown. Sufficient simulation via a semi-physical experiment is conducted to validate the effectiveness and superiority of the proposed control framework.  
</div>
<br />
### [GitHub](https://github.com/HKPolyU-UAV/bluerov2)
<br />
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/eseso_mpc.png" title="BlueRov2" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

