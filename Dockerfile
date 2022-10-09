FROM kalilinux/kali-rolling
RUN apt-get update && apt-get -yu dist-upgrade -y
WORKDIR /backbox
RUN apt-get install -y \
  python2.7 \
  wget \
  nodejs \
  dnsrecon \
  wapiti \
  nmap \
  sslyze \
  dnsenum \
  wafw00f \
  golismero \
  dirb \
  host \
  lbd \
  xsser \
  dnsmap \
  dnswalk \
  fierce \
  davtest \
  whatweb \
  nikto \
  uniscan \
  whois \
  python2 \
  python3 \
  npm \
  nautilus \

RUN wget -O rapidscan.py https://raw.githubusercontent.com/FakeSmileUX/VulScanner/master/vulscanner.py && chmod +x vulscanner.py
RUN ln -s /vulscanner/vulscanner.py /usr/local/bin/rapidscan
WORKDIR /reports
ENTRYPOINT ["backbox"]