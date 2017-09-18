# simple example 1

import tensorflow as tf

node1 = tf.constant(3.2, tf.float32)
node2 = tf.constant(4.3, tf.float32)
node3 = tf.add(node1, node2)

sess = tf.Session()

print(sess.run([node1, node2])) # [3.2, 4.3]
print(sess.run(node3)) # 7.5


