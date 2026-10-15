#!/usr/bin/env python3
"""Generate all 57 CCNA concept map HTML files in @mapamentalinfo visual style."""

import os

OUTPUT_DIR = "/tmp/claude-0/-home-claude/a275c3a6-bafa-5fe9-bbdb-9cf8a5b7f23f/scratchpad/ccna-concept-maps/maps"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def html_map(num, title, core_idea, cols, flow_steps, terminal_lines, checklist_items):
    """Generate a single MAP HTML card."""
    col_html = ""
    for i, col in enumerate(cols, 1):
        items_html = "".join(f"<li>{item}</li>" for item in col["items"])
        col_html += f"""
        <div class="col">
          <div class="col-header">{i}. {col["title"]}</div>
          <ul>{items_html}</ul>
        </div>"""

    flow_html = " ".join(
        f'<div class="flow-box">{s}</div><div class="flow-arrow">→</div>' for s in flow_steps[:-1]
    ) + f'<div class="flow-box">{flow_steps[-1]}</div>' if flow_steps else ""

    terminal_html = "\n".join(terminal_lines)

    check_html = "".join(f'<label><input type="checkbox"> {item}</label>' for item in checklist_items)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MAP {num:02d} – {title}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #f5f0e8;
    min-height: 100vh;
    padding: 20px;
  }}
  .page {{
    max-width: 1100px;
    margin: 0 auto;
    background: #fffdf5;
    border: 2px solid #c8b89a;
    border-radius: 4px;
    box-shadow: 4px 4px 12px rgba(0,0,0,0.15);
    position: relative;
    overflow: hidden;
  }}
  /* Spiral binding holes */
  .spine {{
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 44px;
    background: #e8e0d0;
    border-right: 2px solid #c8b89a;
    z-index: 10;
  }}
  .spine-hole {{
    width: 22px; height: 22px;
    background: #f5f0e8;
    border: 2px solid #b0a090;
    border-radius: 50%;
    margin: 28px auto 0;
  }}
  .content {{
    margin-left: 44px;
    padding: 20px 24px;
  }}
  /* Title bar */
  .map-title {{
    background: #1a1a2e;
    color: #fff;
    font-size: 1.5em;
    font-weight: 800;
    letter-spacing: 1px;
    padding: 12px 18px;
    margin-bottom: 14px;
    border-radius: 3px;
    display: flex;
    align-items: center;
    gap: 14px;
    position: relative;
  }}
  .map-num {{
    background: #e94560;
    color: #fff;
    font-size: 0.75em;
    padding: 3px 10px;
    border-radius: 12px;
    letter-spacing: 2px;
  }}
  /* Core idea sticky */
  .core-idea {{
    position: absolute;
    right: 16px; top: 8px;
    background: #ffd54f;
    color: #333;
    font-size: 0.72em;
    font-weight: 600;
    padding: 10px 14px;
    max-width: 220px;
    border-radius: 3px;
    box-shadow: 3px 3px 6px rgba(0,0,0,0.2);
    line-height: 1.4;
    transform: rotate(1deg);
  }}
  .core-idea strong {{ display: block; font-size: 0.85em; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; color: #b7641a; }}
  /* 4 columns */
  .cols {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-bottom: 14px;
  }}
  .col {{
    border: 2px solid #4caf50;
    border-radius: 4px;
    padding: 10px;
    background: #f9fff9;
  }}
  .col-header {{
    font-weight: 700;
    font-size: 0.82em;
    color: #2e7d32;
    text-transform: uppercase;
    border-bottom: 1px solid #a5d6a7;
    margin-bottom: 8px;
    padding-bottom: 4px;
  }}
  .col ul {{ list-style: none; padding: 0; }}
  .col li {{ font-size: 0.78em; padding: 2px 0 2px 10px; border-left: 3px solid #81c784; margin-bottom: 3px; line-height: 1.4; }}
  /* FLOW section */
  .section-label {{
    font-size: 0.7em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #888;
    margin-bottom: 6px;
    margin-top: 14px;
  }}
  .flow {{
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 4px;
    background: #e3f2fd;
    border: 1px solid #90caf9;
    border-radius: 4px;
    padding: 10px 12px;
    margin-bottom: 10px;
  }}
  .flow-box {{
    background: #1565c0;
    color: #fff;
    font-size: 0.75em;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 4px;
    white-space: nowrap;
  }}
  .flow-arrow {{
    color: #1565c0;
    font-size: 1.2em;
    font-weight: 700;
  }}
  /* TERMINAL section */
  .terminal {{
    background: #0d1117;
    color: #58d68d;
    font-family: 'Courier New', monospace;
    font-size: 0.76em;
    padding: 12px 16px;
    border-radius: 4px;
    margin-bottom: 10px;
    border: 1px solid #30363d;
    white-space: pre;
    overflow-x: auto;
    line-height: 1.6;
  }}
  /* CHECKLIST section */
  .checklist {{
    background: #fff8e1;
    border: 1px solid #ffe082;
    border-radius: 4px;
    padding: 10px 14px;
    display: flex;
    flex-direction: column;
    gap: 5px;
  }}
  .checklist label {{
    font-size: 0.78em;
    display: flex;
    align-items: flex-start;
    gap: 8px;
    cursor: pointer;
    line-height: 1.4;
  }}
  .checklist input {{ margin-top: 2px; flex-shrink: 0; }}
  /* Back link */
  .back {{ margin-top: 14px; font-size: 0.78em; }}
  .back a {{ color: #1565c0; text-decoration: none; }}
  .back a:hover {{ text-decoration: underline; }}
  @media(max-width: 700px) {{
    .cols {{ grid-template-columns: repeat(2, 1fr); }}
    .core-idea {{ position: static; transform: none; margin-bottom: 10px; max-width: 100%; }}
  }}
</style>
</head>
<body>
<div class="page">
  <div class="spine">
    {''.join('<div class="spine-hole"></div>' * 12)}
  </div>
  <div class="content">
    <div class="map-title">
      <span class="map-num">MAP {num:02d}</span>
      {title}
      <div class="core-idea"><strong>Core Idea</strong>{core_idea}</div>
    </div>
    <div class="cols">{col_html}</div>
    <div class="section-label">⬛ Flow</div>
    <div class="flow">{flow_html}</div>
    <div class="section-label">⬛ Terminal</div>
    <div class="terminal">{terminal_html}</div>
    <div class="section-label">✅ Exam Checklist</div>
    <div class="checklist">{check_html}</div>
    <div class="back"><a href="../index.html">← Back to All Maps</a></div>
  </div>
</div>
</body>
</html>"""

# ─────────────────────────────────────────────
# MAP DATA  (57 maps)
# ─────────────────────────────────────────────
MAPS = [
  # ── DOMAIN 1: Network Fundamentals ──────────
  (1, "Network Devices",
   "Each device operates at a specific OSI layer and defines network boundaries.",
   [
     {"title": "End Hosts", "items": ["PCs / Laptops / Servers","IP Phones","Printers & Cameras","Any device with an IP"]},
     {"title": "Switches", "items": ["Layer 2: forwards by MAC","Builds MAC address table","L3 Switch: routes VLANs","Separates collision domains"]},
     {"title": "Routers", "items": ["Forwards by IP address","Connects different networks","Maintains routing table","Default gateway for hosts"]},
     {"title": "Security / Other", "items": ["Firewall: stateful inspection","IDS/IPS: detect/prevent","WLC: manages APs","Load Balancer: distributes traffic"]},
   ],
   ["Frame in","Switch checks MAC table","Known? Forward","Unknown? Flood","Router routes between networks"],
   ["! View ARP / MAC tables","show arp","show mac address-table","show ip route","show interfaces status"],
   ["Switches separate collision domains; Routers separate broadcast domains","Hub = 1 collision domain for ALL ports","Default gateway must be a Router (or L3 Switch) IP","NGFW inspects up to Layer 7"]),

  (2, "OSI & TCP/IP Models",
   "OSI = 7-layer reference model. TCP/IP = 4-layer practical model. Both describe encapsulation.",
   [
     {"title": "OSI Layers 7–5", "items": ["7-App: HTTP FTP DNS SMTP","6-Pres: Encryption Encoding","5-Sess: Session setup/teardown","PDU: Data"]},
     {"title": "OSI Layers 4–3", "items": ["4-Transport: TCP/UDP → Segment","3-Network: IP ICMP → Packet","TCP=reliable UDP=fast","IP header: src/dst/TTL"]},
     {"title": "OSI Layers 2–1", "items": ["2-Data Link: MAC → Frame","1-Physical: Bits cables signals","Switches=L2  Routers=L3","Hub=L1 Firewall=L3-7"]},
     {"title": "TCP/IP 4-Layer", "items": ["4-Application (OSI 5-7)","3-Transport (OSI 4)","2-Internet (OSI 3)","1-Network Access (OSI 1-2)"]},
   ],
   ["App data","+ TCP/UDP hdr = Segment","+ IP hdr = Packet","+ Eth hdr/trl = Frame","→ Bits"],
   ["! Mnemonic top→bottom:","! All People Seem To Need Data Processing","! Bottom→top:","! Please Do Not Throw Sausage Pizza Away"],
   ["TCP = connection-oriented (3-way handshake SYN/SYN-ACK/ACK)","UDP = connectionless, faster, no guarantee","Switches operate at Layer 2; Routers at Layer 3","FCS/CRC at Layer 2 detects errors but does NOT correct them"]),

  (3, "Cables & Interfaces",
   "Physical medium determines speed, distance, and duplex. Match cable to device type.",
   [
     {"title": "Copper UTP", "items": ["Cat5e: 1G/100m","Cat6: 1G/100m (10G short)","Cat6a: 10G/100m","RJ-45 connector"]},
     {"title": "UTP Wiring", "items": ["Straight-through: diff devices","Crossover: same devices","T568A vs T568B","Auto-MDIX: auto-detect"]},
     {"title": "Fiber Optic", "items": ["SMF: long dist, laser, yellow","MMF: short dist, LED, orange","LC connector: small","SC/ST connectors: larger"]},
     {"title": "Speeds", "items": ["Ethernet: 10 Mbps","Fast Eth: 100 Mbps","Gigabit: 1 Gbps","10G/25G/40G/100G: DC"]},
   ],
   ["Choose medium","Check distance","Pick category","Verify duplex","Test connectivity"],
   ["show interfaces GigabitEthernet0/1","show interfaces GigabitEthernet0/1 status","show version   ! shows interface types"],
   ["Straight-through: PC→Switch, Router→Switch","Crossover: Switch→Switch, Router→Router, PC→PC","Auto-MDIX eliminates need to worry about cable type","SMF = longer, laser, yellow  |  MMF = shorter, LED, orange/aqua"]),

  (4, "Ethernet & LAN Switching",
   "Switches learn source MACs and forward/flood based on destination MAC.",
   [
     {"title": "Ethernet Frame", "items": ["Preamble: 7B sync","SFD: 1B start delimiter","Dest/Src MAC: 6B each","EtherType: 2B | FCS: 4B"]},
     {"title": "MAC Address", "items": ["48-bit / 6-byte","First 3B: OUI (vendor)","Last 3B: device unique","Written: AA:BB:CC:DD:EE:FF"]},
     {"title": "Switch Logic", "items": ["Learn: src MAC → port","Forward: known dst unicast","Flood: unknown/broadcast","Age out: default 5 min"]},
     {"title": "Duplex & Speed", "items": ["Full duplex: no CSMA/CD","Half duplex: CSMA/CD active","Speed mismatch = poor perf","Duplex mismatch = collisions"]},
   ],
   ["Frame arrives","Learn src MAC","Dst in table?","Yes → forward","No → flood all ports"],
   ["show mac address-table","show mac address-table dynamic","show mac address-table count","clear mac address-table dynamic"],
   ["Min Ethernet frame = 64B (pad if payload < 46B)","Max Ethernet frame = 1518B (1522 with 802.1Q tag)","FF:FF:FF:FF:FF:FF = broadcast (flood)","FCS detects errors; frame is DROPPED, not corrected"]),

  (5, "IPv4 Addressing",
   "Every host needs a unique IP in its subnet. Subnet mask defines the network boundary.",
   [
     {"title": "Address Classes", "items": ["A: 1-126.x.x.x /8 16M hosts","B: 128-191.x.x /16 65K hosts","C: 192-223.x.x.x /24 254 hosts","D: 224-239 Multicast | E: Exp"]},
     {"title": "Private RFC1918", "items": ["10.0.0.0/8","172.16.0.0/12","192.168.0.0/16","Not routable on internet"]},
     {"title": "Special Addresses", "items": ["127.0.0.1 Loopback","169.254.x.x APIPA","255.255.255.255 Broadcast","0.0.0.0 Unspecified/any"]},
     {"title": "Subnet Masks", "items": ["/24 = 255.255.255.0","/25 = .128 (126 hosts)","/26 = .192 (62 hosts)","Network + Host portions"]},
   ],
   ["IP address","AND subnet mask","→ Network address","Hosts = 2^h − 2","Broadcast = last address"],
   ["! Configure interface","interface GigabitEthernet0/0","ip address 192.168.1.1 255.255.255.0","no shutdown","show ip interface brief"],
   ["Hosts per subnet = 2^host_bits − 2 (subtract network + broadcast)","To find subnet: AND the IP with the subnet mask","APIPA (169.254.x.x) = DHCP failed","Loopback = 127.0.0.0/8, not just 127.0.0.1"]),

  (6, "IPv4 Subnetting",
   "Borrow host bits to create subnets. More subnets = fewer hosts per subnet.",
   [
     {"title": "Subnetting Math", "items": ["Borrow bits from host portion","Subnets = 2^borrowed_bits","Hosts = 2^remaining − 2","Block size = 256 − mask_octet"]},
     {"title": "CIDR Quick Ref", "items": ["/25 → 128 block → 126 hosts","/26 → 64 block → 62 hosts","/27 → 32 block → 30 hosts","/28 → 16 block → 14 hosts"]},
     {"title": "VLSM", "items": ["Variable Length Subnet Mask","Different prefix lengths OK","Assign largest subnet first","Conserves IP address space"]},
     {"title": "Worked: /26", "items": ["192.168.1.0/26","Mask: 255.255.255.192","4 subnets, 62 hosts each","Ranges: .0/.64/.128/.192"]},
   ],
   ["Start with /24","Need X hosts?","Pick prefix","Verify 2^h−2 ≥ X","List subnet ranges"],
   ["! Verify subnets","show ip interface brief","show ip route","ping 192.168.1.1","traceroute 10.0.0.1"],
   ["Block size = 256 − last octet of mask (e.g. /26: 256−192=64)","Subnet ranges step by block size","/31 = P2P links (no network/broadcast — RFC 3021)","VLSM: always allocate largest subnet first"]),

  (7, "IPv6 Fundamentals",
   "IPv6 = 128-bit addresses. No broadcasts. Uses NDP instead of ARP.",
   [
     {"title": "Address Format", "items": ["128 bits / 8 hextets","Colon-hex: 2001:db8::1",":: = contiguous zeros (once)","Leading zeros can be omitted"]},
     {"title": "Address Types", "items": ["Global Unicast: 2000::/3","Link-Local: FE80::/10","Unique Local: FC00::/7","Multicast: FF00::/8"]},
     {"title": "EUI-64", "items": ["Auto-generate interface ID","Split MAC, insert FF:FE","Flip 7th bit (universal bit)","48-bit MAC → 64-bit ID"]},
     {"title": "NDP Replaces ARP", "items": ["Neighbor Solicitation (NS)","Neighbor Advertisement (NA)","Router Solicitation (RS)","Router Advertisement (RA)"]},
   ],
   ["Host boots","RS multicast to FF02::2","Router sends RA","Host gets prefix","EUI-64 or SLAAC address"],
   ["ipv6 unicast-routing","interface GigabitEthernet0/0"," ipv6 address 2001:db8:1::1/64"," ipv6 address FE80::1 link-local","show ipv6 interface brief"],
   ["All IPv6 devices have link-local (FE80::/10) automatically",":: shorthand can only be used ONCE per address","No broadcast in IPv6 — multicast replaces it","NDP uses ICMPv6, not a separate protocol"]),

  (8, "Cisco IOS CLI Basics",
   "IOS has hierarchical modes. Configure → Interface → Exit. Always save config.",
   [
     {"title": "Exec Modes", "items": ["User EXEC: Router>","Privileged EXEC: Router#","Global Config: Router(config)#","Interface: (config-if)#"]},
     {"title": "Navigation", "items": ["enable → privileged EXEC","configure terminal → global config","interface g0/0 → int config","exit / end → step back"]},
     {"title": "Essential Commands", "items": ["show version","show running-config","show interfaces","show ip interface brief"]},
     {"title": "Saving Config", "items": ["copy running-config startup-config","write memory (legacy)","show startup-config","erase startup-config (reset)"]},
   ],
   ["Power on","User EXEC","enable","Privileged EXEC","configure terminal","Global Config"],
   ["hostname SW1","enable secret Cisco123","line vty 0 15"," password Cisco123"," login","service password-encryption"],
   ["Running-config = RAM (lost on reboot). Startup-config = NVRAM (survives reboot)","? = context-sensitive help at any mode","Ctrl+Z = return to privileged EXEC from any mode","Tab = complete command; Up arrow = recall last command"]),

  (9, "Switch Interface Config",
   "Configure speed, duplex, descriptions, and shutdown state on switch interfaces.",
   [
     {"title": "Interface Basics", "items": ["interface GigabitEthernet0/1","description Link to PC-1","speed 1000","duplex full"]},
     {"title": "Interface Ranges", "items": ["interface range f0/1-24","interface range g0/1,g0/3","Applies to all selected","Saves time on bulk config"]},
     {"title": "Status Codes", "items": ["up/up = operational","up/down = protocol issue","down/down = physical issue","admin down = shutdown"]},
     {"title": "Security Basics", "items": ["shutdown unused ports","switchport mode access","no ip address (L2 switch)","errdisable recovery"]},
   ],
   ["Enter interface","Set description","Speed/duplex","no shutdown","Verify status"],
   ["interface GigabitEthernet0/1"," description Link-to-R1"," no shutdown","show interfaces GigabitEthernet0/1","show interfaces status"],
   ["'down/down' often = cable issue or other end is down","'up/down' = physical OK but Layer 2 issue","Always add descriptions — saves hours of troubleshooting","interface range saves time for bulk changes"]),

  (10, "IPv4 Header",
   "IPv4 header has 20 bytes minimum. Key fields: TTL, Protocol, src/dst IP.",
   [
     {"title": "Key Fields", "items": ["Version: 4","IHL: header length (min 20B)","DSCP/ECN: QoS marking","Total Length: header + data"]},
     {"title": "Fragmentation", "items": ["ID: identifies fragments","Flags: DF / MF bits","Fragment Offset: position","MTU default = 1500B"]},
     {"title": "TTL & Protocol", "items": ["TTL: decremented each hop","TTL=0: router drops + ICMP","Protocol: 1=ICMP 6=TCP 17=UDP","Checksum: header only"]},
     {"title": "Addresses", "items": ["Src IP: sender","Dst IP: destination","Both 32-bit","NAT may translate these"]},
   ],
   ["Host creates packet","Sets TTL (128 or 64)","Each router decrements TTL","TTL=0 → dropped","ICMP Time Exceeded sent"],
   ["! Debug IP packet","debug ip packet","! Check TTL in traceroute","traceroute 8.8.8.8","undebug all"],
   ["TTL default: Windows=128, Linux/Cisco=64","DF bit = Don't Fragment — needed for Path MTU Discovery","Protocol field tells receiver what's inside (TCP, UDP, ICMP)","Header checksum protects header only, not payload"]),

  (11, "ARP",
   "ARP resolves IP to MAC on a local subnet. Cached in ARP table.",
   [
     {"title": "ARP Process", "items": ["Host A has IP, needs MAC","Broadcasts ARP request","Target sends unicast reply","Src MAC learned by switch too"]},
     {"title": "ARP Table", "items": ["IP → MAC mapping","Default timeout: ~120s Cisco","show arp on router","show mac address-table on switch"]},
     {"title": "Proxy ARP", "items": ["Router responds with own MAC","For hosts on other subnets","Enabled by default on Cisco","Can cause issues — often disabled"]},
     {"title": "Gratuitous ARP", "items": ["Sender = target IP","Announces IP ownership","Used by FHRP (HSRP/VRRP)","Detects IP conflicts"]},
   ],
   ["Need to send to 192.168.1.10","Check ARP cache","Not found → ARP broadcast","Target replies with MAC","Cache MAC, send frame"],
   ["show arp","show ip arp","clear arp-cache","arp 192.168.1.1 aabb.cc00.1000 arpa  ! static ARP"],
   ["ARP is Layer 2 broadcast — stays within subnet","Router must have ARP entry for each directly-connected host","Proxy ARP lets router answer for remote IPs (use with caution)","Gratuitous ARP used by HSRP active router on failover"]),

  (12, "CDP & LLDP",
   "CDP (Cisco) and LLDP (open standard) discover directly-connected neighbors.",
   [
     {"title": "CDP", "items": ["Cisco proprietary","Layer 2 (Data Link)","Enabled by default","Sends every 60s, holdtime 180s"]},
     {"title": "CDP Info Shared", "items": ["Device ID (hostname)","IP address","Platform / IOS version","Interface and native VLAN"]},
     {"title": "LLDP", "items": ["IEEE 802.1AB standard","Works with non-Cisco devices","Disabled by default on Cisco","lldp run to enable globally"]},
     {"title": "Security Note", "items": ["CDP reveals device details","Disable on edge ports","no cdp run (global)","no cdp enable (interface)"]},
   ],
   ["Enable CDP/LLDP","Devices send multicast","Neighbors populate table","View with show commands","Use for network mapping"],
   ["show cdp neighbors","show cdp neighbors detail","show cdp interface","lldp run","show lldp neighbors"],
   ["CDP runs by default; LLDP must be explicitly enabled","CDP/LLDP only discover DIRECTLY connected neighbors","Disable CDP on interfaces facing untrusted networks","CDP reveals IOS version, IP, platform — security risk on edge"]),

  # ── DOMAIN 2: Network Access ─────────────────
  (13, "VLANs",
   "VLANs segment a single physical switch into multiple broadcast domains.",
   [
     {"title": "VLAN Basics", "items": ["Virtual LAN = broadcast domain","Configured on a switch","VLANs 1-4094 (1 default)","VLAN 1/1002-1005 reserved"]},
     {"title": "Port Modes", "items": ["Access port: one VLAN","Trunk port: multiple VLANs","802.1Q tag: 4-byte insert","Native VLAN: untagged on trunk"]},
     {"title": "VLAN Config", "items": ["vlan 10 → name Sales","switchport mode access","switchport access vlan 10","show vlan brief"]},
     {"title": "Trunk Config", "items": ["switchport mode trunk","switchport trunk native vlan 99","switchport trunk allowed vlan 10,20","DTP: auto/desirable/off"]},
   ],
   ["Create VLAN","Assign access ports","Configure trunks","Tag with 802.1Q","Verify with show vlan"],
   ["vlan 10","  name Sales","interface FastEthernet0/1"," switchport mode access"," switchport access vlan 10","show vlan brief"],
   ["VLAN 1 = default and native VLAN — best practice: change native VLAN","Trunk carries multiple VLANs using 802.1Q tags","Native VLAN frames are NOT tagged on the trunk","VLANs must exist on both sides of a trunk"]),

  (14, "Inter-VLAN Routing",
   "Router-on-a-stick or L3 switch SVIs enable routing between VLANs.",
   [
     {"title": "Router-on-a-Stick", "items": ["One physical link to switch","Sub-interfaces per VLAN","encapsulation dot1Q <vlan>","ip address on each sub-int"]},
     {"title": "SVI (L3 Switch)", "items": ["interface vlan 10","ip address on SVI","ip routing must be enabled","Most efficient for intra-switch"]},
     {"title": "L3 Switch Routed", "items": ["no switchport on L3 port","Acts like a router port","ip routing required","ip default-gateway for mgmt"]},
     {"title": "Comparison", "items": ["ROAS: cheap, 1 link","SVI: fast, no external router","L3 routed port: flexible","SVI preferred in production"]},
   ],
   ["VLAN A host","Sends to default GW","Router sub-int receives","Routes to VLAN B sub-int","Forwards to VLAN B host"],
   ["interface GigabitEthernet0/0.10"," encapsulation dot1Q 10"," ip address 192.168.10.1 255.255.255.0","interface GigabitEthernet0/0.20"," encapsulation dot1Q 20"," ip address 192.168.20.1 255.255.255.0"],
   ["Sub-interface number doesn't have to match VLAN ID (but it's best practice)","ip routing must be enabled on L3 switch for SVIs to route","Native VLAN sub-interface uses 'encapsulation dot1Q X native'","show ip route confirms routing is working"]),

  (15, "STP — Spanning Tree Protocol",
   "STP prevents Layer 2 loops by blocking redundant paths. One root bridge per VLAN.",
   [
     {"title": "STP Election", "items": ["Elect Root Bridge (lowest BID)","BID = Priority + MAC address","Default priority: 32768","Non-root: find best path to root"]},
     {"title": "Port Roles", "items": ["Root Port: best path to root","Designated Port: forwarding on seg","Blocked Port: loop prevention","1 RP per non-root switch"]},
     {"title": "Port States", "items": ["Blocking (15s) → Listening (15s)","→ Learning (15s) → Forwarding","Total convergence: ~30-50s","Disabled = admin shutdown"]},
     {"title": "BPDU & Timers", "items": ["Hello: 2s","Max Age: 20s","Forward Delay: 15s","BPDUs exchanged between bridges"]},
   ],
   ["All switches send BPDUs","Elect root bridge","Each switch finds RP","Block redundant ports","Network is loop-free"],
   ["spanning-tree vlan 1 priority 0     ! make root","show spanning-tree","show spanning-tree vlan 10","spanning-tree portfast   ! access ports"],
   ["Lower priority = preferred root bridge (priority in increments of 4096)","Root bridge has ALL ports as Designated (forwarding)","PortFast bypasses listening/learning — use ONLY on access ports","Never enable PortFast on trunk ports (creates loops)"]),

  (16, "RSTP & Rapid Spanning Tree",
   "RSTP (802.1w) converges in ~1-2 seconds vs 30-50s for classic STP.",
   [
     {"title": "RSTP Improvements", "items": ["Converges in 1-2 seconds","Port roles simplified","New port states: Discarding","Active negotiation (no timers)"]},
     {"title": "RSTP Port Roles", "items": ["Root Port (same as STP)","Designated Port (same)","Alternate Port (blocked backup)","Backup Port (same seg backup)"]},
     {"title": "RSTP Port States", "items": ["Discarding (replaces block+listen)","Learning","Forwarding","Only 3 states vs STP's 5"]},
     {"title": "PVST+ & Rapid-PVST+", "items": ["PVST+ = per-VLAN STP (Cisco)","Rapid-PVST+ = per-VLAN RSTP","Default on Cisco switches","Different root per VLAN possible"]},
   ],
   ["Link comes up","RSTP proposal exchanged","Agreement received","Port moves to forwarding","~1-2s convergence"],
   ["spanning-tree mode rapid-pvst","show spanning-tree","show spanning-tree summary","spanning-tree vlan 10 root primary"],
   ["Rapid-PVST+ is default on modern Cisco switches","RSTP has 3 port states; STP has 5","Alternate port = blocked but ready (like STP blocked)","'spanning-tree vlan X root primary' sets priority to 24576"]),

  (17, "EtherChannel",
   "EtherChannel bundles multiple physical links into one logical link — more bandwidth, redundancy.",
   [
     {"title": "EtherChannel Basics", "items": ["Up to 8 active links (LACP)","Logical port-channel interface","Load balances across links","STP sees as single link"]},
     {"title": "PAgP vs LACP", "items": ["PAgP: Cisco proprietary","LACP: IEEE 802.3ad (open)","LACP: active/passive modes","PAgP: desirable/auto modes"]},
     {"title": "Config Requirements", "items": ["Same speed & duplex","Same VLAN or trunk config","Same native VLAN","Mismatches break EtherChannel"]},
     {"title": "Load Balancing", "items": ["Based on src/dst MAC or IP","Configured per switch","port-channel load-balance","Not equal split — hash-based"]},
   ],
   ["Configure member interfaces","Assign to channel-group","Negotiate with PAgP/LACP","port-channel interface up","STP sees one link"],
   ["interface range GigabitEthernet0/1-2"," channel-group 1 mode active   ! LACP active","interface port-channel 1"," switchport mode trunk","show etherchannel summary"],
   ["All member ports must have identical config (speed, duplex, VLAN, trunk)","LACP active+active or active+passive = forms channel","PAgP desirable+desirable or desirable+auto = forms channel","'show etherchannel summary' — look for SU flags (bundled)"]),

  (18, "Wireless LAN Basics",
   "802.11 Wi-Fi uses CSMA/CA. Access Points extend the wired network wirelessly.",
   [
     {"title": "802.11 Standards", "items": ["802.11a: 5GHz 54Mbps","802.11n (Wi-Fi 4): 2.4/5GHz","802.11ac (Wi-Fi 5): 5GHz","802.11ax (Wi-Fi 6): 2.4/5/6GHz"]},
     {"title": "Frequencies", "items": ["2.4GHz: longer range, more interference","5GHz: shorter range, faster","Non-overlapping: 1,6,11 (2.4G)","More channels on 5GHz"]},
     {"title": "AP Modes", "items": ["Local mode: normal AP","FlexConnect: branch AP","Monitor: scan only","Sniffer: packet capture"]},
     {"title": "Security", "items": ["WPA2: AES-CCMP (strong)","WPA3: SAE (strongest)","WEP: deprecated, broken","802.1X: enterprise auth"]},
   ],
   ["Client sends probe request","AP responds with probe reply","Auth exchange","Association request/response","Connected!"],
   ["! On WLC (web GUI or CLI)","show wlan summary","show ap summary","show ap config general AP1","debug client <mac-address>"],
   ["CSMA/CA (Collision Avoidance) used in wireless, not CSMA/CD","2.4GHz channels 1, 6, 11 are non-overlapping","WPA2-Personal: pre-shared key | WPA2-Enterprise: 802.1X/RADIUS","Autonomous AP vs Lightweight AP (needs WLC)"]),

  (19, "Wireless LAN Controller",
   "WLC centralizes AP management. Lightweight APs (LWAP) tunnel traffic via CAPWAP.",
   [
     {"title": "WLC Architecture", "items": ["WLC = central controller","Lightweight APs (LWAP)","CAPWAP tunnel: control + data","Management via GUI/CLI/SNMP"]},
     {"title": "CAPWAP", "items": ["Control And Provisioning of WAPs","UDP 5246 (control)","UDP 5247 (data)","Replaces LWAPP (older)"]},
     {"title": "AP Discovery", "items": ["DHCP option 43 (WLC IP)","DNS: cisco-capwap-controller","Broadcast (same subnet)","Prior-join list in AP flash"]},
     {"title": "WLC Interfaces", "items": ["Management: device mgmt","AP-Manager: AP control","Virtual: DHCP relay/mobility","Dynamic: VLAN-mapped WLANs"]},
   ],
   ["AP powers on","Discovers WLC via CAPWAP","Downloads config from WLC","Creates SSIDs","Clients connect"],
   ["! WLC verification (CLI)","show ap summary","show ap config general","show wlan summary","show client detail <mac>"],
   ["Lightweight AP needs WLC — cannot operate standalone","CAPWAP uses UDP 5246 (control) and 5247 (data)","Split-MAC: real-time frames handled by AP, management by WLC","FlexConnect allows local switching if WLC link fails"]),

  # ── DOMAIN 3: IP Connectivity ────────────────
  (20, "Routing Fundamentals",
   "Routers forward packets based on longest-prefix match in the routing table.",
   [
     {"title": "Route Sources", "items": ["C = Connected (automatic)","S = Static (manual)","O = OSPF | E = EIGRP","R = RIP | B = BGP"]},
     {"title": "Longest Prefix", "items": ["/32 beats /24 beats /0","More specific = preferred","Default route = 0.0.0.0/0","'Gateway of last resort'"]},
     {"title": "Admin Distance", "items": ["Lower AD = more trusted","Connected: AD 0","Static: AD 1","OSPF: AD 110 | EIGRP: 90"]},
     {"title": "Metric", "items": ["OSPF: cost (bandwidth-based)","EIGRP: composite (BW+delay)","RIP: hop count (max 15)","Lower metric = preferred path"]},
   ],
   ["Packet arrives","Check routing table","Longest prefix match","CEF lookup","Forward out interface"],
   ["show ip route","show ip route 192.168.1.0","show ip route summary","show ip cef","show ip interface brief"],
   ["Connected and static routes have AD 0 and 1 (most trusted)","If same AD + metric: load balance (ECMP)","0.0.0.0/0 = default route (gateway of last resort)","AD is local to the router — not advertised"]),

  (21, "Static Routing",
   "Static routes are manually configured. Used for small networks or specific paths.",
   [
     {"title": "Static Route Types", "items": ["Standard: ip route dst mask nexthop","Default: ip route 0.0.0.0 0.0.0.0","Summary: aggregates subnets","Floating: higher AD for backup"]},
     {"title": "Next-Hop Options", "items": ["Next-hop IP address","Exit interface (use with P2P)","Both: IP + interface","Recursive lookup if IP only"]},
     {"title": "Floating Static", "items": ["Higher AD than dynamic route","Only used if primary fails","ip route ... 200 (AD override)","Backup path/failover"]},
     {"title": "IPv6 Static", "items": ["ipv6 route prefix/len nexthop","ipv6 route ::/0 nexthop (default)","Link-local NH needs interface","ipv6 unicast-routing required"]},
   ],
   ["Identify destination","Determine next-hop","Enter ip route command","Verify in routing table","Test with ping/traceroute"],
   ["ip route 192.168.3.0 255.255.255.0 10.0.0.2","ip route 0.0.0.0 0.0.0.0 203.0.113.1   ! default","ip route 10.10.10.0 255.255.255.0 10.0.0.2 200  ! floating","show ip route static"],
   ["Recursive static route: router looks up next-hop IP (prefer specifying both)","Floating static uses higher AD (e.g., 200) so dynamic route wins","Default route (0.0.0.0/0) matches EVERYTHING if no better match","Directly-attached static (exit interface) only for P2P links"]),

  (22, "OSPF Single-Area",
   "OSPF is a link-state IGP. Forms neighbors, builds LSDB, runs SPF algorithm.",
   [
     {"title": "OSPF Basics", "items": ["Link-state protocol","AD = 110","Hello/Dead timers","Area 0 = backbone"]},
     {"title": "Neighbor States", "items": ["Down → Init → 2-Way","→ ExStart → Exchange","→ Loading → Full","Full = neighbor relationship"]},
     {"title": "DR/BDR Election", "items": ["On multi-access (Ethernet)","Highest priority wins (default 1)","Highest RID wins tie","DR = FULL, others = 2-way"]},
     {"title": "Cost Metric", "items": ["Cost = reference-BW / interface-BW","Default ref-BW: 100 Mbps","auto-cost ref-bandwidth 10000","Lower cost = preferred path"]},
   ],
   ["Enable OSPF","Configure network","Hello exchanged","Elect DR/BDR","Full adjacency","Flood LSAs","Run SPF","Install routes"],
   ["router ospf 1"," router-id 1.1.1.1"," network 192.168.1.0 0.0.0.255 area 0","interface GigabitEthernet0/0"," ip ospf 1 area 0","show ip ospf neighbor"],
   ["OSPF uses wildcard masks in 'network' command (inverse of subnet mask)","Router-ID: highest loopback IP, then highest active interface IP","DR/BDR only elected on broadcast (Ethernet) networks","Change ref-bandwidth if you have links > 100 Mbps"]),

  (23, "OSPF Multi-Area",
   "Multi-area OSPF reduces LSA flooding. Area 0 is backbone; all areas connect to it.",
   [
     {"title": "Area Types", "items": ["Backbone: Area 0","Standard area: full LSAs","Stub: no external LSAs","Totally stub: only default route"]},
     {"title": "Router Roles", "items": ["IR: Internal Router (one area)","ABR: Area Border Router","ASBR: redistributes external","Backbone Router: connects to area 0"]},
     {"title": "LSA Types", "items": ["Type 1: Router LSA (intra-area)","Type 2: Network LSA (DR)","Type 3: Summary LSA (ABR)","Type 5: External LSA (ASBR)"]},
     {"title": "Virtual Links", "items": ["Connect non-contiguous area 0","Configured on ABRs","Avoid when possible","Passes through transit area"]},
   ],
   ["Area 0 backbone","ABR connects areas","Type 3 LSAs cross areas","ASBR imports external","Routes in all areas"],
   ["router ospf 1"," area 1 stub     ! stub area","interface GigabitEthernet0/0"," ip ospf 1 area 0","interface GigabitEthernet0/1"," ip ospf 1 area 1","show ip ospf database"],
   ["All non-backbone areas MUST connect to Area 0 (directly or via virtual link)","ABR generates Type 3 Summary LSAs between areas","Stub areas don't receive Type 5 (external) LSAs — use default route","show ip ospf database shows LSA types in LSDB"]),

  (24, "FHRP — HSRP/VRRP/GLBP",
   "FHRP provides gateway redundancy. Hosts use virtual IP as default gateway.",
   [
     {"title": "HSRP", "items": ["Cisco proprietary","Active/Standby routers","Virtual IP + Virtual MAC","0000.0C07.ACxx (group #)"]},
     {"title": "VRRP", "items": ["IEEE 802.3 (open standard)","Master/Backup routers","Virtual IP (may = real IP)","0000.5E00.01xx (group #)"]},
     {"title": "GLBP", "items": ["Cisco proprietary","Active Virtual Gateway (AVG)","Multiple Active VFs (load balance)","Only FHRP that load-balances"]},
     {"title": "HSRP Config", "items": ["standby <grp> ip <VIP>","standby <grp> priority 110","standby <grp> preempt","standby <grp> version 2"]},
   ],
   ["Configure virtual IP","Routers elect Active/Standby","Hosts use VIP as gateway","Active fails","Standby takes over VIP/MAC"],
   ["interface GigabitEthernet0/0"," standby 1 ip 192.168.1.1"," standby 1 priority 110"," standby 1 preempt"," standby 1 version 2","show standby brief"],
   ["HSRP default priority = 100; higher wins Active role","preempt = Active router reclaims role when it comes back","Without preempt, original Active stays Standby after recovery","GLBP is the only FHRP that provides actual load balancing"]),

  # ── DOMAIN 4: IP Services ────────────────────
  (25, "NAT & PAT",
   "NAT translates private IPs to public. PAT (overload) maps many:1 using port numbers.",
   [
     {"title": "NAT Types", "items": ["Static NAT: 1:1 mapping","Dynamic NAT: pool of publics","PAT/Overload: many:1 (port)","Most common: PAT"]},
     {"title": "NAT Terminology", "items": ["Inside Local: private src IP","Inside Global: translated IP","Outside Local: dst as seen inside","Outside Global: real dst IP"]},
     {"title": "PAT Config", "items": ["ip nat inside source list ACL","interface overload","ip nat inside on int facing LAN","ip nat outside on int facing WAN"]},
     {"title": "NAT Limitations", "items": ["Breaks end-to-end reachability","Complicates troubleshooting","IPsec + NAT needs NAT-T","ALG needed for some protocols"]},
   ],
   ["Host sends packet","Inside interface receives","NAT translates src IP (+ port for PAT)","Forwards to internet","Reply translated back"],
   ["access-list 1 permit 192.168.0.0 0.0.255.255","ip nat inside source list 1 interface GigabitEthernet0/1 overload","interface GigabitEthernet0/0","  ip nat inside","interface GigabitEthernet0/1","  ip nat outside","show ip nat translations"],
   ["PAT uses port numbers to track sessions — allows thousands of users on 1 public IP","'show ip nat translations' shows active NAT table","'clear ip nat translation *' clears the NAT table","NAT overload = PAT = most common deployment"]),

  (26, "DHCP",
   "DHCP dynamically assigns IP, mask, gateway, DNS. Uses DORA process.",
   [
     {"title": "DORA Process", "items": ["Discover: broadcast from client","Offer: server proposes IP","Request: client accepts offer","Acknowledge: server confirms"]},
     {"title": "DHCP Server Config", "items": ["ip dhcp pool NAME","network x.x.x.x /mask","default-router (gateway)","dns-server (DNS IP)"]},
     {"title": "DHCP Relay", "items": ["ip helper-address <server IP>","On router interface facing clients","Converts broadcast to unicast","Forward to DHCP server"]},
     {"title": "DHCP Snooping", "items": ["Switch security feature","Trusted vs untrusted ports","Blocks rogue DHCP servers","Required for DAI"]},
   ],
   ["Client boots","Broadcasts Discover","Server sends Offer","Client sends Request","Server sends ACK","Client configures IP"],
   ["ip dhcp pool LAN_POOL"," network 192.168.1.0 255.255.255.0"," default-router 192.168.1.1"," dns-server 8.8.8.8","ip dhcp excluded-address 192.168.1.1 192.168.1.10","show ip dhcp binding"],
   ["DORA = Discover, Offer, Request, Acknowledge","ip dhcp excluded-address prevents assignment of gateway/static IPs","ip helper-address on the router interface facing the client subnet","DHCP lease is temporary — clients must renew periodically"]),

  (27, "DNS",
   "DNS resolves hostnames to IP addresses. Hierarchical distributed database.",
   [
     {"title": "DNS Hierarchy", "items": ["Root servers (13 sets)","TLD: .com .org .net etc","Authoritative nameserver","Recursive/caching resolver"]},
     {"title": "Record Types", "items": ["A: hostname → IPv4","AAAA: hostname → IPv6","CNAME: alias to another name","MX: mail server | PTR: reverse"]},
     {"title": "DNS Process", "items": ["Client queries recursive resolver","Resolver queries root → TLD → auth","Answer returned and cached","TTL determines cache duration"]},
     {"title": "Cisco DNS Config", "items": ["ip domain-name cisco.com","ip name-server 8.8.8.8","ip domain-lookup (default on)","no ip domain-lookup (disable)"]},
   ],
   ["User types www.cisco.com","Check local cache","Query recursive resolver","Root → .com → cisco.com","A record returned → IP used"],
   ["ip domain-name lab.local","ip name-server 8.8.8.8 8.8.4.4","! Disable DNS lookup (no broadcast)","no ip domain-lookup","show hosts"],
   ["'no ip domain-lookup' prevents router from broadcasting on typos (common lab setting)","DNS uses UDP port 53 (queries) and TCP port 53 (zone transfers)","nslookup / dig are tools to test DNS","PTR records are for reverse DNS lookup (IP → hostname)"]),

  (28, "NTP",
   "NTP synchronizes clocks across devices. Accurate time is critical for logs and security.",
   [
     {"title": "NTP Stratum", "items": ["Stratum 0: atomic clock (ref)","Stratum 1: directly connected","Stratum 2: syncs to stratum 1","Max useful: stratum 15"]},
     {"title": "NTP Modes", "items": ["ntp server <IP>: client mode","ntp master <stratum>: server mode","ntp peer: symmetric","ntp broadcast: efficient (LAN)"]},
     {"title": "NTP Auth", "items": ["ntp authenticate","ntp authentication-key 1 md5 KEY","ntp trusted-key 1","ntp server 1.1.1.1 key 1"]},
     {"title": "Verification", "items": ["show ntp status","show ntp associations","* = synced peer","show clock detail"]},
   ],
   ["Configure NTP server","Clients query server","NTP exchange packets","Clock adjusted","Stratum increments by 1"],
   ["ntp server 216.239.35.0","ntp server 216.239.35.4","! Make this device NTP master","ntp master 3","show ntp status","show ntp associations"],
   ["NTP stratum 0 = reference clock (GPS/atomic); stratum increments each hop","Cisco devices use UTC by default — set timezone: clock timezone EST -5","NTP uses UDP port 123","show ntp status: look for 'synchronized' and stratum"]),

  (29, "SNMP",
   "SNMP monitors and manages network devices. Agent on device, Manager collects data.",
   [
     {"title": "SNMP Versions", "items": ["v1: community strings, no encrypt","v2c: 64-bit counters, no encrypt","v3: auth + encryption (use this!)","v3 modes: noAuthNoPriv/AuthNoPriv/AuthPriv"]},
     {"title": "Components", "items": ["Manager (NMS): polls/receives","Agent: runs on device","MIB: database of OIDs","OID: specific data object"]},
     {"title": "Operations", "items": ["Get: manager requests info","Set: manager changes config","Trap: unsolicited agent alert","Inform: trap + acknowledgment"]},
     {"title": "SNMPv3 Config", "items": ["snmp-server group","snmp-server user","Auth: SHA | Priv: AES","snmp-server host <NMS IP>"]},
   ],
   ["SNMP agent enabled","NMS polls with Get","Agent returns OID data","Agent sends Trap on event","NMS logs and alerts"],
   ["snmp-server community PUBLIC ro","snmp-server community PRIVATE rw","! SNMPv3 (preferred)","snmp-server group MYGROUP v3 priv","snmp-server user MYUSER MYGROUP v3 auth sha AUTH123 priv aes 128 PRIV123","show snmp"],
   ["SNMPv1/v2c = community strings in plaintext — insecure","SNMPv3 AuthPriv = MD5/SHA auth + DES/AES encryption — use this","Traps are UDP 162 (unreliable); Informs require acknowledgment","Read-only community: cannot change config | Read-write: can"]),

  (30, "Syslog",
   "Syslog collects log messages from devices. 8 severity levels (0=Emergency, 7=Debug).",
   [
     {"title": "Severity Levels", "items": ["0 Emergency: system unusable","1 Alert: immediate action","2 Critical: critical conditions","3 Error / 4 Warning / 5 Notice"]},
     {"title": "Severity Levels cont.", "items": ["5 Notice: normal but significant","6 Informational: info messages","7 Debug: detailed debug","'Every Awesome Cisco Engineer Needs Doughnuts In Droves'"]},
     {"title": "Log Destinations", "items": ["Console (default, severity 7)","Buffer (RAM, show logging)","Terminal (vty sessions)","Syslog server (persistent)"]},
     {"title": "Config", "items": ["logging 192.168.1.100","logging trap informational","logging buffered 64000","service timestamps log datetime"]},
   ],
   ["Event occurs on device","Syslog message generated","Sent to configured destination","Syslog server stores message","Admin reviews logs"],
   ["logging 192.168.1.100","logging trap 6              ! informational and above","logging buffered 64000 6","service timestamps log datetime msec","show logging"],
   ["Lower number = more severe (0 is worst, 7 is least important)","Mnemonic: Every Awesome Cisco Engineer Needs Doughnuts In Droves","Console logs all by default — can degrade performance under load","'logging synchronous' prevents log messages from interrupting typing"]),

  (31, "SSH & Telnet",
   "SSH = encrypted remote access (use this). Telnet = plaintext (avoid in production).",
   [
     {"title": "Telnet", "items": ["TCP port 23","Plaintext — insecure","Still used in labs","No encryption whatsoever"]},
     {"title": "SSH", "items": ["TCP port 22","Encrypted (strong)","Requires: hostname + domain","RSA key generation needed"]},
     {"title": "SSH Config Steps", "items": ["1. hostname <name>","2. ip domain-name <domain>","3. crypto key generate rsa","4. username/password + login local"]},
     {"title": "VTY Line Config", "items": ["line vty 0 15","transport input ssh","login local","exec-timeout 10 0"]},
   ],
   ["Set hostname","Set domain name","Generate RSA key","Configure VTY lines","Test SSH connection"],
   ["hostname R1","ip domain-name cisco.com","crypto key generate rsa modulus 2048","username admin secret Cisco123","line vty 0 15"," transport input ssh"," login local","ip ssh version 2","show ip ssh"],
   ["SSH requires hostname AND ip domain-name before key generation","'transport input ssh' — blocks Telnet on VTY lines","'ip ssh version 2' — forces SSHv2 (more secure)","Minimum RSA key size for SSHv2: 768 bits (use 2048)"]),

  (32, "FTP & TFTP",
   "FTP/TFTP used for IOS image transfers and config backup. TFTP = simple, no auth.",
   [
     {"title": "TFTP", "items": ["UDP port 69","No authentication","Simple file transfer","Used for IOS upgrades/configs"]},
     {"title": "FTP", "items": ["TCP ports 20 (data) 21 (control)","Username/password auth","Active and passive modes","More reliable than TFTP"]},
     {"title": "IOS Upgrade via FTP", "items": ["ip ftp username cisco","ip ftp password cisco","copy ftp: flash:","verify /md5 flash:image.bin"]},
     {"title": "Config Backup", "items": ["copy running-config tftp:","copy startup-config tftp:","copy tftp: running-config","archive log config"]},
   ],
   ["Identify source/dest","Configure credentials (FTP)","Initiate transfer","Verify MD5 hash","Reload with new image"],
   ["! Backup config","copy running-config tftp://192.168.1.100/R1-config","! IOS upgrade","copy ftp://192.168.1.100/c1900-universalk9.bin flash:","verify /md5 flash:c1900-universalk9.bin","show flash:"],
   ["TFTP uses UDP — no guarantee of delivery (but simple and fast)","FTP active mode: server connects back to client (may need firewall rule)","FTP passive mode: client initiates both connections (preferred)","Always verify MD5 hash after IOS image transfer"]),

  (33, "QoS — Quality of Service",
   "QoS prioritizes critical traffic. Classify → Mark → Queue → Schedule.",
   [
     {"title": "QoS Need", "items": ["Bandwidth constraint causes drops","Voice/video needs low latency","Data can tolerate delay","Without QoS: all traffic equal"]},
     {"title": "Marking", "items": ["DSCP (6-bit): in IP header","CoS (3-bit): in 802.1Q tag","EF (46): voice/video","AF/CS classes for data"]},
     {"title": "Queuing", "items": ["FIFO: default (no priority)","WFQ: weighted fair queuing","CBWFQ: class-based WFQ","LLQ: low latency (voice)"]},
     {"title": "Shaping vs Policing", "items": ["Policing: drops/marks excess","Shaping: buffers/delays excess","Traffic contract (CIR)","Policing at ingress; shaping egress"]},
   ],
   ["Traffic enters","Classify (NBAR/ACL)","Mark (DSCP)","Queue","Schedule (LLQ priority)","Transmit"],
   ["class-map match-any VOICE"," match dscp ef","policy-map QOS-POLICY"," class VOICE","  priority percent 30"," class class-default","  fair-queue","service-policy output QOS-POLICY","show policy-map interface"],
   ["Voice needs: < 150ms one-way delay, < 30ms jitter, < 1% loss","DSCP EF (46) = Expedited Forwarding = highest priority","LLQ provides strict priority queue for voice/video","Policing drops excess; Shaping buffers it (less aggressive)"]),

  # ── DOMAIN 5: Security ───────────────────────
  (34, "Security Concepts",
   "CIA Triad: Confidentiality, Integrity, Availability. Understand threats and mitigations.",
   [
     {"title": "CIA Triad", "items": ["Confidentiality: only authorized access","Integrity: data not tampered","Availability: services accessible","All three must be maintained"]},
     {"title": "Common Threats", "items": ["DoS/DDoS: flood attack","Man-in-the-Middle: intercept","Phishing: credential theft","Reconnaissance: info gathering"]},
     {"title": "Attack Types", "items": ["Password attacks: brute force","Malware: virus/worm/ransomware","Spoofing: fake identity","Insider threat: trusted user"]},
     {"title": "Defense Layers", "items": ["Perimeter: firewall/IPS","Network: ACLs/segmentation","Host: endpoint protection","Data: encryption"]},
   ],
   ["Identify assets","Assess vulnerabilities","Implement controls","Monitor continuously","Respond to incidents"],
   ["! Basic hardening","no ip http server","no ip http secure-server   ! if not needed","service password-encryption","banner motd ^Authorized Users Only^","no cdp run   ! on edge interfaces"],
   ["CIA Triad is the foundation of all security decisions","Social engineering attacks the human, not the technology","Defense in depth: multiple overlapping security layers","Principle of least privilege: grant only required access"]),

  (35, "Port Security",
   "Port security limits MACs per port and protects against MAC flooding attacks.",
   [
     {"title": "Port Security Basics", "items": ["Limits MAC addresses per port","Configured on access ports only","Violation actions: protect/restrict/shutdown","Default: shutdown (most secure)"]},
     {"title": "MAC Learning", "items": ["Static: manually configured","Dynamic: learned (not saved)","Sticky: learned + saved to config","Sticky = persistent dynamic"]},
     {"title": "Violation Modes", "items": ["Shutdown: port disabled (default)","Restrict: drop + increment counter","Protect: drop, no counter","Shutdown = most secure"]},
     {"title": "Recovery", "items": ["errdisable recovery cause psecure","errdisable recovery interval 300","Manual: shut → no shut","show port-security interface"]},
   ],
   ["Enable port security","Set max MACs","Choose violation mode","Configure sticky (optional)","Monitor for violations"],
   ["interface FastEthernet0/1"," switchport mode access"," switchport port-security"," switchport port-security maximum 2"," switchport port-security mac-address sticky"," switchport port-security violation shutdown","show port-security interface FastEthernet0/1"],
   ["Port security only works on access ports (not trunks)","Default max = 1 MAC, default violation = shutdown","Sticky MAC saves learned MACs to running-config — copy to startup!","Errdisabled port = manually shut/no shut OR enable auto-recovery"]),

  (36, "ACLs — Standard",
   "Standard ACLs filter by source IP only. Applied close to destination.",
   [
     {"title": "ACL Basics", "items": ["Numbered: 1-99 (standard)","Named ACLs (preferred)","Processed top-down","Implicit deny any at end"]},
     {"title": "Standard ACL", "items": ["Matches source IP only","Applied near destination","Numbered: 1-99 and 1300-1999","permit/deny source [wildcard]"]},
     {"title": "Wildcard Masks", "items": ["0 = must match","1 = don't care","0.0.0.255 = match host bits","host = 0.0.0.0 exact match"]},
     {"title": "ACL Application", "items": ["ip access-group NAME in/out","in = filter incoming traffic","out = filter outgoing traffic","One ACL per interface per direction"]},
   ],
   ["Create ACL","Add permit/deny statements","Apply to interface","Verify with show ip access-lists","Test traffic flow"],
   ["ip access-list standard BLOCK_HOST"," deny host 192.168.1.100"," permit any","interface GigabitEthernet0/1"," ip access-group BLOCK_HOST out","show ip access-lists","show ip interface GigabitEthernet0/1"],
   ["Implicit deny at end means everything not permitted is blocked","Standard ACL = source IP only — apply close to DESTINATION","Wildcard mask: 0.0.0.255 matches any host in /24","'host 10.1.1.1' = 'permit 10.1.1.1 0.0.0.0'"]),

  (37, "ACLs — Extended",
   "Extended ACLs filter by src/dst IP, protocol, port. Applied close to source.",
   [
     {"title": "Extended ACL", "items": ["Matches: src IP, dst IP, protocol, port","Numbered: 100-199 and 2000-2699","Apply close to SOURCE","More granular than standard"]},
     {"title": "Protocol Matching", "items": ["ip: matches all IP","tcp: TCP traffic","udp: UDP traffic","icmp: ping/traceroute"]},
     {"title": "Port Matching", "items": ["eq: equal to (=)","gt/lt: greater/less than","range: port range","neq: not equal"]},
     {"title": "Established", "items": ["TCP established keyword","Matches reply traffic (ACK/RST)","Allows return traffic inbound","Used in stateless firewalls"]},
   ],
   ["Define source/dest","Specify protocol","Specify port (eq/gt/lt)","Apply near source","Verify and test"],
   ["ip access-list extended PROTECT"," permit tcp any host 10.1.1.1 eq 80"," permit tcp any host 10.1.1.1 eq 443"," deny ip any any log","interface GigabitEthernet0/0"," ip access-group PROTECT in","show ip access-lists PROTECT"],
   ["Extended ACL = apply close to SOURCE (prevents traffic from traversing network)","'established' only works for TCP (checks ACK/RST bits)","'log' keyword adds logging — use carefully (CPU intensive)","Order matters — ACL is first-match, most specific rules first"]),

  (38, "DHCP Snooping",
   "DHCP Snooping prevents rogue DHCP servers. Trusted (uplink) vs untrusted (client) ports.",
   [
     {"title": "How It Works", "items": ["Switch inspects DHCP messages","Trusted ports: DHCP server/uplinks","Untrusted ports: client-facing","Blocks DHCP Offers from untrusted"]},
     {"title": "DHCP Binding Table", "items": ["IP + MAC + port + VLAN","Built from DHCP Discover/ACK","Used by DAI for validation","show ip dhcp snooping binding"]},
     {"title": "Config", "items": ["ip dhcp snooping (global)","ip dhcp snooping vlan 10","ip dhcp snooping trust (on uplink)","no ip dhcp snooping limit rate"]},
     {"title": "Rate Limiting", "items": ["ip dhcp snooping limit rate 15","Per interface (pps limit)","Protects against DHCP starvation","Applies to untrusted ports"]},
   ],
   ["Enable DHCP snooping","Mark uplink ports trusted","Leave client ports untrusted","Rogue server blocked","Binding table built"],
   ["ip dhcp snooping","ip dhcp snooping vlan 10,20","interface GigabitEthernet0/1   ! uplink to router"," ip dhcp snooping trust","interface range FastEthernet0/1-24   ! client ports"," ip dhcp snooping limit rate 15","show ip dhcp snooping binding"],
   ["All ports untrusted by default — trust ONLY uplinks to real DHCP server","DHCP binding table is required for Dynamic ARP Inspection (DAI)","Rate limiting (pps) on untrusted ports prevents DHCP starvation attacks","'ip dhcp snooping information option' must match relay config"]),

  (39, "Dynamic ARP Inspection",
   "DAI validates ARP packets against DHCP snooping binding table. Prevents ARP spoofing.",
   [
     {"title": "DAI Function", "items": ["Validates ARP requests/replies","Compares ARP to binding table","Drops invalid ARP packets","Prevents ARP poisoning attacks"]},
     {"title": "Trust Ports", "items": ["Trusted: uplinks (not inspected)","Untrusted: client ports (inspected)","ARP from untrusted must match table","Same trust model as DHCP snooping"]},
     {"title": "Config", "items": ["ip arp inspection vlan 10","ip arp inspection trust (uplinks)","ip arp inspection limit rate 100","Requires DHCP snooping first!"]},
     {"title": "Static ARP ACL", "items": ["For static IP hosts (no DHCP)","arp access-list STATIC_HOST","permit ip host x.x.x.x mac host M","ip arp inspection filter"]},
   ],
   ["DAI enabled on VLAN","ARP packet arrives","Check source IP+MAC","Validate against binding table","Valid → forward | Invalid → drop"],
   ["ip dhcp snooping","ip dhcp snooping vlan 10","ip arp inspection vlan 10","interface GigabitEthernet0/1   ! uplink"," ip arp inspection trust","show ip arp inspection vlan 10","show ip arp inspection statistics"],
   ["DAI requires DHCP Snooping binding table (or static ARP ACL for static hosts)","Trust the same ports as DHCP snooping (uplinks to router/server)","DAI prevents man-in-the-middle attacks via ARP poisoning","Rate limit ARP on untrusted ports: ip arp inspection limit rate 100"]),

  (40, "AAA — RADIUS & TACACS+",
   "AAA: Authentication, Authorization, Accounting. RADIUS/TACACS+ are AAA protocols.",
   [
     {"title": "AAA Framework", "items": ["Authentication: who are you?","Authorization: what can you do?","Accounting: what did you do?","Local vs server-based"]},
     {"title": "RADIUS", "items": ["UDP 1812 (auth) 1813 (acct)","Combines Auth+Authz in one","Encrypts password only","Used for network access (Wi-Fi)"]},
     {"title": "TACACS+", "items": ["TCP 49","Separates Auth/Authz/Acct","Encrypts entire payload","Preferred for device admin"]},
     {"title": "Config", "items": ["aaa new-model","aaa authentication login","tacacs-server host / radius-server host","aaa authorization commands"]},
   ],
   ["User tries to log in","Device queries AAA server","Server authenticates user","Authorizes access level","Logs session (accounting)"],
   ["aaa new-model","tacacs-server host 192.168.1.100 key TacKey","aaa authentication login default group tacacs+ local","aaa authorization exec default group tacacs+ local","aaa authorization commands 15 default group tacacs+ local","aaa accounting exec default start-stop group tacacs+"],
   ["TACACS+ = device administration (IOS login) | RADIUS = network access (VPN, Wi-Fi)","TACACS+ encrypts entire packet; RADIUS only encrypts password","aaa new-model is REQUIRED before configuring any AAA","Always have local fallback: '...group tacacs+ local'"]),

  # ── DOMAIN 6: Automation ─────────────────────
  (41, "Network Automation Overview",
   "Automation replaces manual CLI with programmatic config. Faster, less error-prone.",
   [
     {"title": "Why Automate", "items": ["Reduce human error","Faster deployments","Consistent configs","Scale to 1000s of devices"]},
     {"title": "Traditional vs Auto", "items": ["Traditional: CLI per device","Automation: script/template","IaC: Infrastructure as Code","Idempotent: same result each run"]},
     {"title": "Tools Overview", "items": ["Ansible: agentless YAML","Puppet: agent-based Ruby","Chef: agent-based Ruby","Terraform: IaC for cloud"]},
     {"title": "Data Formats", "items": ["JSON: API responses","YAML: config files/Ansible","XML: NETCONF","CSV: simple data exchange"]},
   ],
   ["Identify repetitive task","Choose automation tool","Write playbook/script","Test in lab","Deploy to production","Verify"],
   ["! Verify Python available","python3 --version","pip3 install netmiko","! Simple netmiko test","python3 -c \"from netmiko import ConnectHandler\""],
   ["Ansible is agentless — uses SSH, no software on network devices","Idempotent = running the playbook multiple times = same result","JSON is key for REST APIs; YAML is more human-readable","Automation is 10% of CCNA exam — understand concepts, not deep config"]),

  (42, "SDN & Controllers",
   "SDN separates control plane from data plane. Controller centralizes intelligence.",
   [
     {"title": "Traditional Networking", "items": ["Control plane: on each device","Data plane: on each device","Distributed decision making","CLI management per device"]},
     {"title": "SDN Architecture", "items": ["Control plane: centralized controller","Data plane: stays on device","Northbound API: apps to controller","Southbound API: controller to devices"]},
     {"title": "Planes", "items": ["Management plane: device mgmt","Control plane: routing decisions","Data plane: packet forwarding","SDN centralizes control plane"]},
     {"title": "Cisco SDN Products", "items": ["Cisco DNA Center (campus)","ACI: data center SDN","SD-WAN: Viptela/meraki","NSO: network service orchestrator"]},
   ],
   ["Apps use NB API","Controller processes","SB API pushes to devices","Devices forward traffic","Centralized visibility"],
   ["! Verify DNA Center connectivity","ping dna-center.cisco.com","! REST API test (conceptual)","curl -X GET https://dnac/api/v1/network-device","!  -H 'X-Auth-Token: <token>'"],
   ["SDN Northbound API: apps/orchestration communicate with controller (REST/JSON)","SDN Southbound API: controller programs devices (OpenFlow, NETCONF, RESTCONF)","Cisco DNA Center uses REST API (northbound) and NETCONF/RESTCONF (southbound)","Traditional: distributed control; SDN: centralized control"]),

  (43, "Cisco DNA Center",
   "DNA Center is Cisco's SDN controller for campus/branch. Provides Intent-Based Networking.",
   [
     {"title": "DNA Center Features", "items": ["Design: network hierarchy","Policy: intent-based config","Provision: zero-touch deploy","Assurance: AI/ML analytics"]},
     {"title": "IBN", "items": ["Intent-Based Networking","Business intent → network config","Continuous verification","Self-healing network"]},
     {"title": "DNA Center APIs", "items": ["REST API (northbound)","HTTPS/JSON","Authentication token","Postman/Python access"]},
     {"title": "SD-Access", "items": ["Overlay on DNA Center","VXLAN fabric underlay","LISP for control plane","Micro-segmentation via SGT"]},
   ],
   ["Define network intent","DNA Center translates to config","Pushes config to devices","Monitors with assurance","Remediates automatically"],
   ["! DNA Center REST API","POST /dna/system/api/v1/auth/token","GET /dna/intent/api/v1/network-device","GET /dna/intent/api/v1/topology/site-topology","! All responses in JSON"],
   ["DNA Center communicates with devices via NETCONF/RESTCONF (not just SSH)","Authentication: POST to /auth/token endpoint, get X-Auth-Token header","DNA Center replaces APIC-EM (older Cisco controller)","Assurance uses telemetry data for real-time network analytics"]),

  (44, "REST APIs",
   "REST APIs use HTTP methods (GET/POST/PUT/DELETE) to interact with network controllers.",
   [
     {"title": "REST Basics", "items": ["Representational State Transfer","Stateless: each req independent","HTTP/HTTPS protocol","JSON or XML data format"]},
     {"title": "HTTP Methods", "items": ["GET: retrieve data (read)","POST: create new resource","PUT: replace/update resource","DELETE: remove resource"]},
     {"title": "HTTP Status Codes", "items": ["200 OK: success","201 Created: resource made","400 Bad Request: invalid","401 Unauthorized: auth needed","404 Not Found | 500 Server Error"]},
     {"title": "Authentication", "items": ["Basic auth: base64 user:pass","Token-based: X-Auth-Token","OAuth 2.0: modern standard","API key in header"]},
   ],
   ["Client sends HTTP request","Include auth header","Controller processes","Returns JSON/XML response","Client parses response"],
   ["! Python REST API example","import requests","headers = {'Content-Type': 'application/json', 'X-Auth-Token': token}","response = requests.get('https://dnac/api/v1/network-device', headers=headers)","data = response.json()","print(data['response'])"],
   ["GET = read (safe, idempotent) | POST = create | PUT = update | DELETE = remove","HTTP 200 = OK | 201 = Created | 400 = bad request | 401 = unauth | 404 = not found","JSON key-value pairs: {\"key\": \"value\"} — case-sensitive","REST is stateless: no session maintained between requests"]),

  (45, "Ansible for Network Automation",
   "Ansible is agentless automation using YAML playbooks over SSH. No agents on devices.",
   [
     {"title": "Ansible Basics", "items": ["Agentless (SSH-based)","YAML playbooks","Inventory: list of hosts","Idempotent execution"]},
     {"title": "Key Files", "items": ["inventory: hosts & groups","playbook.yml: tasks to run","ansible.cfg: config settings","roles/: reusable components"]},
     {"title": "Playbook Structure", "items": ["hosts: which devices","gather_facts: yes/no","tasks: list of modules","ios_command / ios_config modules"]},
     {"title": "Cisco Modules", "items": ["ios_command: run show cmds","ios_config: push config lines","ios_facts: gather device info","napalm: multi-vendor"]},
   ],
   ["Write inventory","Write playbook","ansible-playbook run","SSH to devices","Execute tasks","Return results"],
   ["# inventory.ini","[routers]","R1 ansible_host=192.168.1.1","# playbook.yml","- hosts: routers","  tasks:","  - name: Show version","    ios_command:","      commands: show version","    register: output"],
   ["Ansible is agentless — only needs SSH access to devices","Playbooks are YAML — indentation matters!","ios_config module is idempotent — only changes if needed","ansible-playbook -i inventory.ini playbook.yml --check (dry run)"]),

  (46, "Puppet & Chef",
   "Puppet and Chef are agent-based automation tools. Agents pull config from master server.",
   [
     {"title": "Puppet", "items": ["Agent-based (pull model)","Ruby DSL manifests","Puppet master server","Desired state enforcement"]},
     {"title": "Puppet Key Concepts", "items": ["Manifest: config description","Module: reusable manifest","Catalog: compiled config for node","Agent pulls every 30min"]},
     {"title": "Chef", "items": ["Agent-based (pull model)","Ruby cookbooks/recipes","Chef server (or Chef Solo)","Test Kitchen for testing"]},
     {"title": "Comparison vs Ansible", "items": ["Puppet/Chef: agents required","Ansible: agentless (SSH)","Puppet/Chef: pull model","Ansible: push model"]},
   ],
   ["Install agent on device","Agent registers with master","Master compiles catalog","Agent applies catalog","Reports compliance"],
   ["# Puppet manifest example (conceptual)","# class network_config {","#   cisco_interface { 'GigabitEthernet0/0':","#     ensure      => present,","#     description => 'Uplink to Core',","#   }","# }"],
   ["Puppet and Chef require an agent installed on each managed device","Pull model: agents check in periodically vs Ansible's push model","Puppet uses manifests (.pp files); Chef uses cookbooks/recipes","For CCNA exam: understand agentless (Ansible) vs agent-based (Puppet/Chef)"]),

  (47, "JSON & YAML",
   "JSON is API data format. YAML is human-readable config format. Know both for automation.",
   [
     {"title": "JSON", "items": ["JavaScript Object Notation","Key-value pairs: {\"key\": \"val\"}","Arrays: [\"a\", \"b\", \"c\"]","Nested: objects within objects"]},
     {"title": "JSON Data Types", "items": ["String: \"text\"","Number: 42 or 3.14","Boolean: true/false","null: no value | Array: []"]},
     {"title": "YAML", "items": ["YAML Ain't Markup Language","Human-readable","Indentation-based (no braces)","Used in Ansible, K8s, Docker"]},
     {"title": "YAML vs JSON", "items": ["YAML: spaces not tabs","key: value (no quotes needed)","List: - item (dash prefix)","# comments allowed in YAML"]},
   ],
   ["API returns JSON","Parse with json.loads()","Access with dict['key']","YAML read for config","Convert: yaml.safe_load()"],
   ['# JSON example\n{"hostname": "R1", "interfaces": [{"name": "Gi0/0", "ip": "10.0.0.1"}]}\n\n# YAML equivalent\nhostname: R1\ninterfaces:\n  - name: Gi0/0\n    ip: 10.0.0.1'],
   ["JSON uses {}, [], and quotes for strings; YAML uses indentation","YAML is a superset of JSON — valid JSON is valid YAML","REST APIs use JSON; Ansible playbooks use YAML","Python: json.loads(str) and json.dumps(obj) for conversion"]),

  (48, "Cisco DevNet",
   "DevNet is Cisco's developer program. Provides sandboxes, learning labs, and APIs.",
   [
     {"title": "DevNet Resources", "items": ["developer.cisco.com","Always-On sandboxes","Learning Labs (free)","DevNet Certifications"]},
     {"title": "Key Sandboxes", "items": ["DNA Center Always-On","IOS XE on DevNet","NSO sandbox","APIC (ACI) sandbox"]},
     {"title": "DevNet Tools", "items": ["Postman: REST API testing","Python + Requests library","netmiko: SSH to devices","nornir: automation framework"]},
     {"title": "CCNA Relevance", "items": ["Understand automation concepts","Know REST API basics","JSON/YAML data formats","SDN controller concepts"]},
   ],
   ["Create DevNet account","Access always-on sandbox","Use Postman or Python","Call REST API","Parse JSON response","Automate!"],
   ["# Install Python tools","pip3 install netmiko requests","# Quick netmiko test","from netmiko import ConnectHandler","device = {'device_type': 'cisco_ios', 'host': '192.168.1.1', 'username': 'admin', 'password': 'cisco'}","connection = ConnectHandler(**device)","output = connection.send_command('show version')","print(output)"],
   ["DevNet sandboxes are free — always-on or reservable","Postman is the standard tool for exploring REST APIs manually","netmiko uses Paramiko (SSH) under the hood","CCNA exam tests concepts — you won't write Python code during the exam"]),

  # ── Additional Fundamentals ──────────────────
  (49, "TCP vs UDP",
   "TCP = reliable, connection-oriented. UDP = fast, connectionless. Know when to use each.",
   [
     {"title": "TCP", "items": ["Connection-oriented","3-way handshake (SYN/SYN-ACK/ACK)","Sequencing + acknowledgment","Flow control + error recovery"]},
     {"title": "TCP Features", "items": ["Window size: flow control","Retransmission on loss","4-way teardown (FIN/ACK)","Port number identifies app"]},
     {"title": "UDP", "items": ["Connectionless","No handshake","No sequencing/acknowledgment","Low overhead — fast"]},
     {"title": "Port Numbers", "items": ["Well-known: 0-1023","Registered: 1024-49151","Dynamic/ephemeral: 49152-65535","Source = random, Dst = service"]},
   ],
   ["Application chooses TCP or UDP","TCP: SYN → SYN-ACK → ACK","Data transfer with seq/ack","TCP: FIN → FIN-ACK → ACK","Connection closed"],
   ["! Common ports to memorize","! FTP: 20/21 | SSH: 22 | Telnet: 23","! SMTP: 25 | DNS: 53 | DHCP: 67/68","! HTTP: 80 | HTTPS: 443 | SNMP: 161","! NTP: 123 | Syslog: 514 | RDP: 3389"],
   ["TCP SYN flood = DoS attack exploiting 3-way handshake","UDP used by: DNS, DHCP, TFTP, SNMP, RTP (voice/video)","TCP used by: HTTP, HTTPS, FTP, SSH, Telnet, SMTP","Well-known ports: 0-1023 (require root/admin to bind)"]),

  (50, "ICMP",
   "ICMP reports errors and tests reachability. Used by ping and traceroute.",
   [
     {"title": "ICMP Basics", "items": ["Internet Control Message Protocol","IP Protocol number 1","Error reporting (not error correction)","Used by ping and traceroute"]},
     {"title": "ICMP Message Types", "items": ["Type 0: Echo Reply (ping reply)","Type 3: Destination Unreachable","Type 8: Echo Request (ping)","Type 11: Time Exceeded (TTL=0)"]},
     {"title": "Ping Operation", "items": ["Sends Type 8 Echo Request","Receives Type 0 Echo Reply","5 pings by default on Cisco","!!!!! = 5/5 success"]},
     {"title": "Traceroute", "items": ["Sends packets with TTL=1,2,3...","Each router sends Type 11 back","Builds hop-by-hop path","UDP on Unix, ICMP on Cisco"]},
   ],
   ["ping sent (TTL=1 for traceroute)","Each router decrements TTL","TTL=0: router sends ICMP Type 11","Last hop: sends Echo Reply","Path revealed"],
   ["ping 8.8.8.8","ping 192.168.1.1 repeat 100","traceroute 8.8.8.8","ping 192.168.1.1 source Loopback0","! Extended ping for more options","ping"],
   ["! = success, . = timeout, U = unreachable, Q = protocol unreachable","TTL exceeded (Type 11) = how traceroute works","ICMP is best-effort — routers may drop ICMP under load","Firewalls often block ICMP — missing hop in traceroute ≠ broken network"]),

  (51, "WAN Technologies",
   "WAN connects sites over carrier networks. Know leased lines, MPLS, internet-based options.",
   [
     {"title": "WAN Types", "items": ["Leased line: dedicated T1/E1","MPLS: provider-managed VPN","Metro Ethernet: Ethernet WAN","Internet: broadband/fiber"]},
     {"title": "VPN Options", "items": ["IPsec: site-to-site VPN","SSL/TLS: remote access VPN","DMVPN: dynamic multipoint","SD-WAN: overlay on internet"]},
     {"title": "WAN Encapsulation", "items": ["HDLC: Cisco default on serial","PPP: multi-vendor serial","PPPoE: DSL broadband","Frame Relay: legacy (retired)"]},
     {"title": "Cable Types", "items": ["T1: 1.544 Mbps","E1: 2.048 Mbps (Europe)","Serial: DB-60 or Smart Serial","CSU/DSU: converts to serial"]},
   ],
   ["HQ → Serial/fiber","Service provider MPLS cloud","Branch offices connect","OR IPsec VPN over internet","Traffic encrypted+tunneled"],
   ["interface Serial0/0/0"," encapsulation hdlc"," ip address 10.0.0.1 255.255.255.252","! PPP","encapsulation ppp","show interface Serial0/0/0","show ip interface brief"],
   ["HDLC is Cisco default on serial interfaces (not compatible with other vendors)","PPP: open standard, supports auth (PAP/CHAP), compression, multilink","MPLS = provider routes packets using labels, not IP lookups","SD-WAN replaces traditional WAN with internet-based overlay + centralized mgmt"]),

  (52, "Network Address Translation Deep Dive",
   "PAT (overload) uses both IP and port for many:1 mapping. Inside/outside local/global.",
   [
     {"title": "NAT Types Review", "items": ["Static: 1:1 (servers/DMZ)","Dynamic: pool (less common)","PAT/Overload: N:1 (most common)","NAT64: IPv6 to IPv4 translation"]},
     {"title": "NAT Table Entries", "items": ["Inside Local: client private IP","Inside Global: translated public IP","Outside Local: dst as seen by inside","Outside Global: actual dst IP (same for internet)"]},
     {"title": "PAT Port Tracking", "items": ["Same public IP, different ports","Translation table: IP+Port","Supports 65,535 sessions per IP","Scales to thousands of users"]},
     {"title": "NAT Troubleshooting", "items": ["show ip nat translations","show ip nat statistics","debug ip nat","clear ip nat translation *"]},
   ],
   ["Client 192.168.1.10:1024","NAT translates: 203.0.113.1:2001","Sends to internet","Reply to 203.0.113.1:2001","NAT maps back to 192.168.1.10:1024"],
   ["show ip nat translations","show ip nat translations verbose","show ip nat statistics","debug ip nat","clear ip nat translation *   ! clears all dynamic entries"],
   ["PAT creates a unique IP:port combination for each session","Static NAT is used for servers that need a permanent public IP","ip nat inside / ip nat outside must be configured on the right interfaces","NAT statistics show: total active translations, expired, misses"]),

  (53, "OSPF Advanced",
   "OSPF DR/BDR election, LSA types, area types, and OSPF authentication.",
   [
     {"title": "DR/BDR Deep Dive", "items": ["Only on broadcast (Ethernet)","Highest priority wins (then RID)","Priority 0 = never DR/BDR","Non-preemptive by default"]},
     {"title": "OSPF Auth", "items": ["None (default)","Clear text: area X auth","MD5: area X auth message-digest","ip ospf message-digest-key 1 md5 KEY"]},
     {"title": "OSPF Network Types", "items": ["Broadcast: Ethernet (DR/BDR)","Point-to-Point: Serial (no DR)","NBMA: Frame Relay (manual config)","Point-to-Multipoint: hub-spoke"]},
     {"title": "Route Types", "items": ["O = intra-area OSPF","O IA = inter-area (ABR Type 3)","O E1/E2 = external (ASBR)","O N1/N2 = NSSA external"]},
   ],
   ["OSPF enabled","Discover neighbors (Hello)","Elect DR/BDR (broadcast)","Exchange LSDBs","Run Dijkstra SPF","Install O routes"],
   ["router ospf 1"," router-id 1.1.1.1","interface GigabitEthernet0/0"," ip ospf priority 255   ! force DR"," ip ospf message-digest-key 1 md5 OSPFKEY"," ip ospf authentication message-digest","show ip ospf neighbor detail","show ip ospf interface GigabitEthernet0/0"],
   ["DR/BDR election is non-preemptive — clear ip ospf process to re-elect","Changing priority doesn't trigger re-election unless OSPF process is cleared","OSPF uses multicast: 224.0.0.5 (all OSPF routers), 224.0.0.6 (DR/BDR)","Dead timer = 4x Hello timer; mismatch prevents adjacency"]),

  (54, "IPv6 Routing",
   "IPv6 uses OSPFv3, EIGRPv6, and static routes. No ARP — uses NDP/ICMPv6.",
   [
     {"title": "IPv6 Static Routes", "items": ["ipv6 route ::/0 nexthop","ipv6 route prefix/len interface","Link-local NH needs interface","ipv6 unicast-routing required"]},
     {"title": "OSPFv3", "items": ["Supports IPv6 (and IPv4)","ipv6 router ospf 1","ipv6 ospf 1 area 0 on interface","Router-ID still 32-bit"]},
     {"title": "EIGRPv6", "items": ["ipv6 router eigrp 100","eigrp router-id x.x.x.x","ipv6 eigrp 100 on interface","no shutdown under process"]},
     {"title": "IPv6 Address Planning", "items": ["Global: 2000::/3 (routable)","Link-local: FE80::/10 (auto)","Unique-local: FC00::/7 (private)","Loopback: ::1/128"]},
   ],
   ["Enable ipv6 unicast-routing","Assign IPv6 addresses","Configure OSPFv3 or static","Verify with show ipv6 route","Test with ping IPv6"],
   ["ipv6 unicast-routing","interface GigabitEthernet0/0"," ipv6 address 2001:db8:1::1/64","ipv6 route ::/0 2001:db8:1::254","router ospf 1"," router-id 1.1.1.1","interface GigabitEthernet0/0"," ip ospf 1 area 0","show ipv6 route"],
   ["ipv6 unicast-routing must be enabled on router for IPv6 routing","Link-local addresses (FE80::/10) are automatically assigned — needed for NDP","OSPFv3 still needs a 32-bit Router-ID (use 'router-id' command)","ping ipv6 2001:db8::1 — use 'ping ipv6' not just 'ping'"]),

  (55, "Network Troubleshooting",
   "Systematic OSI-layer-by-layer troubleshooting. Start at Layer 1, work up.",
   [
     {"title": "Troubleshooting Method", "items": ["Top-down: L7 → L1","Bottom-up: L1 → L7 (most common)","Divide and conquer","Follow the packet"]},
     {"title": "Layer 1 Checks", "items": ["show interfaces (up/down state)","Cable connected? LED on?","show interfaces counters errors","Speed/duplex mismatch"]},
     {"title": "Layer 2–3 Checks", "items": ["show mac address-table","show arp / show ip arp","show ip route","ping / extended ping"]},
     {"title": "Common Issues", "items": ["Duplex mismatch: late collisions","Wrong VLAN: can't reach gateway","Routing: missing route","ACL: traffic blocked"]},
   ],
   ["Can't ping","Check L1: cable/interface","Check L2: ARP/MAC table","Check L3: routing table","Check ACLs","Check application"],
   ["show interfaces","show ip interface brief","show ip route","show arp","show mac address-table","show access-lists","debug ip packet (use carefully!)","ping 192.168.1.1 source 192.168.2.1"],
   ["Start with 'show ip interface brief' — identifies up/down/admin-down quickly","Duplex mismatch causes late collisions and CRC errors","'debug ip packet' can CPU-lock a router — always use with ACL filter","Extended ping: specify source interface to test specific paths"]),

  (56, "Network Management",
   "Manage devices with SNMP, Syslog, NTP, and out-of-band management (console).",
   [
     {"title": "Management Plane", "items": ["Out-of-band: console/aux port","In-band: SSH over network","Management VRF isolation","Dedicated management network"]},
     {"title": "Baseline & Documentation", "items": ["Network topology diagrams","IP address management (IPAM)","Configuration backups","Change management process"]},
     {"title": "NetFlow", "items": ["Traffic flow statistics","ip flow ingress/egress","show ip flow export","Used for capacity planning/security"]},
     {"title": "RSPAN/SPAN", "items": ["SPAN: copy port traffic","RSPAN: remote SPAN across switches","Used by IDS/packet capture","monitor session 1 source/destination"]},
   ],
   ["Establish baselines","Deploy SNMP/Syslog","Configure NTP","Automate config backups","Monitor + alert","Respond"],
   ["ip flow-export destination 192.168.1.100 2055","ip flow-export version 9","interface GigabitEthernet0/0"," ip flow ingress","monitor session 1 source interface Gi0/1","monitor session 1 destination interface Gi0/24","show monitor session 1"],
   ["Out-of-band management (console) is critical when network is down","NetFlow = who's talking to whom, how much (not packet content)","SPAN copies traffic to an analysis port (IDS, packet analyzer)","Configuration backup + version control is foundational to operations"]),

  (57, "CCNA Exam Strategy",
   "Exam 200-301. 120 min, 90-100 questions. Pass ~825/1000. No partial credit.",
   [
     {"title": "Exam Format", "items": ["200-301: 90-100 questions","120 minutes","Score 825+ / 1000 to pass","Multiple choice, drag-drop, sim"]},
     {"title": "Domain Weights", "items": ["Network Fundamentals: 20%","Network Access: 20%","IP Connectivity: 25%","IP Services: 10%","Security: 15%","Automation: 10%"]},
     {"title": "High-Value Topics", "items": ["Subnetting (always on exam)","OSPF configuration","VLANs + trunking","ACLs (standard + extended)"]},
     {"title": "Study Tips", "items": ["Hands-on lab practice","Jeremy's IT Lab (free YouTube)","Subnetting until instant recall","Review all 57 maps!"]},
   ],
   ["Study all 6 domains","Lab every topic","Practice subnetting daily","Take practice exams","Review weak areas","Book exam","Pass!"],
   ["! Subnet practice","! 192.168.5.0/28 → how many subnets from /24? 16","! Hosts per subnet? 14","! Subnet 3 range? 192.168.5.32 - 192.168.5.47","! Block size? 16","! Broadcast of subnet 3? 192.168.5.47"],
   ["Subnetting is guaranteed — practice until it's automatic (< 60s per subnet)","Simulation questions: read carefully, configure exactly what's asked","Flag uncertain questions and return — don't spend >3 min on one question","You can skip and return to most questions — manage time carefully"]),
]

# ─────────────────────────────────────────────
# Generate all HTML files
# ─────────────────────────────────────────────
for entry in MAPS:
    num = entry[0]
    title = entry[1]
    core_idea = entry[2]
    cols = entry[3]
    flow_steps = entry[4]
    terminal_lines = entry[5]
    checklist_items = entry[6]

    slug = title.lower().replace(" ", "-").replace("/", "-").replace("&", "and").replace("--", "-")
    filename = f"map-{num:02d}-{slug}.html"
    filepath = os.path.join(OUTPUT_DIR, filename)

    html = html_map(num, title, core_idea, cols, flow_steps, terminal_lines, checklist_items)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {filename}")

print(f"\n✅ Generated {len(MAPS)} map files in {OUTPUT_DIR}")
