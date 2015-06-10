Summary: The Next-Generation capture agent for Sipcapture's Homer Project
Name: captagent
Version: 4.2.0
Release: 1
License: GPL
URL: http://sipcapture.org
Source: captagent.tar.gz

BuildRequires: tar make m4 automake autoconf libtool libcap libcap-devel expat-devel libpcap-devel openssl-devel

%description
Native HEP capture agents are supported out-of-the-box
in Kamailio/OpenSER, OpenSIPS, FreeSWITCH, Asterisk. Any
other platform supported via Homer's universal Capture
Agent with HEP3 & Filtering for total flexibility.

%prep
%setup -c

%build
./build.sh
./configure --enable-ssl --enable-compression
make

%install
%make_install
%__install -d $RPM_BUILD_ROOT/etc/init.d
%__install -d $RPM_BUILD_ROOT/etc/sysconfig
%__install -d $RPM_BUILD_ROOT/usr/local/etc/captagent
%__install init/centos/captagent.init $RPM_BUILD_ROOT/etc/init.d/captagent
%__install init/centos/captagent.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/captagent
%__install conf/captagent.xml $RPM_BUILD_ROOT/usr/local/etc/captagent/captagent.xml

%files
/etc/init.d/captagent
%config /etc/sysconfig/captagent
%config /usr/local/etc/captagent/captagent.xml
/usr/local/include/capt_cli.h
/usr/local/include/core_hep.h
/usr/local/include/ipreasm.h
/usr/local/include/proto_rtcp.h
/usr/local/include/proto_uni.h
/usr/local/bin/captagent
/usr/local/lib/captagent/

%clean
rm -rf $RPM_BUILD_ROOT
