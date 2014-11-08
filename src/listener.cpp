#include "stdio.h"
#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String &msg)
{
    printf("ok");
//  ROS_INFO("I heard: [%s]", msg->data.c_str());
//  if (msg.data == "start"){
//      printf("ok");
//  }
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "listener");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

  ros::spin();

  return 0;
}
