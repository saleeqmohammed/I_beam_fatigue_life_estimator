# I beam fatigue life estimator

This project is a python implementation of fatigue life estimation for beams, with varying corss sections like aircraft wing spars. The model is based on SN curves and Minor-damage sum. Loading cycles are counted to approppriate frequencies and cycles with rainflow counting algorithm.

## Pre-calculations
Beam design and cross sections are necessary inputs

<img src="images/beam.jpg" height="150px" />
<img src="images/section_A.jpg" height="150px" />
<img src="images/section_B.jpg" height="150px" />
<img src="images/section_C.jpg" height="150px" />


### The testcase uses WISPER air load data

![](images/Figure_1.png)

### Loading calculations
<div style="display:inline-block;">
<img src="images/reredesigned_beam_mesh_0.16m_element.png" width="300px"/>
<p><i>Meshing the beam for FEM analysis</i></p>
</div>
<div style="display:inline-block;">
<img src="images/reredesigned_beam_forces.png" width="300px"/>
<p><i>Load application points</i></p>
</div>

The data needs to be simulated in an FEM software (Ansys Mechanical in this case) to estimate maximum stress and displacement.

#### Von-miesis stress and strain distribution
![](images/von-mieses-Stress_redesigned_animation.gif)
_Equivalent stress disribution animation_
<div style="display:inline-block;">
<img src="images/reredesigned_beam_von-mieses_stress.png" width="300px"/>
<img src="images/Equivalent stress (von-miesis).png" width="300px"/>
<p><i>Von-Miesis stress distribution</i></p>
</div>
<div style="display:inline-block;">
<img src="images/directional_deformation_redesigned_animation.gif" width="600px"/>
<p><i>Directional deformation</i></p>
<div style="display:inline-block;">
<img src="images/Directional deformation along beam.png" width="300px"/>
<p><i>Directional deformation distribution</i></p></div>
<div style="display:inline-block;">
<img src="images/reredesigned_beam_von-miesis_strain.png" width="300px"/>
<p><i>Equivalanet strain distribution</i></p></div>
</div>

 
 **Other material parameters are added as inputs in the script.**

 ## Miscallaneous calculations

