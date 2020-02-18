:title: Project
:sortorder: 5

A significant portion of your grade will be assigned based on a multi-week long
project involving the modeling, analysis, and design of a real vibrating
system. You will be paired with a partner and together you must select a
reasonably complex system that can be modeled using planar kinematics and
dynamics.

You will start by suggesting a well-posed question about and/or design criteria
for the system which the simulation and analysis can help you to address. You
will derive the differential equations of motion, study the system by
simulating the system dynamics, and present you results in a well formatted
written report in the form of a Jupyter notebook (or set of) including whatever
charts, tables, figures, and visualizations you may need to clearly communicate
your results.

Many students believe that once the equations are written and the simulation is
completed, the job is finished. Actually, dynamic simulations are merely a tool
to learn about the possible dynamic behaviors that a system can exhibit and how
these dynamics depend on other parameters. They must be used cleverly and
resourcefully to elucidate the behavior of the system. This involves asking the
right questions about the system and understanding which parametric
dependencies are of interest. Usually this will come from some engineering job
requirements and specifications or from some scientific question which one
would like answered (e.g. "Design an antenna deployment system for a
communication satellite which works in the near earth orbit, deploys in less
that 10 sec, ..., etc." or "What are the important parameters which limit the
maximum range of achievable in a throw of the discus and how should it be
launched optimally?").

In this project you will be responsible for generating this project requirement
before writing the simulation to help you answer the question you have asked. A
good, precise statement of an interesting question is every bit as important as
good answer. Indeed, poorly defined or worded questions are often impossible to
answer in a satisfying and fulfilling way.

Basic Project Tasks
===================

- Develop a research question and/or design criteria for the system
- Perform a literature review and report on at least two relevant and useful
  references
- Develop a simple planar free body diagram along with an associated
  mathematical and computational model
- Calculate fundamental modal frequencies and frequency response of the system
- Design inputs to the systems that mimic reality
- Identify parameters (mass, geometry, stiffness, damping, etc.) to investigate
- Simulate the system for the inputs and design changes
- Design your system to answer your question or meet the design criteria

Proposal [Due Friday February 7th]
==================================

Report to the instructors in writing the system of your choice, including a
motivation for the problem, background on how the system works heuristically, a
literature search to identify previous work on this problem, and a relatively
complete discussion of the way you hope to use the vibration simulation to
learn what you have chosen to learn. The proposal should be no more than 3
pages and address these things:

- What do you want to figure out or solve? Propose either a research question
  or some specifications a design should meet.
- Background and literature review of prior related work others have done.
- What are inputs/outputs of the system?
- What are relevant masses/inertias in the system?
- What are flexible elements of the system?
- What dissipates energy in the system?
- Include a basic sketch or schematic of the system with descriptive
  annotation.

Proposal Rubric
---------------

[10] Research question/Design Criteria

- [10] Defined a research question or design criteria
- [5] Research question or design criteria is present but not articulated
  clearly
- [0] Did not define a research question or design criteria

[10] Literature review

- [10] Identified more than two relevant work or extensive discussion of at
  least two
- [5] Identified and discussed at least two relevant works
- [0] Did not look into the literature

[10] System description

- [10] System described from a vibrational and dynamics perspective
- [5] System described but lacking in description of dynamics/vibration
- [0] System not described

[10] Methods description

- [10] Clear plan on how analysis and simulation may be used to answer research
  question
- [5] Plan on how to answer question is murky
- [0] No discussion of how analysis and simulation may be used to answer
  research question or address design criteria

[10] Writing

- [10] Clear, coherent, and well organized
- [5] Writing and organization needs improvement
- [0] Not clear, coherent, or well organized

[10] Contributions

- [10] Very clear that each partner contributed equitably to all aspects of the
  project.
- [5] Need to improve the contributions of one or more members
- [0] Clear that everyone is not contributing equitably

Modeling Report [Due Friday, February 28th]
===========================================

This report will extend your proposal with a detailed description of your model
and a demonstration that it behaves like the real system. The report should be
no longer than 6 pages in total.

The report should include:

- Everything from the proposal (you will receive full points if the feedback is
  addressed, otherwise the grade from the proposal will be used).
- Description of the modeling assumptions, number of degrees of freedom,
  inertial, restorative & dissipative elements and any forcing functions.
- A free body diagram (or diagrams) of your system that indicates the
  generalized coordinates & speeds, important velocities, and applied forces &
  torques.
- A Lagrange derivation of the nonlinear equations of motion using SymPy (start
  with kinetic and potential energy definitions and show the equations of
  motion in explicit nonlinear first order form).
- A demonstration through numerical simulation that the model behaves like the
  real system.
- A short paragraph describing each team members' contributions to this report.

Submit your written report as a PDF alongside a zip file that contains your
functioning Jupyter notebooks (.ipynb), Python (.py), and/or data files. Make
sure that "Kernel > Restart Kernel and Run All Cells" runs without error on any
notebooks before submitting. The instructors should be able to run and inspect
the notebooks.  Make use of Markdown cells with section headings and text to
describe what you are doing in each section of the notebook(s).

Report Rubric
-------------

[10] Proposal

- [10] Proposal included and feedback addressed
- [0-9.9] Proposal grade if not present or feedback not addressed

[10] Model description

- [10] Model fully described
- [5] Model partially described
- [0] Model not described

[10] Free body diagram

- [10] Complete & fully descriptive free body diagram(s)
- [5] Partially descriptive free body diagram(s)
- [0] No free body diagram

[10] Equations of motion

- [10 Exceeds] Correct Lagrange derivation and resulting nonlinear equations of
  motion in explicit first order form
- [5 Meets] Partially correct derivation and resulting nonlinear equations of
  motion
- [0 Does not meet] No derivation and equations of motion

[10] Demonstration of model

- [10 Exceeds] Simulation demonstrates that the model behaves like the real
  system
- [5 Meets] Simulation present but does not necessarily demonstrate the model
  behaves as expected
- [0 Does not meet] No simulation

[10] Writing

- [10] Clear, coherent, and well organized
- [5] Writing and organization needs improvement
- [0] Not clear, coherent, or well organized

[10] Contributions

- [10] Very clear that each partner contributed equitably to all aspects of the
  project.
- [5] Need to improve the contributions of one or more members
- [0] Clear that everyone is not contributing equitably

Final Report [Due Tuesday March 17th]
=====================================

This report will cover the entirety of the project. More will be added to this
section after the modeling report is submitted.

Project Idea Prompts
====================

You may propose your own project idea if you'd like. Each team must choose a
unique project topic with respect to the other teams. Here are some possible
ideas to choose from or to use as inspiration:

Utensil/Tool Design for People with Parkinson's Disease
-------------------------------------------------------

Parkinson's disease often causes uncontrollable shaking. This prevents people
with the disease from performing many daily tasks. For example, it is difficult
to eat with utensils because the vibration in the hand causes the food to fall
from the utensil or not make it into the mouth. There are products that damp
the vibrations in the utensil, for example the `Liftware Steady Spoon`_. The
goal of this project would be to design a utensil or tool that could allow
those with Parkinson's to continue performing the selected task.

.. _Liftware Steady Spoon: https://www.liftware.com/steady/

You will need to characterize the typical motion and vibrations that occur in
the task. The task should be one that can be modeled with a planar model of the
arm, hand, and utensil/tool. The idea would be do design a passive mechanism
with appropriate damping that causes the effector of the utensil to move more
smoothly than that of the shaking input.

Record Player Needle
--------------------

Record players produce sound by vibrating a thin structure, the needle, across
a dimpled surface. The vibration of the needle then has to be transformed into
vibrations of the air to produce sound. The simplest setup can be created by
attaching a vibrating needle to a paper cone that amplifies the air vibration
magnitude. Electronic record players use a voice coil that transforms
mechanical motion into voltage changes in a coil via the Lorentz effect which
is then amplified via the transformation back into the motion of the speaker
diaphragm. This project could explore the design geometry of the needle, the
surface shapes of the record dimpling, the transformation into electric energy,
fatigue constraints, material selection, and/or resonance. It is even possible
to produce sound waves with Python based on our simulations.

Cricket Sound Production
------------------------

Cricket's and other insects produce sound by vibrating elements of their
exoskeletons. This project would involve investing the geometric and material
properties of the exoskeleton elements that are used to make their chirp,
creating a simple model of the mechanism, and designing the model to produce
chirps of frequency and amplitude that match an actual cricket or other insect.

Braking On Cobblestone
----------------------

A cobblestone road is shaped such that a tire (e.g. bicycle tire) doesn't
create a full contact patch between the tire and the road, as it does on a
smooth road. This short article gives some initial ideas about the issues:

https://figshare.com/articles/On_coupling_of_vertical_and_longitudinal_dynamics_of_unsuspended_bicycles/5404942

Here you would develop a model that shows the difference in braking ability and
affects of the vehicle due to the cobblestone road. Once the simulations are
functioning you can turn to designing the suspension, tire, materials, or other
aspects to provide better braking and suspension  performance.

Car, Motorcycle, etc. Traversing Periodic Roads with Active Damping
-------------------------------------------------------------------

Two and four wheel vehicles are often modeled as a "half car" with a rigid body
representing the sprung mass mounted on front and rear suspension elements and
an unsprung mass representing the mass of the wheels. Develop a half car model
and select realistic parameter values for a real vehicle of your choice.
Develop a variety of road inputs for different travel speeds and design a
suspension system that provides a comfortable rider to the passengers and
sufficiently low forces to the vehicle structure. There is also the concept of
the Skyhook damper that could be investigated:

https://en.wikipedia.org/wiki/Active_suspension

Here is a paper that implements a model that would be of interest:

https://pdfs.semanticscholar.org/7f64/a2002cfa48a49161f7eafeb509052d4925fc.pdf

Bouncy Bus Seat
---------------

The driver's seat of buses are typically mounted on special suspension systems
that have large travel. This project could investigate why this is the only
seat with suspension, how should this suspension be designed, data collection
of acceleration of different locations on a bus. You can use a smartphone to
collect angular rate and linear acceleration data different locations on a
Unitrans bus to characterize inputs to seat locations. You would then need to
design a seat suspension system to provide comfortable motion to the driver
and/or passengers.

Here is a related paper:

https://www.sciencedirect.com/science/article/pii/S0307904X13002345

Tuned Mass Damper
-----------------

Tuned mass dampers are often designed and installed in skyscrapers to damp
oscillations due to earthquakes. This project would focus on modeling a
multistory building and designing a tune mass damper to suppress motion from
earthquake-like input vibrations.

https://en.wikipedia.org/wiki/Tuned_mass_damper

https://en.wikipedia.org/wiki/Earthquake_engineering

Energy Harvesting From Waves
----------------------------

Ocean waves provide an oscillation input. If designed correctly a machine that
floats on the surface or that is attached to the sea floor can harvest energy
from the periodic motion of the waves. The moving machine can be coupled to an
electric motor to transform rotational or linear motion into electricity. This
project would investigate a wave energy harvesting device and design it such
that energy can be stored from the "vibrating" ocean waves.

https://en.wikipedia.org/wiki/Wave_power

Design of Front Wheel Suspension in an Automobile
-------------------------------------------------

There are a variety of non-trivial suspension designs for ground vehicles. This
project would select a suspension system that has a reasonably complex
mechanism to model and simulation under realistic road conditions.

Here is a paper some Formula SAE students wrote about their suspension design
that could be a starting point:

https://www.sciencedirect.com/science/article/pii/S1877705816302983

Design and Analysis of a Mountain Bike Suspension
-------------------------------------------------

There are a variety of interesting bicycle suspension designs (see
https://en.wikipedia.org/wiki/Bicycle_suspension for a starting point). This
project would model and investigate a non-trivial mountain bike suspension over
downhill off-road shapes with a goal to provide comfortable traversal of the
rough terrain.

Design of a Tire Balance Machine
--------------------------------

Automobile tires need to be "balanced" to minimized vibrations due to
asymmetries in the mass distribution of the wheel. Autoshop typically have a
machine that spins the wheel and recommends a location and mass size to add to
the wheel to ensure minimal vibration when rotating at speed. This project
would focus on figuring out how this machine works and designing the machine
through a model and simulation.

https://en.wikipedia.org/wiki/Tire_balance

Estimating of the Inertia of a Sports Implement
-----------------------------------------------

It is potentially useful to know the inertia of a sports implement for further
dynamic study. For example, tennis rackets, baseball bats, cricket bats,
bowling balls, etc. all have moments and products of inertia. This project
would be to design a vibrating machine that could automatically estimate the
inertia of a sports implement that is place on a vibrating table. You can see
how Jason has done this with bicycle parts here:

http://moorepants.github.io/dissertation/physicalparameters.html

but this is a labor intensive process. It would be much nicer if the item can
be placed in a machine and vibrated in such a way that doesn't require special
mounting to arrive at the full set of inertia values.

Piezoelectric Hydraulic Pump
----------------------------

Piezoelectric materials are those which convert applied mechanical stress into
electrical signals. These materials are used in a wide array of transducers
(sensors and actuators).

https://en.wikipedia.org/wiki/Piezoelectricity

In this project, you will model a positive displacement piston pump powered by
a piezoelectric stack actuator. The piezoelectric actuator will be driven by a
sinusoidal voltage at a frequency of approximately 1kHz. The pump will consist
of a single piston moving axially in a frictionless bore. Your simulation will
include the mass and stiffness of the pump housing, piston, and fluid, as well
as pressure losses from flow resistance. This study will examine how elements
of mechanical design are driven by the properties and limitations of real
materials. An effective model will aid in the identification of design criteria
that will drive the selection of materials, and the geometry of the final
product.

.. image:: https://objects-us-east-1.dream.io/eng122/2020w/piezo-pump.jpg
   :width: 600px
