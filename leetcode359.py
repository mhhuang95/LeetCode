class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.log:
            if timestamp - self.log[message] >= 10:
                self.log[message] = timestamp
                return True
            else:return False
        else:
            self.log[message] = timestamp
            return True