#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String &msg)
{
    if (msg.data == "start"){
         ROS_INFO("ok");
    }
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "listener");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

  ros::spin();

  return 0;
}
