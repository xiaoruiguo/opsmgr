#--- Monitoring commands for OpsMgr role: osa_lxc_rsyslog

command[osa_lxc_procs] = sudo /etc/nagios/plugins/check-lxc.sh rsyslog check-procs.rb '-p rsyslogd -w 80 -c 320 -W 1 -C 1'

