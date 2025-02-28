PRECHECKS = {
    'Router': {
        'L0': [
            'tem len 0',
            'ping 255.255.255.255',
            'show ver',
            'show inventory',
            'show platform',
            'show env all',
            'show license status',
            'show controller',
            'show module',
            'show redundancy',
        ],
        'L1': [
            'show interface',
            'show int description',
            'show interface counters',
            'show int status',
            'show int status | count connected',
            'show interface status err',
            'show cdp neighbor',
            'show cdp neighbor detail',
            'show lldp neihbor',
            'show lldp neighbor detail',
        ],
        'L2': [
            'show port-channel summary',
            'show etherchannel summary',
            'show arp | count ARPAcome o'
        ],
        'L3': [
            'show ip int brief',
            'show ip route summary',
            'show ip route ospf',
            'show ip protocol',
            'show ip ospf nei',
            'show ip ospf interface brief',
            'show ip arp',
            'show ip route',
            'show standby brief',
            'show ip policy',
            'show ip bgp all summ',
            'show ip bgp vpnv4 all summary'
        ],
        'Other Checks': [
            'show ip access-list',
            'show run | count access-list',
            'show ntp assoc',
            'show ip dhcp snooping binding',
            'show snmp user',
            'show authentication sessions'
        ],
        'Final Checks': [
            'show run',
            'show startup',
            'show log',
            'show interface counters'
        ]
    },
    'Switch': {
        'L0': [
                'term len 0',
                'ping 255.255.255.255',
                'show version',
                'show inventory',
                'show platform',
                'show env all',
                'show license status',
                'show controller',
                'show stackwise-virtual link',
                'show stackwise-virtual switch 1',
                'show stackwise-virtual switch 2',
                'show stackwise-virtual dual-active-detection',
                'show switch stack-ports summary',
                'show switch stack-ports detail',
                'show switch stack-ring speed',
                'show stack-power',
                'show module',
                'show romvar',
                'show redundancy',
                'show switch detail',
            ],
            'L1 Checks': [
                'show interface',
                'show int description',
                'show interface counters',
                'show int status',
                'show int status | count connected',
                'show interface status err',
                'show cdp neighbor',
                'show cdp neighbor detail',
                'show lldp neihbor',
                'show lldp neighbor detail',
                'show port-channel summary',
                'show etherchannel summary'
            ],
            'L2 Checks': [
                'show vlan',
                'show vtp status',
                'show vtp devices',
                'show mac address-table',
                'show mac address-table | ex Po',
                'show int trunk',
                'show spanning-tree',
                'show spanning-tree vlan XXX',
                'show spanning-tree root',
                'show spanning-tree | count root',
                'show switch detail',
                'show power inline',
                'show power inline detail',
                'show arp | count ARPAcome o',
            ],
            'L3 Checks': [
                'show ip int brief',
                'show ip route summary',
                'show ip route ospf',
                'show ip protocol',
                'show ip ospf nei',
                'show ip ospf interface brief',
                'show ip arp',
                'show ip route',
                'show standby brief',
                'show ip policy',
                'show ip bgp all summary',
                'show ip bgp vpnv4 all summary'
            ],
            'Other Checks': [
                'show ip access-list',
                'show run | count access-list',
                'show ntp assoc',
                'show ip dhcp snooping binding',
                'show snmp user',
                'show authentication sessions'
            ],
            'Final Checks': [
                'show run',
                'show startup',
                'show log',
                'show interface counters'
            ]
    }
}