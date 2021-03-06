# This is the tutorial exampole config of GEM5
# By Qian

import m5
from m5.objects import *

system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '4GHz'
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('2GB')]

system.cpu = TimingSimpleCPU()

system.membus = SystemXBar()

system.cpu.icache_port = system.membus.slave
system.cpu.dcache_port = system.membus.slave

system.cpu.createInterruptController()
system.cpu.interrupts.pio = system.membus.master
system.cpu.interrupts.int_master = system.membus.slave
system.cpu.interrupts.int_slave = system.membus.master
system.cpu.numThreads = 4

system.system_port = system.membus.slave

system.mem_ctrl = DDR3_1600_x64()
system.mem_ctrl.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

process = LiveProcess()

process.cmd = ['tests/test-progs/sdbench/bin/x86/linux/sdbench', '-l 3', '-e 1']
system.cpu.workload = process 

system.cpu.createThreads()
system.cpu.createThreads()
system.cpu.createThreads()
system.cpu.createThreads()


root = Root(full_system = False, system = system)
m5.instantiate()

print "Begining simulation! by Qian"
exit_event = m5.simulate()
print 'Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause())


