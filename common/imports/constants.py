#!/usr/bin/env python

BASE = ''
DMTCP = BASE + '/dmtcp'
STRACE = BASE + '/strace'

LOGDIR = BASE + '/log'
DATADIR = BASE + '/data'
CHKPTDIR = DATADIR + '/init_chkpts'

SEQ_DIR = DATADIR + '/seq'
SEQ_STATS_DIR = SEQ_DIR + '/stats'
SEQ_DATA_DIR = SEQ_DIR + '/appdata'
SEQ_APP_INSTANCE_DIR = SEQ_DATA_DIR + '/app_instance_xml'

SEQ_DMTCP_DIR = DATADIR + '/seq_dmtcp'
SEQ_DMTCP_STATS_DIR = SEQ_DMTCP_DIR + '/stats'
SEQ_DMTCP_CHKPTS_DIR = SEQ_DMTCP_DIR + '/chkpts'
SEQ_DMTCP_DATA_DIR = SEQ_DMTCP_DIR + '/appdata'
SEQ_DMTCP_APP_INSTANCE_DIR = SEQ_DMTCP_DATA_DIR + '/app_instance_xml'

PARALLEL_DIR = DATADIR + '/parallel'
PARALLEL_STATS_DIR = PARALLEL_DIR + '/stats'
PARALLEL_DATA_DIR = PARALLEL_DIR + '/appdata'
PARALLEL_APP_INSTANCE_DIR = PARALLEL_DATA_DIR + '/app_instance_xml'
PARALLEL_GROUPS_DIR = PARALLEL_DATA_DIR + '/groups'
PARALLEL_RANDOM_DIR = PARALLEL_DATA_DIR + '/random'

PARALLEL_DMTCP_DIR = DATADIR + '/parallel_dmtcp'
PARALLEL_DMTCP_STATS_DIR = PARALLEL_DMTCP_DIR + '/stats'
PARALLEL_DMTCP_DATA_DIR = PARALLEL_DMTCP_DIR + '/appdata'
PARALLEL_DMTCP_APP_INSTANCE_DIR = PARALLEL_DMTCP_DATA_DIR + '/app_instance_xml'
PARALLEL_DMTCP_CHKPTS_DIR = PARALLEL_DMTCP_DIR + '/chkpts'
PARALLEL_DMTCP_COMPLETED_DIR = PARALLEL_DMTCP_STATS_DIR + '/completed'
PARALLEL_DMTCP_QUEUED_DIR = PARALLEL_DMTCP_STATS_DIR + '/queued'
PARALLEL_DMTCP_RUNNING_DIR = PARALLEL_DMTCP_STATS_DIR + '/running'
PARALLEL_DMTCP_NOIDEA_DIR = PARALLEL_DMTCP_STATS_DIR + '/noidea'

MYPLUG = DMTCP + '/src/plugin/myplug/dmtcp_myplughijack.so'

#DMTCP COMMANDS
DMTCP_COORDINATOR = DMTCP + '/bin/dmtcp_coordinator'
DMTCP_LAUNCH = DMTCP + '/bin/dmtcp_launch'
DMTCP_RESTART = DMTCP + '/bin/dmtcp_restart'
DMTCP_COMMAND = DMTCP + '/bin/dmtcp_command'

#CONSTANTS
SHORTDELAY = 5
LONGDELAY = 30
LOGGER = 'default.log'

