#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import roslib; roslib.load_manifest('rospeex_if')
except:
    pass

import rospy
import datetime
import re

# Import other libraries
from rospeex_if import ROSpeexInterface

class Demo(object):
    """ Demo class """
    def __init__(self):
        """ Initializer """
        self._interface = ROSpeexInterface()

    def sr_response(self, message):
        """ speech recognition response callback
        @param message: recognize result (e.g. what time is it ?)
        @type  message: str
        """
        hello = re.compile('(?P<hello>こんにちは)').search(message)
        gdmrg = re.compile('(?P<gdmrg>おはよう)').search(message)
        yes = re.compile('(?P<yes>はい)').search(message)
        no = re.compile('(?P<no>いいえ)').search(message)
        begin = re.compile('(?P<begin>始め)').search(message)
        start = re.compile('(?P<start>開始)').search(message)
        progress = re.compile('(?P<progress>進捗)').search(message)
        danger = re.compile('(?P<danger>危ない)').search(message)

        print 'you said : %s' % message

	f = open('test.yaml','a')
        f.write(message)
	f.write("\n")
        f.close()

        if hello is not None:
	    text = u'こんにちは。'

	elif gdmrg is not None:
	    text = u'おはようございます。'

        elif progress is not None:
	    text = u'進捗頑張って下さい。'

        elif yes is not None:
	    text = u'探索対象者を見つけました。'

        elif no is not None:
	    text = u'ありがとうございます、人違いでした。'

        elif start is not None or begin is not None:
	    text = u'ナビゲーションを開始します。'

        elif danger is not None:
	    text = u'危険を感知しました、一時停止します。'

        # rospeex reply
        print 'rospeex reply : %s' %text
        self._interface.say(text, 'ja', 'nict')

    def run(self):
        """ run ros node """
        # initialize ros node
        rospy.init_node('ss_sr_demo')

        # initialize rospeex
        self._interface.init()
        self._interface.register_sr_response(self.sr_response)
        self._interface.set_spi_config(language='ja',engine='nict')
        rospy.spin()

if __name__ == '__main__':
    try:
        node = Demo()
        node.run()
    except rospy.ROSInterruptException:
        pass
