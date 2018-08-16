import tensorflow as tf

const1 = tf.constant([[1,2,3], [4,5,6]]);
const2 = tf.constant([[7,8,9], [10,11,12]]);

result1 = tf.add(const1, const2);
result2 = tf.subtract(const1, const2);
result3 = tf.multiply(const1, const2);
result4 = tf.divide(const2, const1);

with tf.Session() as sess:
  output1 = sess.run(result1)
  output2 = sess.run(result2)
  output3 = sess.run(result3)
  output4 = sess.run(result4)
  print(output1)

  print(output2)

  print(output3)
  
  print(output4)