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


SciKit-Surgery is developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

scikit-surgery is a collection of packages for the development of Image Guided Surgery systems.

* `scikit-surgerycore`_ - Algorithms/tools common to all scikit-surgery packages
* `scikit-surgeryimage`_ - Image processing algorithms using OpenCV
* `scikit-surgeryvtk`_ - Implements VTK functionality for IGS applications
* `scikit-surgeryutils`_ - Example applications/utilities
* `scikit-surgerycalibration`_ - Calibration algorithms (camera/pointer/ultrasound etc)
* `scikit-surgerysurfacematch`_ - Stereo reconstruction and point cloud matching
* `scikit-surgerytf`_ - IGS models implemented in TensorFlow
* `scikit-surgerytorch`_ - IGS models implemented in PyTorch
* `scikit-surgerynditracker`_ - Interface for Northern Digital (NDI) trackers. Vicra, Spectra, Vega, Aurora.
* `scikit-surgeryarucotracker`_ - Interface for OpenCV ARuCo.
* `scikit-surgeryspeech`_ - Speech/Wakeword detection

Please see `Documentation`_ for further module details.

.. tutorial-start

Tutorials
---------

**scikit-surgeryvtk**

* `How To Use VTKOverlayWindow <https://scikit-surgeryvtk.readthedocs.io/en/latest/tutorials/overlay_widget.html>`_   
* `Distance Fields & Voxelisation <https://scikit-surgeryvtk.readthedocs.io/en/latest/tutorials/voxelisation.html>`_

**Misc Tutorials**

* `Augmented Reality Tutorial 1 <https://scikit-surgerytutorial01.readthedocs.io/en/latest/>`_
* `Augmented Reality Tutorial 2 <https://mphy0026.readthedocs.io/en/latest/summerschool/overlay_demo.html#summerschooloverlay>`_
* `Tutorial on Software Developemnt for Clincal Translation <https://scikit-surgerytutorial02.readthedocs.io/en/latest>`_
* `Camera Calibration <https://mphy0026.readthedocs.io/en/latest/summerschool/camera_calibration_demo.html#summerschoolcameracalibration>`_
* `Make and Calibrate a Pointer <https://mphy0026.readthedocs.io/en/latest/summerschool/pivot_calibration_demo.html#summerschoolpivotcalibration>`_
* `Fiducial Registration Tutorial <https://mphy0026.readthedocs.io/en/latest/summerschool/registration_demo.html#fidregistrationtutorial>`_

**Tutorials Requiring Equipment**

* `Point Based Registration <https://mphy0026.readthedocs.io/en/latest/schedule-2020/workshop-1.html#workshop1pbr>`_
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
.. _`scikit-surgeryimage`: https://github.com/UCL/scikit-surgeryimage
.. _`scikit-surgerycore`: https://github.com/UCL/scikit-surgerycore
.. _`scikit-surgeryvtk`: https://github.com/UCL/scikit-surgeryvtk
.. _`scikit-surgeryutils`: https://github.com/UCL/scikit-surgeryutils
.. _`scikit-surgerytf`: https://github.com/UCL/scikit-surgerytf
.. _`scikit-surgerytorch`: https://github.com/UCL/scikit-surgerytorch
.. _`scikit-surgeryspeech`: https://github.com/UCL/scikit-surgeryspeech
.. _`scikit-surgerynditracker`: https://github.com/UCL/scikit-surgerynditracker
.. _`scikit-surgeryarucotracker`: https://github.com/UCL/scikit-surgeryarucotracker


.. _`scikit-surgerysurfacematch`: https://github.com/UCL/scikit-surgerysurfacematch
.. _`scikit-surgerysurfacecalibration`: https://github.com/UCL/scikit-surgerysurfacecalibration
.. _`common issues`: https://github.com/UCL/scikit-surgery/issues
