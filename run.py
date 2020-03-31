from flaskblog import dev_network_mesh
import os

PORT = int(os.environ.get('PORT', '8443'))
app = dev_network_mesh()

if __name__ == '__main__':
    app.run( debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
