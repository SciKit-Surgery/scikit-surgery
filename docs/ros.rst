Using scikit-surgery with ROS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All scikit-surgery modules are Python 3 compatible, so can be used in a ROS2 project.

ROS1 only supports Python 2 modules - some scikit-surgery modules may be compatible, but functionality cannot be guaranteed. 

Publisher/Subscriber example
----------------------------
This is intended to be a short demonstration of how scikit-surgery can be used within a ROS2 project, and assumes that you already have some knowledge of ROS.
Code is based on the `ROS2 Publisher/Subscriber Tutorial <https://index.ros.org/doc/ros2/Tutorials/Writing-A-Simple-Py-Publisher-And-Subscriber/>`_.

We will modify the publisher to transmit an image message, using OpenCV to read the image, and the CvBridge module to convert to a ROS Image message.

Replace the code in `publisher_member_function.py` with:

.. code-block:: python

    import cv2
    import rclpy
    from rclpy.node import Node
    import sys
    from cv_bridge import CvBridge
    from sensor_msgs.msg import Image

    class MinimalPublisher(Node):

        def __init__(self):
            super().__init__('minimal_publisher')
            self.publisher_ = self.create_publisher(Image, 'topic', 10)
            timer_period = 2  # seconds
            self.timer = self.create_timer(timer_period, self.timer_callback)

        def timer_callback(self):

            filename = sys.argv[1]
            img = cv2.imread(filename)
            bridge = CvBridge()
            imgMsg = bridge.cv2_to_imgmsg(img, "bgr8")

            self.publisher_.publish(imgMsg)
            self.get_logger().info('Publishing Image Message')


    def main(args=None):
        rclpy.init(args=args)

        minimal_publisher = MinimalPublisher()

        rclpy.spin(minimal_publisher)

        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        minimal_publisher.destroy_node()
        rclpy.shutdown()


    if __name__ == '__main__':
        main()

The subscriber will be modified to receive the image message, convert it back to an OpenCV type image, and then 
use the scikit-surgeryimage Chessboard Detector, to search for any chessboard corners in the image.

Replace the contents of `subscriber_member_function.py` with:

.. code-block:: python

    import cv2
    import rclpy

    from rclpy.node import Node
    from cv_bridge import CvBridge
    from sensor_msgs.msg import Image

    from sksurgeryimage.calibration.chessboard_point_detector import ChessboardPointDetector

    class MinimalSubscriber(Node):

        def __init__(self):
            super().__init__('minimal_subscriber')
            self.subscription = self.create_subscription(
                Image,
                'topic',
                self.listener_callback,
                10)
            self.subscription  # prevent unused variable warning

            self.detector = ChessboardPointDetector((13, 10), 3)

        def listener_callback(self, msg):
            bridge = CvBridge()
            image = bridge.imgmsg_to_cv2(msg, "bgr8")
            ids, object_points, image_points = self.detector.get_points(image)

            self.get_logger().info('Detected %s points' % len(ids))


    def main(args=None):
        rclpy.init(args=args)

        minimal_subscriber = MinimalSubscriber()

        rclpy.spin(minimal_subscriber)

        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        minimal_subscriber.destroy_node()
        rclpy.shutdown()


    if __name__ == '__main__':
        main()

You will also need to add dependencies for sensor_msgs and cv_bridge to `packages.xml`:

.. code-block::

    <exec_depend>std_msgs</exec_depend>
    <exec_depend>sensor_msgs</exec_depend>

With two terminals open, run a listener node in one:  

``ros2 run py_pubsub listener``

In the other terminal, run the talker node, with an image file as argument:  

``ros2 run py_pubsub talker image.png``

scikit-surgeryimage has some `chessboard data <https://github.com/UCL/scikit-surgeryimage/tree/master/tests/data/calib-ucl-chessboard>`_ that can be used.
The subscriber node will report the number of detected chessboard points. In this example, the publisher is always sending the same image, so the results are always the same e.g.:

.. code-block:: bash

    INFO] [minimal_subscriber]: Detected 130 points
    [INFO] [minimal_subscriber]: Detected 130 points