scikit-surgery
===============================

.. image:: https://github.com/UCL/scikit-surgery/raw/master/weiss_logo.png
   :height: 128px
   :width: 128px
   :target: https://github.com/UCL/scikit-surgery

|

.. image:: https://coveralls.io/repos/github/UCL/scikit-surgery/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/UCL/scikit-surgery?branch=master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/scikit-surgery/badge/?version=latest
    :target: http://scikit-surgery.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. introduction-start

SciKit-Surgery is a collection of compact libraries developed for surgical navigation. Individual libraries can
be combined using Python to create clinical applications for translational research. However because each application's requirements are unique the individual SciKit-Surgery libraries are kept independent, enabling them to be maintained, modified and combined in new ways to create new clinical applications. Keeping the libraries independent enables researchers to implement novel algorithms within a small library that can be readily reused and built on by the research community.

A typical clinical application might consist of an imaging source (e.g. `SciKit-SurgeryBK`_ to stream ultrasound images), a tracking source (e.g. `SciKitSurgery-NDITracker`_) to locate the images in space, an image processor (e.g. `SciKit-SurgeryTorch`_) to segment anatomy from the image, and a visualisation layer (e.g. `SciKit-SurgeryVTK`_)

SciKit-Surgery is developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences <http://www.ucl.ac.uk/weiss>`_, part of `University College London (UCL) <http://www.ucl.ac.uk/>`_.

.. introduction-end

.. features-start


Packages
--------

* `scikit-surgerycore <https://github.com/UCL/scikit-surgerycore>`_ - Algorithms/tools common to all scikit-surgery packages
* `scikit-surgeryimage <https://github.com/UCL/scikit-surgeryimage>`_ - Image processing algorithms using OpenCV
* `scikit-surgeryvtk <https://github.com/UCL/scikit-surgeryvtk>`_ - Implements VTK functionality for IGS applications
* `scikit-surgeryutils <https://github.com/UCL/scikit-surgeryutils>`_ - Example applications/utilities
* `scikit-surgerycalibration <https://github.com/UCL/scikit-surgerycalibration>`_ - Calibration algorithms (camera/pointer/ultrasound etc)
* `scikit-surgerysurfacematch <https://github.com/UCL/scikit-surgerysurfacematch>`_ - Stereo reconstruction and point cloud matching
* `scikit-surgerytf <https://github.com/UCL/scikit-surgerytf>`_ - IGS models implemented in TensorFlow
* `scikit-surgerytorch <https://github.com/UCL/scikit-surgerytorch>`_ - IGS models implemented in PyTorch
* `scikit-surgerynditracker <https://github.com/UCL/scikit-surgerynditracker>`_ - Interface for Northern Digital (NDI) trackers. Vicra, Spectra, Vega, Aurora.
* `scikit-surgeryarucotracker <https://github.com/UCL/scikit-surgeryarucotracker>`_ - Interface for OpenCV ARuCo.
* `scikit-surgeryspeech <https://github.com/UCL/scikit-surgeryspeech>`_ - Speech/Wakeword detection

.. features-end

Please see `Documentation`_ for further module details.

.. tutorial-start

Tutorials
---------
Tutorials are split into three groups, those that show how to assemble SciKit-Surgery libraries into an application, those that concentrate on the workings a single application, and those that are aimed at general education in image guided interventions using SciKit-Surgery.

**General Tutorials**

* `Use SciKit-SurgeryUtils and SciKit-SurgeryArUcoTracker to build an AR application using your webcam. <https://scikit-surgerytutorial01.readthedocs.io/en/latest/>`_

**scikit-surgeryvtk**

* `How To Use VTKOverlayWindow <https://scikit-surgeryvtk.readthedocs.io/en/latest/tutorials/overlay_widget.html>`_
* `How To Add Text To VTKOverlayWindow <https://scikit-surgeryvtk.readthedocs.io/en/latest/tutorials/text_overlay.html>`_
* `Using The Rendering Generator <https://scikit-surgeryvtk.readthedocs.io/en/latest/tutorials/rendering_generator.html>`_

* `Distance Fields & Voxelisation <https://scikit-surgeryvtk.readthedocs.io/en/latest/tutorials/voxelisation.html>`_

**Educational Tutorials**

* `Use a ready made application to investigate different ways of presenting augmented reality. <https://mphy0026.readthedocs.io/en/latest/summerschool/overlay_demo.html#summerschooloverlay>`_
* `Improve your impact by creating high quality software implementations of your research. <https://scikit-surgerytutorial02.readthedocs.io/en/latest>`_
* `Camera calibration using your phone or webcam. <https://mphy0026.readthedocs.io/en/latest/summerschool/camera_calibration_demo.html#summerschoolcameracalibration>`_
* `Make and Calibrate a Pointer. <https://mphy0026.readthedocs.io/en/latest/summerschool/pivot_calibration_demo.html#summerschoolpivotcalibration>`_
* `Online Fiducial Registration Tutorial. <https://mphy0026.readthedocs.io/en/latest/summerschool/registration_demo.html#fidregistrationtutorial>`_
* `Point Based Registration using Lego or anatomical phantoms. <https://mphy0026.readthedocs.io/en/latest/schedule-2020/workshop-1.html#workshop1pbr>`_
* `Camera Calibration of Laparoscopes <https://mphy0026.readthedocs.io/en/latest/schedule-2020/workshop-2.html#workshop2cameracalib>`_

.. tutorial-end

Encountering Problems?
-----------------------
Please check list of `common issues`_.

Contributing
------------

Please see the `contributing guidelines`_.


Useful links
------------

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2018 University College London.
scikit-surgery is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://github.com/UCL/scikit-surgery
.. _`Documentation`: https://scikit-surgery.readthedocs.io
.. _`SciKit-Surgery`: https://github.com/UCL/scikit-surgery/wiki
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/UCL/scikit-surgery/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/UCL/scikit-surgery/blob/master/LICENSE
.. _`common issues`: https://github.com/UCL/scikit-surgery/issues
.. _`SciKit-SurgeryBK`: https://github.com/UCL/scikit-surgerybk
.. _`SciKit-SurgeryVTK`: https://github.com/UCL/scikit-surgeryvtk
.. _`SciKitSurgery-NDITracker`: https://github.com/UCL/scikit-surgerynditracker
.. _`SciKit-SurgeryTorch`: https://github.com/UCL/scikit-surgerytorch

