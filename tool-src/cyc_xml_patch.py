import re,sys,html
path=sys.argv[1]; x=open(path,encoding='utf-8').read()
W=20000
# name: (longName, description, min, max, enums or None)
F={
'imu_conf.accel_confidence_decay':('CYC Street throttle power 1 (W)','Street mode, anchor 1. Watts. Display assist level 3 = this value; levels 1-2 are fractions of it.',0,W,None),
'imu_conf.mahony_kp':('CYC Street throttle torque 1 (%)','Street mode, anchor 1. Percent of motor current max.',0,100,None),
'imu_conf.mahony_ki':('CYC Street PAS power 1 (W)','Street mode, anchor 1. Watts.',0,W,None),
'imu_conf.madgwick_beta':('CYC Street PAS torque 1 (%)','Street mode, anchor 1. Percent of motor current max.',0,100,None),
'imu_conf.rot_roll':('CYC Street throttle power 2 (W)','Street mode, anchor 2 (display level 6). Watts.',0,W,None),
'imu_conf.rot_pitch':('CYC Street throttle torque 2 (%)','Street mode, anchor 2.',0,100,None),
'imu_conf.rot_yaw':('CYC Street PAS power 2 (W)','Street mode, anchor 2. Watts.',0,W,None),
'imu_conf.accel_offsets__0':('CYC Street PAS torque 2 (%)','Street mode, anchor 2.',0,100,None),
'imu_conf.gyro_offset_comp_clamp':('CYC Street PAS torque 2 (old, unused)','Superseded by Street PAS torque 2.',0,100,None),
'app_ppm_conf.tc_max_diff':('CYC Street throttle power 3 (W)','Street mode, anchor 3 (display level 9). Watts.',0,W,None),
'app_ppm_conf.hyst':('CYC Street throttle torque 3 (%)','Street mode, anchor 3.',0,100,None),
'app_ppm_conf.throttle_exp':('CYC Street PAS power 3 (W)','Street mode, anchor 3. Watts.',0,W,None),
'app_ppm_conf.throttle_exp_brake':('CYC Street PAS torque 3 (%)','Street mode, anchor 3.',0,100,None),
'app_chuk_conf.ramp_time_pos':('CYC Race throttle power 1 (W)','Race mode, anchor 1 (display level 3). Watts.',0,W,None),
'app_chuk_conf.ramp_time_neg':('CYC Race throttle torque 1 (%)','Race mode, anchor 1.',0,100,None),
'app_chuk_conf.stick_erpm_per_s_in_cc':('CYC Race PAS power 1 (W)','Race mode, anchor 1. Watts.',0,W,None),
'app_chuk_conf.hyst':('CYC Race PAS torque 1 (%)','Race mode, anchor 1.',0,100,None),
'app_chuk_conf.smart_rev_max_duty':('CYC Race throttle power 2 (W)','Race mode, anchor 2 (display level 6). Watts.',0,W,None),
'app_chuk_conf.smart_rev_ramp_time':('CYC Race throttle torque 2 (%)','Race mode, anchor 2.',0,100,None),
'app_balance_conf.roll_steer_kp':('CYC Race PAS power 2 (W)','Race mode, anchor 2. Watts.',0,W,None),
'app_balance_conf.brake_current':('CYC Race PAS torque 2 (%)','Race mode, anchor 2.',0,100,None),
'app_balance_conf.roll_steer_erpm_kp':('CYC Race throttle power 3 (W)','Race mode, anchor 3 (display level 9). Watts.',0,W,None),
'app_balance_conf.yaw_current_clamp':('CYC Race throttle torque 3 (%)','Race mode, anchor 3.',0,100,None),
'app_ppm_conf.ramp_time_neg':('CYC Race PAS power 3 (W)','Race mode, anchor 3. Watts.',0,W,None),
'app_ppm_conf.max_erpm_for_dir':('CYC Race PAS torque 3 (%)','Race mode, anchor 3.',0,100,None),
'app_ppm_conf.pulse_start':('CYC Street throttle speed limit (km/h)','Always km/h, whatever the display unit.',0,200,None),
'app_ppm_conf.pulse_end':('CYC Race throttle speed limit (km/h)','Always km/h.',0,200,None),
'app_ppm_conf.smart_rev_max_duty':('CYC Street PAS speed limit (km/h)','Always km/h.',0,200,None),
'app_ppm_conf.pulse_center':('CYC Race PAS speed limit (km/h)','Always km/h.',0,200,None),
'imu_conf.mode':('CYC Motor type','Selects the motor preset and which power table applies.',None,None,['X1 Pro Gen 4','X1 Pro Gen 3','Stealth Gen 1','Stealth Gen 3']),
'imu_conf.sample_rate_hz':('CYC Region (0 USA 1 Canada 2 EU 3 Unrestricted 4 EPAC 5 Japan)','Region code.',0,5,None),
'app_nrf_conf.retry_delay':('CYC Wheel size','Wheel diameter. The last entry uses the mm value from CYC Wheel size in mm.',None,None,['16 in','18 in','20 in','22 in','24 in','26 in','27.5 in','28 in / 700c','29 in','Use mm value']),
'app_balance_conf.tiltback_constant_erpm':('CYC Wheel size in mm (when wheel size = Use mm value)','Wheel diameter in mm.',0,3000,None),
'app_nrf_conf.retries':('CYC Battery class (8=24V 10=36V 12=48V 14=52V 16=60V 20=72V)','Nominal pack voltage code. Sets the voltage limits together with min/max voltage.',0,30,None),
'app_balance_conf.torquetilt_filter':('CYC Battery min voltage (V)','Low voltage cutoff start.',0,200,None),
'app_balance_conf.turntilt_strength':('CYC Battery max voltage (V)','Max input voltage.',0,200,None),
'app_nrf_conf.speed':('CYC Display model','Which display is connected.',None,None,['750C','SW102 / DS103','Smart display']),
'app_nrf_conf.address__0':('CYC Display model (written by display) 0=750C 1=SW102/DS103 2=Smart','Set by the display itself.',0,255,None),
'app_ppm_conf.pid_max_erpm':('CYC Torque sensor model (0 = Gen 2, 1 = Gen 3)','Torque sensor generation.',0,10,None),
'app_chuk_conf.tc_max_diff':('CYC Wheel speed magnets per revolution','Magnet count on the wheel speed sensor.',0,100,None),
'app_ppm_conf.ramp_time_pos':('CYC Gen 2 torque sensor baseline voltage (V)','Torque sensor zero point.',0,10,None),
'uavcan_raw_rpm_max':('CYC Torque sensor offset (Nm)','Added to the measured torque.',-100,100,None),
'servo_out_enable':('CYC Invert motor direction','Swap motor rotation direction.',None,None,None),
'app_pas_conf.ctrl_type':('CYC Temperature unit','Display temperature unit.',None,None,['Celsius','Fahrenheit','(unused)']),
'app_pas_conf.invert_pedal_direction':('CYC Speed unit in miles (off = km)','Display speed unit.',None,None,None),
'app_pas_conf.sensor_type':('CYC Ride mode','Street or race. The display mode button also changes this.',None,None,['Street','Race']),
'app_ppm_conf.median_filter':('CYC Display settings lock','Locks the settings menu on the display.',None,None,None),
'app_nrf_conf.power':('CYC Mode after reboot','Which ride mode to start in.',None,None,['Remember last','Street','Race','(unused)','(unused)']),
'app_ppm_conf.ctrl_type':('CYC Cadence start','Start assist from cadence.',None,None,['Off','On','(unused)','(unused)','(unused)','(unused)','(unused)','(unused)']),
'app_ppm_conf.throttle_exp_mode':('CYC Backwards cutout','Cut assist when pedalling backwards.',None,None,['Off','On','(unused)']),
'app_chuk_conf.ctrl_type':('CYC Motor NTC','Motor temperature sensor enable.',None,None,['Off','On','(unused)','(unused)','Battery series bypass']),
'app_ppm_conf.safe_start':('CYC Temperature sensor present','Whether a motor temperature sensor is fitted.',None,None,['No','Yes','(unused)']),
'app_nrf_conf.send_crc_ack':('CYC Brake sensor enable','Enable the brake cutoff input.',None,None,None),
'app_balance_conf.booster_current':('CYC Field weakening current (% of 275 A)','Field weakening.',0,100,None),
'app_balance_conf.startup_pitch_tolerance':('CYC PAS sensitivity','Pedal assist sensitivity.',0,200,None),
'app_balance_conf.startup_roll_tolerance':('CYC PAS power ramp-up time','Pedal assist ramp.',0,200,None),
'app_balance_conf.tiltback_lv_angle':('CYC New motor assist factor','Assist factor for the newer motor.',0,200,None),
'app_adc_conf.ramp_time_pos':('CYC Throttle ramp time (s)','Throttle positive ramp.',0,10,None),
}
Z={'app_balance_conf.yaw_kp':'HR zone 1 BPM','app_balance_conf.yaw_ki':'HR zone 1 BPM range','app_balance_conf.yaw_kd':'HR zone 2 BPM','imu_conf.gyro_offsets__0':'HR zone 2 BPM range','imu_conf.gyro_offsets__1':'HR zone 3 BPM','imu_conf.gyro_offsets__2':'HR zone 3 BPM range','imu_conf.accel_offsets__1':'Human power zone 1 W','imu_conf.accel_offsets__2':'Human power zone 1 W range','app_balance_conf.booster_angle':'Human power zone 2 W','app_balance_conf.booster_ramp':'Human power zone 2 W range','app_balance_conf.torquetilt_angle_limit':'Human power zone 3 W','app_balance_conf.torquetilt_on_speed':'Human power zone 3 W range','app_balance_conf.torquetilt_off_speed':'Both: human power zone 1 W','app_balance_conf.torquetilt_strength':'Both: human power zone 1 W range','app_balance_conf.turntilt_angle_limit':'Both: HR zone 1 BPM','app_balance_conf.turntilt_start_angle':'Both: HR zone 1 BPM range','app_balance_conf.turntilt_start_erpm':'Both: human power zone 2 W','app_balance_conf.turntilt_speed':'Both: human power zone 2 W range','app_balance_conf.turntilt_erpm_boost':'Both: HR zone 2 BPM','app_balance_conf.turntilt_erpm_boost_end':'Both: HR zone 2 BPM range','app_balance_conf.kp':'Both: human power zone 3 W','app_balance_conf.ki':'Both: human power zone 3 W range','app_balance_conf.kd':'Both: HR zone 3 BPM','app_balance_conf.hertz':'Both: HR zone 3 BPM range','app_balance_conf.loop_time_filter':'HR zone 1:0','app_balance_conf.fault_pitch':'HR zone 1:1','app_balance_conf.fault_roll':'HR zone 2:0','app_balance_conf.fault_duty':'HR zone 2:1','app_balance_conf.fault_adc1':'HR zone 3:0','app_balance_conf.fault_adc2':'HR zone 3:1','app_balance_conf.fault_delay_pitch':'PAS torque level zone 1','app_balance_conf.fault_delay_roll':'PAS torque level zone 2','app_balance_conf.fault_delay_duty':'PAS torque level zone 3','app_balance_conf.fault_delay_switch_half':'PAS power level zone 1','app_balance_conf.fault_delay_switch_full':'PAS power level zone 2','app_balance_conf.fault_adc_half_erpm':'PAS power level zone 3'}
for k,v in Z.items(): F[k]=('CYC Trainer '+v,'Stationary trainer zone setting.',0,W,None)
def settag(block,tag,val):
    if re.search(r'<%s>.*?</%s>'%(tag,tag),block,re.S): return re.sub(r'<%s>.*?</%s>'%(tag,tag),'<%s>%s</%s>'%(tag,val,tag),block,count=1,flags=re.S)
    return block.replace('</longName>','</longName>\n            <%s>%s</%s>'%(tag,val,tag),1)
n=0
for name,(ln,desc,mn,mx,en) in F.items():
    m=re.search(r'( *<%s>\n)(.*?)(\n *</%s>)'%(re.escape(name),re.escape(name)),x,re.S)
    if not m: print('MISSING',name); continue
    b=m.group(2)
    t=int(re.search(r'<type>(\d)</type>',b).group(1))
    b=settag(b,'longName',html.escape(ln)); b=settag(b,'description',html.escape(desc))
    if mn is not None:
        if t==1: b=settag(b,'minDouble',mn); b=settag(b,'maxDouble',mx); b=settag(b,'editorScale',1); b=settag(b,'editAsPercentage',0); b=settag(b,'editorDecimalsDouble',1)
        elif t==2: b=settag(b,'minInt',mn); b=settag(b,'maxInt',mx); b=settag(b,'editorScale',1); b=settag(b,'editAsPercentage',0)
    if en is not None:
        assert t==4,name
        b=re.sub(r'\s*<enumNames>.*?</enumNames>','',b,flags=re.S)
        b=b.replace('</longName>','</longName>'+''.join('\n            <enumNames>%s</enumNames>'%html.escape(s) for s in en),1)
    x=x[:m.start(2)]+b+x[m.end(2):]; n+=1
x=x.replace('    <SerOrder>','    <SignatureOverride>3733512279</SignatureOverride>\n    <SerOrder>',1)
open(path,'w',encoding='utf-8').write(x); print('patched',n,'params')
