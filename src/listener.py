#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

robot_message = u'message'

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
   
def call(data):
    global robot_message
    robot_message = rospy.loginfo(data.data)
 
def listener():

    global robot_message
    # in ROS, nodes are unique named. If two nodes with the same
    # node are launched, the previous one is kicked off. The 
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaenously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("syscommand", String, callback)

    rospy.Subscriber("syscommand", String, call)
    print "%s" %robot_message

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        
if __name__ == '__main__':
    listener()
