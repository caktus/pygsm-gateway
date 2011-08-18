.. pygsm-gateway documentation master file
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pygsm-gateway
=============

`pygsm-gateway` is a `RapidSMS <https://github.com/rapidsms/rapidsms>`_ backend
or "gateway" that  wraps `PyGSM <https://github.com/rapidsms/pygsm>`_ with a
basic HTTP server, to separate it from the route process and simplify
development.  It works seamlessly with 
`rapidsms-threadless-router <https://github.com/caktus/rapidsms-threadless-router>`_
to help make RapidSMS communicate to gateways purely by HTTP, while still
allowing the use of PyGSM.


Contents:

.. toctree::
   :maxdepth: 2
   
   using

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

