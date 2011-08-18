pygsm-gateway
=============

A `RapidSMS <https://github.com/rapidsms/rapidsms>`_ backend or "gateway" that 
wraps PyGSM with a basic HTTP server, to separate it from the route process and
simplify development.  pygsm-gateway works seamlessly with 
`rapidsms-threadless-router <https://github.com/caktus/rapidsms-threadless-router>`
to help make RapidSMS communicate to gateways purely by HTTP, while still
allowing the use of PyGSM.

Please refer to the `documentation <http://pygsm-gateway.readthedocs.org/>`_ for more details.

Development by `Caktus Consulting Group <http://www.caktusgroup.com/>`_.
