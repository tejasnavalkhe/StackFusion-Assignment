from StackFusion import create_app
from StackFusion.main.views import *
from StackFusion.models import *

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
