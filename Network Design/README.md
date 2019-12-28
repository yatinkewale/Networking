Designed and implemented a multi-location, inter-networking strategy for a small and stable organization. This
organization currently has 5 locations. Corporate headquarters is located in Boston and Mumbai. The
company is placed at 3 other locations, which are New York, Mumbai, London and Beijing.
• Every office has 250 employees with 85% of redundancy (For IP addresses). As 85% redundancy was required, each company was allocated a /24 ip address with VLSM Technique
• Subnet the 193.168.84.0/19 to distribute the IPs to all locations.\n
• Boston and Mumbai offices have Finance, HR and Technical departments.
• Other offices have HR and Technical departments.
• All the IP addresses inside departments assigned by DHCP server.
• All the DHCP servers are in Technical department.
• Each company switch was configured with VLANs to provide segmentation for different branches.
• Finance cannot be accessed by any other departments but Finance accesses any other
department.
• Two Finance departments access each other.
• All other departments access each other
• Access Lists are used to secure different departments in every location.
• Routing protocol used for the entire network is OSPF.
• For router redundancy HSRP was implemented
• Switch redundancy was implemented at Beijing, New York and London and Spanning tree protocol was used.
