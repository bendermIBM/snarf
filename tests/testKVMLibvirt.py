import os
import unittest

from lxml import etree

from snarf_libvirt import KVMLibvirt

dir_path = os.path.dirname(os.path.realpath(__file__))


class KVMLibvirtTest(unittest.TestCase):
    def setUp(self):
        self.kvmlibvirt = KVMLibvirt('ltickvm5.fpet.pokprv.stglabs.ibm.com', 'root')

    def testNewDiskCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLDisk.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'newXMLDisk.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertTrue(self.kvmlibvirt.compareDiskImages(oldDiskXML, newDiskXML))

    def testRemovedDiskCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLDisk.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'newXMLDiskRemoved.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertTrue(self.kvmlibvirt.compareDiskImages(oldDiskXML, newDiskXML))

    def testSameDiskCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLDisk.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLDisk.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertFalse(self.kvmlibvirt.compareDiskImages(oldDiskXML, newDiskXML))

    def testSameNetworkCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLNetwork.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'newXMLNetwork.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertFalse(self.kvmlibvirt.compareNetworkMac(oldDiskXML, newDiskXML))

    def testNewNetworkCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLNetwork.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'newXMLNetworkNEW.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertTrue(self.kvmlibvirt.compareNetworkMac(oldDiskXML, newDiskXML))

    def testRemovedNetworkCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLNetwork.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'newXMLNetworkRemoved.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertTrue(self.kvmlibvirt.compareNetworkMac(oldDiskXML, newDiskXML))

    def testChangedNetworkCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLNetwork.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'newXMLNetworkChanged.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertTrue(self.kvmlibvirt.compareNetworkMac(oldDiskXML, newDiskXML))

    def testSameMemoryCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLDisk.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'newXMLDisk.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertFalse(self.kvmlibvirt.compareMemory(oldDiskXML, newDiskXML))

    def testDifferentMemoryCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLDisk.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'memChange.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertTrue(self.kvmlibvirt.compareMemory(oldDiskXML, newDiskXML))

    def testDifferentUnitMemoryCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLDisk.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'memGB.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertTrue(self.kvmlibvirt.compareMemory(oldDiskXML, newDiskXML))

    def testSameCPUCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLDisk.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'memGB.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertFalse(self.kvmlibvirt.compareCPU(oldDiskXML, newDiskXML))

    def testDiffCPUCompare(self):
        oldDiskXML = etree.parse(os.path.join(dir_path, 'data', 'oldXMLDisk.xml'))
        oldDiskXML = oldDiskXML.getroot()

        newDiskXML = etree.parse(os.path.join(dir_path, 'data', 'cpuChange.xml'))
        newDiskXML = newDiskXML.getroot()

        self.assertTrue(self.kvmlibvirt.compareCPU(oldDiskXML, newDiskXML))
