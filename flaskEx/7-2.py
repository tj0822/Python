activate_this = "/var/www/sample_edition/bin/activate_this.py"
exec(open(activate_this).read(), dict(__file__ = activate_this))

import sys
sys.path.insert(0, '/var/www/html/sample')

from hello_world import app as application