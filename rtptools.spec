Summary: RTP Tools
Name: rtptools
Version: VERSION
Release: 1
Source: http://www.cs.columbia.edu/IRT/software/rtptools/src/rtptools-VERSION.tar.gz
Copyright: Copyright (C) 2001 by Columbia University; all rights reserved
Group: Networking

%description
The rtptools distribution consists of a number of small applications that
can be used for processing RTP data.

rtpplay
     play back RTP sessions recorded by rtpdump
rtpsend
     generate RTP packets from textual description, generated by hand or
     rtpdump
rtpdump
     parse and print RTP packets, generating output files suitable for
     rtpplay and rtpsend
rtptrans
     RTP translator between unicast and multicast networks

multidump
	 Shell script that starts multiple rtpdump's simultaneously.  If you
	 want to play the recording with multiplay, use the '-F dump'
	 option. Writes to base-file.N (N = 1,2,...).
     Usage: 
       multidump <args for rtpdump> base-file addr/port addr/port ...

multiplay
	 Shell script that starts multiple rtpplay's simultaneously.
     Usage: 
       multiplay <args for rtpplay> base-file addr/port addr/port ...

See http://www.cs.columbia.edu/IRT/software/rtptools

Henning Schulzrinne schulzrinne@cs.columbia.edu
Xiaotao Wu
Akira Tsukamoto

%prep
%setup
%build
./configure
make

%install
make install

%files
/usr/local/bin
