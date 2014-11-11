#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

void chatterreqCallback(const std_msgs::String &msg)
{
    ROS_INFO("ok");
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "listener");

  ros::NodeHandle n;

  ros::Subscriber chatterreq_sub = n.subscribe("chatterreq", 1000, chatterreqCallback);

  ros::spin();
/*
  ros::Publisher chatterres_pub = n.advertise<std_msgs::String>("chatterres",1000);

  std_msgs::String msg;

  std::stringstream ss;
  ss << "chatterres: listener to talker";
  msg.data = ss.str();

  chatterres_pub.publish(msg);

  ros::spinOnce();
*/
  return 0;
}
