"""Para hospedagens que utilizam cPanel e
[Phusion Passenger](https://www.phusionpassenger.com/).
"""

from {{ project_name }} import wsgi

application = wsgi.application
