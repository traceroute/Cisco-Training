rst_ip = "208.8.8.128"

lab = crt.Dialog.Prompt("""
Specify the Lab number.

  1  = 01. IP Services Sim
  2  = 02. IP Services Sim 2
  3  = 03. Static Routing and Configuration Sim
...

""")

lab = lab.strip()
lab = lab.lstrip('0')
lab = int(lab)

if lab == 1:
    connections = [
        "/TELNET " + rst_ip + " 2001",
        "/TELNET " + rst_ip + " 2002",
        "/TELNET " + rst_ip + " 2003"
    ]
elif lab == 2:
    connections = [
        "/TELNET " + rst_ip + " 2004",
        "/TELNET " + rst_ip + " 2005",
        "/TELNET " + rst_ip + " 2006"
    ]
elif lab == 3:
    connections = [
        "/TELNET " + rst_ip + " 2007",
        "/TELNET " + rst_ip + " 2008",
        "/TELNET " + rst_ip + " 2009",
        "/TELNET " + rst_ip + " 2010"
    ]
elif lab == 4:
    connections = [
        "/TELNET " + rst_ip + " 2011",
        "/TELNET " + rst_ip + " 2012",
        "/TELNET " + rst_ip + " 2013",
        "/TELNET " + rst_ip + " 2014"
    ]
elif lab == 5:
    connections = [
        "/TELNET " + rst_ip + " 2014",
        "/TELNET " + rst_ip + " 2015"
    ]
elif lab == 6:
    connections = [
        "/TELNET " + rst_ip + " 2016",
        "/TELNET " + rst_ip + " 2017"
    ]
elif lab == 7:
    connections = [
        "/TELNET " + rst_ip + " 2020",
        "/TELNET " + rst_ip + " 2021",
        "/TELNET " + rst_ip + " 2022",
        "/TELNET " + rst_ip + " 2023",
        "/TELNET " + rst_ip + " 2024",
        "/TELNET " + rst_ip + " 2025",
        "/TELNET " + rst_ip + " 2026"
    ]
elif lab == 8:
    connections = [
        "/TELNET " + rst_ip + " 2027",
        "/TELNET " + rst_ip + " 2028"
    ]
elif lab == 9:
    connections = [
        "/TELNET " + rst_ip + " 2029",
        "/TELNET " + rst_ip + " 2030",
        "/TELNET " + rst_ip + " 2032",
        "/TELNET " + rst_ip + " 2033"
    ]
elif lab == 10:
    connections = [
        "/TELNET " + rst_ip + " 2035",
        "/TELNET " + rst_ip + " 2037",
        "/TELNET " + rst_ip + " 2038",
        "/TELNET " + rst_ip + " 2039",
        "/TELNET " + rst_ip + " 2041"
    ]
elif lab == 11:
    connections = [
        "/TELNET " + rst_ip + " 2044",
        "/TELNET " + rst_ip + " 2045"
    ]
elif lab == 12:
    connections = [
        "/TELNET " + rst_ip + " 2050",
        "/TELNET " + rst_ip + " 2051"
    ]
elif lab == 13:
    connections = [
        "/TELNET " + rst_ip + " 2053",
        "/TELNET " + rst_ip + " 2054"
    ]
elif lab == 14:
    connections = [
        "/TELNET " + rst_ip + " 2059",
        "/TELNET " + rst_ip + " 2060",
        "/TELNET " + rst_ip + " 2061"
    ]
elif lab == 15:
    connections = [
        "/TELNET " + rst_ip + " 2064",
        "/TELNET " + rst_ip + " 2065"
    ]
elif lab == 16:
    connections = [
        "/TELNET " + rst_ip + " 2070",
        "/TELNET " + rst_ip + " 2071"
    ]
elif lab == 17:
    connections = [
        "/TELNET " + rst_ip + " 2075",
        "/TELNET " + rst_ip + " 2076",
        "/TELNET " + rst_ip + " 2077"
    ]
elif lab == 18:
    connections = [
        "/TELNET " + rst_ip + " 2080",
        "/TELNET " + rst_ip + " 2081"
    ]
elif lab == 19:
    connections = [
        "/TELNET " + rst_ip + " 2085",
        "/TELNET " + rst_ip + " 2087",
        "/TELNET " + rst_ip + " 2089",
        "/TELNET " + rst_ip + " 2090",
    ]
elif lab == 20:
    connections = [
        "/TELNET " + rst_ip + " 2093",
        "/TELNET " + rst_ip + " 2094"
    ]
elif lab == 21:
    connections = [
        "/TELNET " + rst_ip + " 2095",
        "/TELNET " + rst_ip + " 2096",
        "/TELNET " + rst_ip + " 2097",
        "/TELNET " + rst_ip + " 2098"
    ]
elif lab == 22:
    connections = [
        "/TELNET " + rst_ip + " 2100",
        "/TELNET " + rst_ip + " 2101",
        "/TELNET " + rst_ip + " 2102"
    ]
elif lab == 23:
    connections = [
        "/TELNET " + rst_ip + " 2106",
        "/TELNET " + rst_ip + " 2107",
        "/TELNET " + rst_ip + " 2110"
    ]
elif lab == 24:
    connections = [
        "/TELNET " + rst_ip + " 2112",
        "/TELNET " + rst_ip + " 2113"
    ]
elif lab == 25:
    connections = [
        "/TELNET " + rst_ip + " 2114",
        "/TELNET " + rst_ip + " 2115",
        "/TELNET " + rst_ip + " 2116"
    ]
elif lab == 26:
    connections = [
        "/TELNET " + rst_ip + " 2117",
        "/TELNET " + rst_ip + " 2118"
    ]
elif lab == 27:
    connections = [
        "/TELNET " + rst_ip + " 2119",
        "/TELNET " + rst_ip + " 2120",
        "/TELNET " + rst_ip + " 2121"
    ]
elif lab == 28:
    connections = [
        "/TELNET " + rst_ip + " 2122",
        "/TELNET " + rst_ip + " 2123"
    ]
elif lab == 29:
    connections = [
        "/TELNET " + rst_ip + " 2128",
        "/TELNET " + rst_ip + " 2129"
    ]
elif lab == 30:
    connections = [
        "/TELNET " + rst_ip + " 2130",
        "/TELNET " + rst_ip + " 2131",
        "/TELNET " + rst_ip + " 2132"
    ]
elif lab == 31:
    connections = [
        "/TELNET " + rst_ip + " 2135",
        "/TELNET " + rst_ip + " 2136"
    ]
elif lab == 32:
    connections = [
        "/TELNET " + rst_ip + " 2139",
        "/TELNET " + rst_ip + " 2140",
        "/TELNET " + rst_ip + " 2141",
        "/TELNET " + rst_ip + " 2142"
    ]
elif lab == 33:
    connections = [
        "/TELNET " + rst_ip + " 2001",
        "/TELNET " + rst_ip + " 2002",
        "/TELNET " + rst_ip + " 2003",
        "/TELNET " + rst_ip + " 2004",
        "/TELNET " + rst_ip + " 2005",
        "/TELNET " + rst_ip + " 2006",
        "/TELNET " + rst_ip + " 2007",
        "/TELNET " + rst_ip + " 2008"
    ]    

crt.Screen.Synchronous = True

for connection in connections:
    crt.Session.ConnectInTab(connection)

crt.Screen.Synchronous = False