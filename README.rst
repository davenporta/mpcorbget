mpcorbget v1.0.0a7
=======================

This is a tool for planning observations of minor planets. It pulls data from the Minor Planet Center's MPCORB.DAT and its list of observatories and calculates the geocentric and topocentric coordinates of the object.

In addition to calculating coordinates, it provides an api to retrieve and utilize data from the MPC for use in other scripts.

Currently the it does not support asteroids without a permanent designation. I am hoping to implement that in the future.

You can type mpcorbget directly into the command line to run the QuickEphem tool script. Otherwise import mpcorbget. To see a list of objects and their attributes and methods use help("mpcorbget").
