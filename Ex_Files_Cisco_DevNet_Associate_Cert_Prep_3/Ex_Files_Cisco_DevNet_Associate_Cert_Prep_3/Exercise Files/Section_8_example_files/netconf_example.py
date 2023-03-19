#!/usr/bin/env python3

from ncclient import manager
import xml.dom.minidom

host = "ios-xe-mgmt.cisco.com"
username = "developer"
password = "C1sco12345"
port = 10000

yang_file = "interfaces-ietf.xml"

conn = manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False, device_params={'name': 'default'}, allow_agent=False, look_for_keys=False)

with open(yang_file) as f: 
    output = (conn.get_config('running', f.read()))

print(xml.dom.minidom.parseString(output.xml).toprettyxml())

"""
Example output: 
(venv) $ python netconf_example.py 
<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:7cc4f355-85c3-4649-85f6-53e955aba156">
        <data>
                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                        <interface>
                                <name>GigabitEthernet1</name>
                                <description>MANAGEMENT INTERFACE - DON'T TOUCH ME</description>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
                                <enabled>true</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                        <address>
                                                <ip>10.10.20.48</ip>
                                                <netmask>255.255.255.0</netmask>
                                        </address>
                                </ipv4>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                        <interface>
                                <name>GigabitEthernet2</name>
                                <description>Configured by NETCONF</description>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
                                <enabled>true</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                        <address>
                                                <ip>10.255.255.1</ip>
                                                <netmask>255.255.255.0</netmask>
                                        </address>
                                </ipv4>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                        <interface>
                                <name>GigabitEthernet3</name>
                                <description>Network Interface</description>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
                                <enabled>false</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                        <interface>
                                <name>Loopback1</name>
                                <description>Added with RESTCONF by Edilmar on 15-07-2020. Thanks to David Bombal</description>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                                <enabled>true</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                        <address>
                                                <ip>1.1.1.1</ip>
                                                <netmask>255.255.255.255</netmask>
                                        </address>
                                </ipv4>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                        <interface>
                                <name>Loopback10</name>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                                <enabled>true</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                        <interface>
                                <name>Loopback55</name>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                                <enabled>true</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                        <interface>
                                <name>Loopback66</name>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                                <enabled>true</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                        <address>
                                                <ip>66.66.66.66</ip>
                                                <netmask>255.255.255.255</netmask>
                                        </address>
                                </ipv4>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                        <interface>
                                <name>Loopback77</name>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                                <enabled>true</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                        <address>
                                                <ip>77.77.77.77</ip>
                                                <netmask>255.255.255.255</netmask>
                                        </address>
                                </ipv4>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                        <interface>
                                <name>Loopback99</name>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                                <enabled>true</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                        <interface>
                                <name>Loopback100</name>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                                <enabled>true</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                        <address>
                                                <ip>100.1.1.1</ip>
                                                <netmask>255.255.255.255</netmask>
                                        </address>
                                </ipv4>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                        <interface>
                                <name>Loopback200</name>
                                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                                <enabled>true</enabled>
                                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
                        </interface>
                </interfaces>
        </data>
</rpc-reply>

"""
