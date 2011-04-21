###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import RRDDataSourceInfo
from ZenPacks.zenoss.FtpMonitor.interfaces import IFtpMonitorDataSourceInfo
from ZenPacks.zenoss.FtpMonitor.datasources.FtpMonitorDataSource import FtpMonitorDataSource

def ftpMonitorStatesVocabulary(context):
    return SimpleVocabulary.fromValues(FtpMonitorDataSource.states)


class FtpMonitorDataSourceInfo(RRDDataSourceInfo):
    implements(IFtpMonitorDataSourceInfo)
    timeout = ProxyProperty('timeout')
    cycletime = ProxyProperty('cycletime')
    hostname = ProxyProperty('hostname')
    port = ProxyProperty('port')
    sendString = ProxyProperty('sendString')
    expectString = ProxyProperty('expectString')
    quitString = ProxyProperty('quitString')
    refuse = ProxyProperty('refuse')
    mismatch = ProxyProperty('mismatch')
    maxBytes = ProxyProperty('maxBytes')
    delay = ProxyProperty('delay')
    certificate = ProxyProperty('certificate')
    useSSL = ProxyProperty('useSSL')
    warning = ProxyProperty('warning')
    critical = ProxyProperty('critical')
    
    @property
    def testable(self):
        """
        We can NOT test this datsource against a specific device
        """
        return False
    


