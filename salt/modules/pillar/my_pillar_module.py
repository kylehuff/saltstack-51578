#!/bin/env python

import salt.utils.master
import salt.pillar

import logging

log = logging.getLogger('my_pillar_module')


def ext_pillar(minion_id, pillar, *args, **kwargs):
  # return pillar
  ret_pillar = {'dual-shared-value': 'no match'}

  # disable ext_pillars, we don't want a recursion problem
  master_options = {}
  master_options.update(**__opts__)
  master_options['ext_pillar'] = []

  neighbor = pillar.get('neighbor')

  # setup pillar request
  pillar_util = salt.utils.master.MasterPillarUtil(
    neighbor,
    "glob",
    use_cached_grains=True,
    grains_fallback=False,
    use_cached_pillar=True,
    pillar_fallback=False,
    opts=master_options,
  )
  
  # get the other minion's pillar value for "neighbor"
  neighbor_value = pillar_util.get_minion_pillar().get(neighbor, {}).get('neighbor')

  log.info("ext_pillar 'my_pillar_module' checking relationship between {} and {}".format(minion_id, neighbor))

  # check if relationship is mutual
  if neighbor_value == minion_id:
    ret_pillar['dual-shared-value'] = 'something-shared'

  return ret_pillar
