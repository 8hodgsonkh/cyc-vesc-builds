# Move every "CYC ..." param out of its original VESC page into one "CYC Settings" list under the ADC group.
import re,sys
path=sys.argv[1]; x=open(path,encoding='utf-8').read()
def P(*names): return list(names)
sections=[
 ('CYC ride mode and switches', P('app_pas_conf.sensor_type','app_ppm_conf.median_filter','app_nrf_conf.power','app_ppm_conf.ctrl_type','app_ppm_conf.throttle_exp_mode','app_chuk_conf.ctrl_type','app_ppm_conf.safe_start','app_nrf_conf.send_crc_ack','app_balance_conf.booster_current','app_balance_conf.startup_pitch_tolerance','app_balance_conf.startup_roll_tolerance','app_balance_conf.tiltback_lv_angle','app_adc_conf.ramp_time_pos')),
 ('CYC speed limits (km/h)', P('app_ppm_conf.pulse_start','app_ppm_conf.pulse_end','app_ppm_conf.smart_rev_max_duty','app_ppm_conf.pulse_center')),
 ('CYC street power table (anchor 1 / 2 / 3)', P('imu_conf.accel_confidence_decay','imu_conf.mahony_kp','imu_conf.mahony_ki','imu_conf.madgwick_beta','imu_conf.rot_roll','imu_conf.rot_pitch','imu_conf.rot_yaw','imu_conf.accel_offsets__0','app_ppm_conf.tc_max_diff','app_ppm_conf.hyst','app_ppm_conf.throttle_exp','app_ppm_conf.throttle_exp_brake')),
 ('CYC race power table (anchor 1 / 2 / 3)', P('app_chuk_conf.ramp_time_pos','app_chuk_conf.ramp_time_neg','app_chuk_conf.stick_erpm_per_s_in_cc','app_chuk_conf.hyst','app_chuk_conf.smart_rev_max_duty','app_chuk_conf.smart_rev_ramp_time','app_balance_conf.roll_steer_kp','app_balance_conf.brake_current','app_balance_conf.roll_steer_erpm_kp','app_balance_conf.yaw_current_clamp','app_ppm_conf.ramp_time_neg','app_ppm_conf.max_erpm_for_dir')),
 ('CYC bike setup', P('imu_conf.mode','imu_conf.sample_rate_hz','app_nrf_conf.retry_delay','app_balance_conf.tiltback_constant_erpm','app_nrf_conf.retries','app_balance_conf.torquetilt_filter','app_balance_conf.turntilt_strength','app_nrf_conf.speed','app_nrf_conf.address__0','app_ppm_conf.pid_max_erpm','app_chuk_conf.tc_max_diff','app_ppm_conf.ramp_time_pos','uavcan_raw_rpm_max','servo_out_enable','app_pas_conf.ctrl_type','app_pas_conf.invert_pedal_direction')),
]
# trainer zones = every remaining param whose longName starts with "CYC Trainer"
trainer=[]
for m in re.finditer(r'<([a-z_0-9.]+)>\s*<longName>CYC Trainer',x): trainer.append(m.group(1))
sections.append(('CYC trainer zones (stationary mode)', trainer))
allp=[p for _,ps in sections for p in ps]
head,grp=x.split('<Grouping>',1)
for p in allp:
    grp,n=re.subn(r'\n[ \t]*<param>%s</param>'%re.escape(p),'',grp)
    if n==0: print('not found in grouping:',p)
body=''
for title,ps in sections:
    body+='                    <param>::sep::%s</param>\n'%title
    for p in ps: body+='                    <param>%s</param>\n'%p
sub='            <subgroup>\n                <subgroupName>CYC Settings</subgroupName>\n                <subgroupParams>\n'+body+'                </subgroupParams>\n            </subgroup>\n'
# insert at the end of the ADC group
m=re.search(r'<groupName>ADC</groupName>.*?(\n        </group>)',grp,re.S)
assert m
grp=grp[:m.start(1)]+'\n'+sub.rstrip('\n')+grp[m.start(1):]
open(path,'w',encoding='utf-8').write(head+'<Grouping>'+grp)
print('moved',len(allp),'params into ADC > CYC Settings')
