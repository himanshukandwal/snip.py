import os, sys
from flask_script import Manager, Server

# append parent module also in the sys.path in order to make it available while py module lookup (win same directory)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tumblelog import app

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

if __name__ == "__main__":
    manager.run()