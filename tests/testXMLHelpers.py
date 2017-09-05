import os
import unittest

from lxml import etree

from snarf_libvirt.xmlHelpers import getDiskImageURLs, getNetworkMacAddr

dir_path = os.path.dirname(os.path.realpath(__file__))


class XMLHelpersTest(unittest.TestCase):
    def setUp(self):
        self.xmlPath = os.path.join(dir_path, 'data', 'oldXMLDisk.xml')
        diskXML = etree.parse(self.xmlPath)
        self.diskXML = diskXML.getroot()
        # self.networkXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLNetwork.xml')).getroot()
        pass

    def testGetDiskImageURLs(self):
        xmlPath = os.path.join(dir_path, 'data', 'oldXMLDisk.xml')
        diskXML = etree.parse(xmlPath)
        diskXML = diskXML.getroot()

        deviceElement = diskXML.find('devices')

        self.assertIsNotNone(deviceElement)

        expectedImageUrls = ['/kvmvols/max/kvmServerFrontEnd/kvmServerFrontEnd.img']

        self.assertEqual(getDiskImageURLs(deviceElement), expectedImageUrls)

    def testGetMultipleDiskImageURLs(self):
        xmlPath = os.path.join(dir_path, 'data', 'oldXMLMultipleDisk.xml')
        diskXML = etree.parse(xmlPath)
        diskXML = diskXML.getroot()

        deviceElement = diskXML.find('devices')

        self.assertIsNotNone(deviceElement)

        expectedImageUrls = ['/kvmvols/max/kvmServerFrontEnd/kvmServerFrontEnd.img', '/kvmvols/max/kvmServerFrontEnd/kvmServerFrontEnd2.img', '/kvmvols/max/kvmServerFrontEnd/kvmServerFrontEnd3.img']

        self.assertEqual(getDiskImageURLs(deviceElement), expectedImageUrls)

    def testGetNoDiskImageURLs(self):
        xmlPath = os.path.join(dir_path, 'data', 'oldXMLNoDisk.xml')
        diskXML = etree.parse(xmlPath)
        diskXML = diskXML.getroot()

        deviceElement = diskXML.find('devices')

        self.assertIsNotNone(deviceElement)

        expectedImageUrls = []

        self.assertEqual(getDiskImageURLs(deviceElement), expectedImageUrls)

    def testGetNetworkAddr(self):
        xmlPath = os.path.join(dir_path, 'data', 'oldXMLNetwork.xml')
        diskXML = etree.parse(xmlPath)
        diskXML = diskXML.getroot()

        deviceElement = diskXML.find('devices')

        self.assertIsNotNone(deviceElement)

        expectedMacAddresses = ['52:54:00:f4:1e:67']

        self.assertEqual(getNetworkMacAddr(deviceElement), expectedMacAddresses)

    def testGetMultipleNetworkAddr(self):
        xmlPath = os.path.join(dir_path, 'data', 'oldXMLMultipleNetwork.xml')
        diskXML = etree.parse(xmlPath)
        diskXML = diskXML.getroot()

        deviceElement = diskXML.find('devices')

        self.assertIsNotNone(deviceElement)

        expectedMacAddresses = ['52:54:00:f4:1e:67', '53:53:03:f3:13:63']

        self.assertEqual(getNetworkMacAddr(deviceElement), expectedMacAddresses)

    def testGetNoNetworkAddr(self):
        xmlPath = os.path.join(dir_path, 'data', 'oldXMLNoNetwork.xml')
        diskXML = etree.parse(xmlPath)
        diskXML = diskXML.getroot()

        deviceElement = diskXML.find('devices')

        self.assertIsNotNone(deviceElement)

        expectedMacAddresses = []

        self.assertEqual(getNetworkMacAddr(deviceElement), expectedMacAddresses)

    def testGetNetworkAddrNew(self):
        xmlPath = os.path.join(dir_path, 'data', 'oldXMLNetworkNEW.xml')
        diskXML = etree.parse(xmlPath)
        diskXML = diskXML.getroot()

        deviceElement = diskXML.find('devices')

        self.assertIsNotNone(deviceElement)

        expectedMacAddresses = ['#####']

        self.assertEqual(getNetworkMacAddr(deviceElement), expectedMacAddresses)

    def testGetNetworkAddrNewAndOld(self):
        xmlPath = os.path.join(dir_path, 'data', 'oldXMLNetworkNEWAndOld.xml')
        diskXML = etree.parse(xmlPath)
        diskXML = diskXML.getroot()

        deviceElement = diskXML.find('devices')

        self.assertIsNotNone(deviceElement)

        expectedMacAddresses = ['#####', '52:54:00:f4:1e:67']

        self.assertEqual(getNetworkMacAddr(deviceElement), expectedMacAddresses)
