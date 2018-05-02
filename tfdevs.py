import os
import logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
logging.getLogger("tensorflow").setLevel(logging.DEBUG)

import tensorflow as tf
tf.logging.set_verbosity(tf.logging.DEBUG)

from tensorflow.python.client import device_lib

print "\n\n"
print tf.__version__

print device_lib.list_local_devices()

hello = tf.constant('Hello, TensorFlow!')

# Start tf session
sess = tf.Session()

# Run the op

print(sess.run(hello))
