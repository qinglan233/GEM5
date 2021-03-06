# Create caches with specific parameters
# By Qian

from m5.objects import BaseCache

class L1Cache(BaseCache):
  assoc = 2
  hit_latency = 2
  response_latency = 2
  mshrs = 4
  tgts_per_mshr = 20
  is_top_level = True

  def connectCPU(self, cpu):
    # need to define this in a sub class!
    raise NotImplementedError

  def connectBus(self, bus):
    self.mem_side = bus.slave

class L1ICache(L1Cache):
  size = '16KB'

  def connectCPU(self, cpu):
    self.cpu_side = cpu.icache_port

class L1DCache(L1Cache):
  size = '64KB'

  def connectCPU(self, cpu):
    self.cpu_side = cpu.dcache_port
 
class L2Cache(BaseCache):
  size = '256KB'
  assoc = 8
  hit_latency = 20
  response_latency = 20
  mshrs = 20
  tgts_per_mshr = 12

  def connectCPUSideBus(self, bus):
    self.cpu_side = bus.master

  def connecMemSideBus(self, bus):
    self.mem_side = bus.slave


