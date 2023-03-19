#!/usr/bin/env python
from ucsmsdk.ucshandle import UcsHandle

# pip install ucsmsdk
# Login to UCS and create session
handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")
handle.login()
print(f'UCS Session Cookie: {handle.cookie}')

# Query for compute blades
blade_result = handle.query_classid("computeBlade")
for blade in blade_result[:3]:
    print(blade)

# example output
"""
(venv) $ python UCS_Director_Python_SDK.py 
UCS Session Cookie: 1596308929/f3112fd4-cbe6-44ae-9e85-1d803b91cc3a

Managed Object                  :       ComputeBlade
--------------
class_id                        :ComputeBlade
admin_power                     :policy
admin_state                     :in-service
asset_tag                       :
assigned_to_dn                  :
association                     :none
availability                    :available
available_memory                :49152
chassis_id                      :3
check_point                     :discovered
child_action                    :None
conn_path                       :A,B
conn_status                     :A,B
descr                           :
discovery                       :complete
discovery_status                :
dn                              :sys/chassis-3/blade-1
flt_aggr                        :0
fsm_descr                       :
fsm_flags                       :
fsm_prev                        :DiscoverSuccess
fsm_progr                       :100
fsm_rmt_inv_err_code            :none
fsm_rmt_inv_err_descr           :
fsm_rmt_inv_rslt                :
fsm_stage_descr                 :
fsm_stamp                       :2020-08-01T18:36:28.833
fsm_status                      :nop
fsm_try                         :0
int_id                          :62242
kmip_fault                      :no
kmip_fault_description          :
lc                              :undiscovered
lc_ts                           :1970-01-01T00:00:00.000
local_id                        :
low_voltage_memory              :not-applicable
managing_inst                   :A
memory_speed                    :not-applicable
mfg_time                        :not-applicable
model                           :UCSB-EX-M4-1
name                            :
num_of40_g_adaptors_with_old_fw :0
num_of40_g_adaptors_with_unknown_fw:0
num_of_adaptors                 :2
num_of_cores                    :10
num_of_cores_enabled            :10
num_of_cpus                     :2
num_of_eth_host_ifs             :0
num_of_fc_host_ifs              :0
num_of_threads                  :16
[X]operSolutionStackType        :none
oper_power                      :off
oper_pwr_trans_src              :unknown
oper_qualifier                  :
oper_qualifier_reason           :None
oper_state                      :unassociated
operability                     :operable
original_uuid                   :1b4e28ba-2fa1-11d2-0301-b9a761bde3fb
part_number                     :
policy_level                    :0
policy_owner                    :local
presence                        :equipped
revision                        :0
rn                              :blade-1
sacl                            :None
scaled_mode                     :single
serial                          :SRV126
server_id                       :3/1
slot_id                         :1
status                          :None
storage_oper_qualifier          :None
total_memory                    :49152
usr_lbl                         :
uuid                            :1b4e28ba-2fa1-11d2-0301-b9a761bde3fb
vendor                          :Cisco Systems Inc
vid                             :



Managed Object                  :       ComputeBlade
--------------
class_id                        :ComputeBlade
admin_power                     :policy
admin_state                     :in-service
asset_tag                       :
assigned_to_dn                  :
association                     :none
availability                    :available
available_memory                :49152
chassis_id                      :3
check_point                     :discovered
child_action                    :None
conn_path                       :A,B
conn_status                     :A,B
descr                           :
discovery                       :complete
discovery_status                :
dn                              :sys/chassis-3/blade-3
flt_aggr                        :0
fsm_descr                       :
fsm_flags                       :
fsm_prev                        :DiscoverSuccess
fsm_progr                       :100
fsm_rmt_inv_err_code            :none
fsm_rmt_inv_err_descr           :
fsm_rmt_inv_rslt                :
fsm_stage_descr                 :
fsm_stamp                       :2020-08-01T18:36:28.461
fsm_status                      :nop
fsm_try                         :0
int_id                          :62267
kmip_fault                      :no
kmip_fault_description          :
lc                              :undiscovered
lc_ts                           :1970-01-01T00:00:00.000
local_id                        :
low_voltage_memory              :not-applicable
managing_inst                   :A
memory_speed                    :not-applicable
mfg_time                        :not-applicable
model                           :UCSB-EX-M4-1
name                            :
num_of40_g_adaptors_with_old_fw :0
num_of40_g_adaptors_with_unknown_fw:0
num_of_adaptors                 :2
num_of_cores                    :10
num_of_cores_enabled            :10
num_of_cpus                     :2
num_of_eth_host_ifs             :0
num_of_fc_host_ifs              :0
num_of_threads                  :16
[X]operSolutionStackType        :none
oper_power                      :off
oper_pwr_trans_src              :unknown
oper_qualifier                  :
oper_qualifier_reason           :None
oper_state                      :unassociated
operability                     :operable
original_uuid                   :1b4e28ba-2fa1-11d2-0303-b9a761bde3fb
part_number                     :
policy_level                    :0
policy_owner                    :local
presence                        :equipped
revision                        :0
rn                              :blade-3
sacl                            :None
scaled_mode                     :single
serial                          :SRV127
server_id                       :3/3
slot_id                         :3
status                          :None
storage_oper_qualifier          :None
total_memory                    :49152
usr_lbl                         :
uuid                            :1b4e28ba-2fa1-11d2-0303-b9a761bde3fb
vendor                          :Cisco Systems Inc
vid                             :



Managed Object                  :       ComputeBlade
--------------
class_id                        :ComputeBlade
admin_power                     :policy
admin_state                     :in-service
asset_tag                       :
assigned_to_dn                  :
association                     :none
availability                    :available
available_memory                :49152
chassis_id                      :3
check_point                     :discovered
child_action                    :None
conn_path                       :A,B
conn_status                     :A,B
descr                           :
discovery                       :complete
discovery_status                :
dn                              :sys/chassis-3/blade-5
flt_aggr                        :0
fsm_descr                       :
fsm_flags                       :
fsm_prev                        :DiscoverSuccess
fsm_progr                       :100
fsm_rmt_inv_err_code            :none
fsm_rmt_inv_err_descr           :
fsm_rmt_inv_rslt                :
fsm_stage_descr                 :
fsm_stamp                       :2020-08-01T18:36:28.207
fsm_status                      :nop
fsm_try                         :0
int_id                          :62418
kmip_fault                      :no
kmip_fault_description          :
lc                              :undiscovered
lc_ts                           :1970-01-01T00:00:00.000
local_id                        :
low_voltage_memory              :not-applicable
managing_inst                   :A
memory_speed                    :not-applicable
mfg_time                        :not-applicable
model                           :UCSB-EX-M4-1
name                            :
num_of40_g_adaptors_with_old_fw :0
num_of40_g_adaptors_with_unknown_fw:0
num_of_adaptors                 :2
num_of_cores                    :10
num_of_cores_enabled            :10
num_of_cpus                     :2
num_of_eth_host_ifs             :0
num_of_fc_host_ifs              :0
num_of_threads                  :16
[X]operSolutionStackType        :none
oper_power                      :off
oper_pwr_trans_src              :unknown
oper_qualifier                  :
oper_qualifier_reason           :None
oper_state                      :unassociated
operability                     :operable
original_uuid                   :1b4e28ba-2fa1-11d2-0305-b9a761bde3fb
part_number                     :
policy_level                    :0
policy_owner                    :local
presence                        :equipped
revision                        :0
rn                              :blade-5
sacl                            :None
scaled_mode                     :single
serial                          :SRV128
server_id                       :3/5
slot_id                         :5
status                          :None
storage_oper_qualifier          :None
total_memory                    :49152
usr_lbl                         :
uuid                            :1b4e28ba-2fa1-11d2-0305-b9a761bde3fb
vendor                          :Cisco Systems Inc
vid                             :

"""

