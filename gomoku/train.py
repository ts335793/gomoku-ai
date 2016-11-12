import tensorflow as tf

from gomoku import networks
from gomoku import replay_ops

tf.app.flags.DEFINE_string('replay_dir', 'data/replays/',
                     'Directory containing the replay files for training.')
tf.app.flags.DEFINE_string('model_dir', 'data/model/',
                     'Directory where the model snapshots will be saved.')
FLAGS = tf.app.flags.FLAGS

def main(_):
  replay_files = tf.matching_files(FLAGS.replay_dir + "*.tfrecords")
  filename_queue = tf.train.string_input_producer(replay_files)
  options = tf.python_io.TFRecordOptions(
      tf.python_io.TFRecordCompressionType.ZLIB)
  reader = tf.TFRecordReader(options=options)
  key, record_string = reader.read(filename_queue)
  features, scores = replay_ops.decode_replays(record_string)

  with tf.variable_scope('value') as value_scope:
    predicted_scores = networks.Value(features)

  supervisor = tf.train.Supervisor(
      logdir=FLAGS.model_dir, save_summaries_secs=120, save_model_secs=300)
  with supervisor.managed_session() as sess:
    print(sess.run(replay_files))
    print(sess.run([features, scores]))

if __name__ == '__main__':
  tf.app.run()
