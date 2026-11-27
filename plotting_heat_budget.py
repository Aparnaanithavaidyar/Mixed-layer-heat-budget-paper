'''
Access the files from Zenodo

                            '''


###############################   WEIO ########################################

lat_min = -2
lat_max = 3
lon_min = 50
lon_max = 60
# Conversion factor for the advection variables (degC/day)
convert = 24 * 60 * 60
Region  = 'WEIO'
file_region = f'{Region}'


# Specify the variable names in the datasets
foam_var = 'total_advection'
bias_var = 'ttrd_totad_bias'
model_nhf_calc_var = 'solar_nonsolar_tendency_model'
foam_nhf_var = 'solar_nonsolar_tendency_foam'
model_nhf_vari = 'nhf'
nhf_bias_var = 'solar_nonsolar_tendency_bias'
model_adv_cal_var = 'total_advection'

foam_increment_weio = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_temperature_increment.nc').bckint
foam_nhf_weio = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_nhf_tendency_new.nc')
foam_tempdt_weio = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_regridded_sliced_using_np.nc')
foam_vert_weio = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_vertical_velocity_new.nc')
foam_dtdz_weio = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_dtdz_new.nc')
foam_xadvection_weio = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_xadvection_new.nc')
foam_yadvection_weio = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_yadvection_new.nc')



model_tempdt_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_diag.nc')
model_total_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_heat_budget_masked_ijk_new.nc')
model_advection_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_advection_masked_ijk_new.nc')
model_vmix_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_vertical_mixing_masked_ijk_new_threshold_0.2.nc')
model_hmix_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_horizontal_mixing.nc')
model_nhf_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_net_heat_flux.nc')


cumulus_tempdt_weio = xr.open_dataset('model_concatenated_volume_avg_lat_-2.0_3.0_lon_50.0_60.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_diag_cumulus.nc')
cumulus_total_weio = xr.open_dataset(f'cumulus_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_heat_budget.nc')
cumulus_advection_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_advection_masked_ijk_new_threshold_0.1_cumulus.nc')
cumulus_vmix_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_vertical_mixing_masked_ijk_new_threshold_0.1_cumulus.nc')
cumulus_hmix_weio = xr.open_dataset(f'cumulus_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_horizontal_mixing.nc')
cumulus_nhf_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_net_heat_flux_cumulus.nc')


nudged_tempdt_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_diag_nudged.nc')
nudged_total_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_heat_budget_masked_ijk_new_threshold_0.3_nudged.nc')
nudged_advection_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_advection_masked_ijk_new_threshold_0.3_nudged.nc')
nudged_vmix_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_vertical_mixing_masked_ijk_new_threshold_0.1_nudged.nc')
nudged_hmix_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_horizontal_mixing_masked_ijk_new_threshold_0.3_nudged.nc')
nudged_nhf_weio = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_net_heat_flux_nudged.nc')


foam_wadv_weio = foam_vert_weio['wo'] * foam_dtdz_weio['dT_dz'] *convert *-1
foam_xadvection_var_weio = foam_xadvection_weio['xadvection'] * convert #*-1 #+ foam_increment[foam_inc_var][0:134].data
foam_yadvection_var_weio = foam_yadvection_weio['yadvection'] * convert  #*-1#+ foam_increment[foam_inc_var][0:134].data
foam_nhf_var_weio = foam_nhf_weio['nhf_tendency']
foam_tempdt_var_weio = foam_tempdt_weio['dtemp']*86400
foam_advection_calc_weio = foam_xadvection_var_weio[:] + foam_yadvection_var_weio[:] + foam_wadv_weio[:] #+ foam_temp_incr[0:141].data


control_advection_var_weio = model_advection_weio['ttrd_totad'] * convert
control_hmix_var_weio = model_hmix_weio['ttrd_ldf'] * convert
control_vmix_var_weio = model_vmix_weio['ttrd_zdf'] * convert
control_nhf_op_weio = model_nhf_weio['nhf'] * convert
control_tempdt_var_weio = model_tempdt_weio['diagnosed_temperature_tendency']*86400
control_total_var_weio = model_total_weio['ttrd_tot'] * convert

cumulus_advection_var_weio = cumulus_advection_weio['ttrd_totad'] * convert
cumulus_hmix_var_weio = cumulus_hmix_weio['ttrd_ldf'] * convert
cumulus_vmix_var_weio = cumulus_vmix_weio['ttrd_zdf'] * convert
cumulus_nhf_op_weio = cumulus_nhf_weio['nhf'] * convert
cumulus_tempdt_var_weio = cumulus_tempdt_weio['diagnosed_temperature_tendency']*86400
cumulus_total_var_weio = cumulus_total_weio['ttrd_tot'] * convert

nudged_advection_var_weio = nudged_advection_weio['ttrd_totad'] * convert
nudged_hmix_var_weio = nudged_hmix_weio['ttrd_ldf'] * convert
nudged_vmix_var_weio = nudged_vmix_weio['ttrd_zdf'] * convert
nudged_nhf_op_weio = nudged_nhf_weio['nhf'] * convert
nudged_tempdt_var_weio = nudged_tempdt_weio['diagnosed_temperature_tendency']*86400
nudged_total_var_weio = nudged_total_weio['ttrd_tot'] * convert


data_total_weio = pd.DataFrame({
    'FOAM analysis' : foam_tempdt_var_weio[0:141].values.flatten(),
    'Control' : control_total_var_weio[0:141].values.flatten(),
    'cumulus' : cumulus_total_var_weio[0:141].values.flatten(),
    'Nudge' :  nudged_total_var_weio[0:141].values.flatten()
})

data_advection_weio = pd.DataFrame({
    'FOAM analysis' : foam_advection_calc_weio[0:141].values.flatten(),
    'Control' : control_advection_var_weio[0:141].values.flatten(),
    'cumulus' : cumulus_advection_var_weio[0:141].values.flatten(),
    'Nudge' :  nudged_advection_var_weio[0:141].values.flatten()
})

data_vmix_weio = pd.DataFrame({
    # 'FOAM - UM analysis' : foam_advection_calc_weio[0:141].values.flatten(),
    'Control' : control_vmix_var_weio[0:141].values.flatten(),
    'cumulus' : cumulus_vmix_var_weio[0:141].values.flatten(),
    'Nudge' :  nudged_vmix_var_weio[0:141].values.flatten()
})

data_nhf_weio = pd.DataFrame({
    'FOAM analysis' : foam_nhf_var_weio[0:141].values.flatten(),
    'Control' : control_nhf_op_weio[0:141].values.flatten(),
    'cumulus' : cumulus_nhf_op_weio[0:141].values.flatten(),
    'Nudge' :  nudged_nhf_op_weio[0:141].values.flatten()
})

data_incr_weio = pd.DataFrame({
    'FOAM analysis' : foam_increment_weio[0:141].values.flatten()
})

# ################################   nBoB  ##########################################

lat_min = 15
lat_max = 23
lon_min = 90
lon_max = 100
# Conversion factor for the advection variables
convert = 24 * 60 * 60
Region  = 'nBoB'
file_region = f'{Region}'


foam_increment_bob = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_temperature_increment.nc').bckint
foam_nhf_bob = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_nhf_tendency_new.nc')
foam_tempdt_bob = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_regridded_sliced_using_np.nc')
foam_vert_bob = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_vertical_velocity_new.nc')
foam_dtdz_bob = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_dtdz_new.nc')
foam_xadvection_bob = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_xadvection_new.nc')
foam_yadvection_bob = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_yadvection_new.nc')



foam_wadv_bob = foam_vert_bob['wo'] * foam_dtdz_bob['dT_dz'] *convert *-1
# print(foam_wadv)

foam_xadvection_var_bob = foam_xadvection_bob['xadvection'] * convert #*-1 #+ foam_increment[foam_inc_var][0:134].data
foam_yadvection_var_bob = foam_yadvection_bob['yadvection'] * convert  #*-1#+ foam_increment[foam_inc_var][0:134].data
# foam_zadvection_var_jun = foam_zadvection_jun['wadvection'] #* convert *-1#* -1#+ foam_increment[foam_inc_var][0:134].data
foam_nhf_var_bob = foam_nhf_bob['nhf_tendency'] 
foam_tempdt_var_bob = foam_tempdt_bob['dtemp']*86400
# # foam_advection_var_jun = foam_xadvection_var_jun[0:141] + foam_yadvection_var_jun[0:141] + foam_zadvection_var_jun[0:141] #+ foam_temp_incr[0:141].data
foam_advection_calc_bob = foam_xadvection_var_bob[:] + foam_yadvection_var_bob[:] + foam_wadv_bob[:] #+ foam_temp_incr[0:141].data

model_tempdt_bob = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_diag.nc')
model_total_bob = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_heat_budget.nc')
model_advection_bob = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_advection.nc')
model_vmix_bob = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_vertical_mixing.nc')
model_hmix_bob = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_horizontal_mixing.nc')
model_nhf_bob = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_net_heat_flux.nc')



control_advection_var_bob = model_advection_bob['ttrd_totad'] * convert
control_hmix_var_bob = model_hmix_bob['ttrd_ldf'] * convert
control_vmix_var_bob = model_vmix_bob['ttrd_zdf'] * convert
control_nhf_op_bob = model_nhf_bob['nhf'] * convert
control_tempdt_var_bob = model_tempdt_bob['diagnosed_temperature_tendency']*86400
control_total_var_bob = model_total_bob['ttrd_tot'] * convert


cumulus_tempdt_bob = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_diag_cumulus.nc')
cumulus_total_bob = xr.open_dataset(f'cumulus_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_heat_budget.nc')
cumulus_advection_bob = xr.open_dataset(f'cumulus_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_advection.nc')
cumulus_vmix_bob = xr.open_dataset(f'cumulus_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_vertical_mixing.nc')
cumulus_hmix_bob = xr.open_dataset(f'cumulus_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_horizontal_mixing.nc')
cumulus_nhf_bob = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_net_heat_flux_cumulus.nc')


cumulus_advection_var_bob = cumulus_advection_bob['ttrd_totad'] * convert
cumulus_hmix_var_bob = cumulus_hmix_bob['ttrd_ldf'] * convert
cumulus_vmix_var_bob = cumulus_vmix_bob['ttrd_zdf'] * convert
# # cumulus_nhf_var_jun = cumulus_nhf_jun['nhf_tendency']
cumulus_nhf_op_bob = cumulus_nhf_bob['nhf'] * convert
cumulus_tempdt_var_bob = cumulus_tempdt_bob['diagnosed_temperature_tendency']*86400
cumulus_total_var_bob = cumulus_total_bob['ttrd_tot'] * convert
nudged_tempdt_bob = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_diag_nudged.nc')
nudged_total_bob = xr.open_dataset(f'nudged_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_heat_budget.nc')
nudged_advection_bob = xr.open_dataset(f'nudged_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_advection.nc')
nudged_vmix_bob = xr.open_dataset(f'nudged_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_vertical_mixing.nc')
nudged_hmix_bob = xr.open_dataset(f'nudged_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_horizontal_mixing.nc')
nudged_nhf_bob = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_net_heat_flux_nudged.nc')


nudged_advection_var_bob = nudged_advection_bob['ttrd_totad'] * convert
nudged_hmix_var_bob = nudged_hmix_bob['ttrd_ldf'] * convert
nudged_vmix_var_bob = nudged_vmix_bob['ttrd_zdf'] * convert
# # cumulus_nhf_var_jun = cumulus_nhf_jun['nhf_tendency']
nudged_nhf_op_bob = nudged_nhf_bob['nhf'] * convert
nudged_tempdt_var_bob = nudged_tempdt_bob['diagnosed_temperature_tendency']*86400
nudged_total_var_bob = nudged_total_bob['ttrd_tot'] * convert



# # cumulus_advection_op_var_jun = ma.masked_greater(cumulus_advection_op_var_jun.data, 5e12)

# print(cumulus_advection_calc_var_jun.values)
data_total_bob = pd.DataFrame({
    'FOAM analysis' : foam_tempdt_var_bob[0:141].values.flatten(),
    'Control' : control_total_var_bob[0:141].values.flatten(),
    'cumulus' : cumulus_total_var_bob[0:141].values.flatten(),
    'Nudge' :  nudged_total_var_bob[0:141].values.flatten()
})

data_advection_bob = pd.DataFrame({
    'FOAM analysis' : foam_advection_calc_bob[0:141].values.flatten(),
    'Control' : control_advection_var_bob[0:141].values.flatten(),
    'cumulus' : cumulus_advection_var_bob[0:141].values.flatten(),
    'Nudge' :  nudged_advection_var_bob[0:141].values.flatten()
})

data_vmix_bob = pd.DataFrame({
    # 'FOAM - UM analysis' : nudged_vertical_var_bob[0:141].values.flatten(),
    'Control' : control_vmix_var_bob[0:141].values.flatten(),
    'cumulus' : cumulus_vmix_var_bob[0:141].values.flatten(),
    'Nudge' :  nudged_vmix_var_bob[0:141].values.flatten()
})

data_nhf_bob = pd.DataFrame({
    'FOAM analysis' : foam_nhf_var_bob[0:141].values.flatten(),
    'Control' : control_nhf_op_bob[0:141].values.flatten(),
    'cumulus' : cumulus_nhf_op_bob[0:141].values.flatten(),
    'Nudge' :  nudged_nhf_op_bob[0:141].values.flatten()
})

data_incr_bob = pd.DataFrame({
    'FOAM analysis' : foam_increment_bob[0:141].values.flatten()
})

###################################  nAS  ######################################


lat_min = 18
lat_max = 24
lon_min = 60
lon_max = 67
# Conversion factor for the advection variables
convert = 24 * 60 * 60
Region  = 'nas'
file_region = f'{Region}'


foam_increment_nas = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_temperature_increment.nc').bckint
foam_nhf_nas = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_nhf_tendency_new.nc')
foam_tempdt_nas = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_regridded_sliced_using_np.nc')
foam_vert_nas = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_vertical_velocity_new.nc')
foam_dtdz_nas = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_dtdz_new.nc')
foam_xadvection_nas = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_xadvection_new.nc')
foam_yadvection_nas = xr.open_dataset(f'foam_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_foam_mld_time_mean_Jun_Sep_yadvection_new.nc')



foam_wadv_nas = foam_vert_nas['wo'] * foam_dtdz_nas['dT_dz'] *convert *-1
# print(foam_wadv)

foam_xadvection_var_nas = foam_xadvection_nas['xadvection'] * convert #*-1 #+ foam_increment[foam_inc_var][0:134].data
foam_yadvection_var_nas = foam_yadvection_nas['yadvection'] * convert  #*-1#+ foam_increment[foam_inc_var][0:134].data
# foam_zadvection_var_jun = foam_zadvection_jun['wadvection'] #* convert *-1#* -1#+ foam_increment[foam_inc_var][0:134].data
foam_nhf_var_nas = foam_nhf_nas['nhf_tendency'] 
foam_tempdt_var_nas = foam_tempdt_nas['dtemp']*86400
# # foam_advection_var_jun = foam_xadvection_var_jun[0:141] + foam_yadvection_var_jun[0:141] + foam_zadvection_var_jun[0:141] #+ foam_temp_incr[0:141].data
foam_advection_calc_nas = foam_xadvection_var_nas[:] + foam_yadvection_var_nas[:] + foam_wadv_nas[:] #+ foam_temp_incr[0:141].data

model_tempdt_nas = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_diag.nc')
model_total_nas = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_heat_budget.nc')
model_advection_nas = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_advection.nc')
model_vmix_nas = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_vertical_mixing.nc')
model_hmix_nas = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_horizontal_mixing.nc')
model_nhf_nas = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_net_heat_flux.nc')



control_advection_var_nas = model_advection_nas['ttrd_totad'] * convert
control_hmix_var_nas = model_hmix_nas['ttrd_ldf'] * convert
control_vmix_var_nas = model_vmix_nas['ttrd_zdf'] * convert
control_nhf_op_nas = model_nhf_nas['nhf'] * convert
control_tempdt_var_nas = model_tempdt_nas['diagnosed_temperature_tendency']*86400
control_total_var_nas = model_total_nas['ttrd_tot'] * convert


cumulus_tempdt_nas = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_diag_cumulus.nc')
cumulus_total_nas = xr.open_dataset(f'cumulus_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_heat_budget.nc')
cumulus_advection_nas = xr.open_dataset(f'cumulus_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_advection.nc')
cumulus_vmix_nas = xr.open_dataset(f'cumulus_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_vertical_mixing.nc')
cumulus_hmix_nas = xr.open_dataset(f'cumulus_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_horizontal_mixing.nc')
cumulus_nhf_nas = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_net_heat_flux_cumulus.nc')


cumulus_advection_var_nas = cumulus_advection_nas['ttrd_totad'] * convert
cumulus_hmix_var_nas = cumulus_hmix_nas['ttrd_ldf'] * convert
cumulus_vmix_var_nas = cumulus_vmix_nas['ttrd_zdf'] * convert
# # cumulus_nhf_var_jun = cumulus_nhf_jun['nhf_tendency']
cumulus_nhf_op_nas = cumulus_nhf_nas['nhf'] * convert
cumulus_tempdt_var_nas = cumulus_tempdt_nas['diagnosed_temperature_tendency']*86400
cumulus_total_var_nas = cumulus_total_nas['ttrd_tot'] * convert
nudged_tempdt_nas = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_dtemp_dt_diag_nudged.nc')
nudged_total_nas = xr.open_dataset(f'nudged_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_heat_budget.nc')
nudged_advection_nas = xr.open_dataset(f'nudged_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_total_advection.nc')
nudged_vmix_nas = xr.open_dataset(f'nudged_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_vertical_mixing.nc')
nudged_hmix_nas = xr.open_dataset(f'nudged_model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_horizontal_mixing.nc')
nudged_nhf_nas = xr.open_dataset(f'model_concatenated_volume_avg_lat_{lat_min}.0_{lat_max}.0_lon_{lon_min}.0_{lon_max}.0_over_model_mld_time_mean_Jun_Sep_net_heat_flux_nudged.nc')


nudged_advection_var_nas = nudged_advection_nas['ttrd_totad'] * convert
nudged_hmix_var_nas = nudged_hmix_nas['ttrd_ldf'] * convert
nudged_vmix_var_nas = nudged_vmix_nas['ttrd_zdf'] * convert
# # cumulus_nhf_var_jun = cumulus_nhf_jun['nhf_tendency']
nudged_nhf_op_nas = nudged_nhf_nas['nhf'] * convert
nudged_tempdt_var_nas = nudged_tempdt_nas['diagnosed_temperature_tendency']*86400
nudged_total_var_nas = nudged_total_nas['ttrd_tot'] * convert



# # cumulus_advection_op_var_jun = ma.masked_greater(cumulus_advection_op_var_jun.data, 5e12)

# print(cumulus_advection_calc_var_jun.values)
data_total_nas = pd.DataFrame({
    'FOAM analysis' : foam_tempdt_var_nas[0:141].values.flatten(),
    'Control' : control_total_var_nas[0:141].values.flatten(),
    'cumulus' : cumulus_total_var_nas[0:141].values.flatten(),
    'Nudge' :  nudged_total_var_nas[0:141].values.flatten()
})

data_advection_nas = pd.DataFrame({
    'FOAM analysis' : foam_advection_calc_nas[0:141].values.flatten(),
    'Control' : control_advection_var_nas[0:141].values.flatten(),
    'cumulus' : cumulus_advection_var_nas[0:141].values.flatten(),
    'Nudge' :  nudged_advection_var_nas[0:141].values.flatten()
})

data_vmix_nas = pd.DataFrame({
    # 'FOAM - UM analysis' : nudged_vertical_var_nas[0:141].values.flatten(),
    'Control' : control_vmix_var_nas[0:141].values.flatten(),
    'cumulus' : cumulus_vmix_var_nas[0:141].values.flatten(),
    'Nudge' :  nudged_vmix_var_nas[0:141].values.flatten()
})

data_nhf_nas = pd.DataFrame({
    'FOAM analysis' : foam_nhf_var_nas[0:141].values.flatten(),
    'Control' : control_nhf_op_nas[0:141].values.flatten(),
    'cumulus' : cumulus_nhf_op_nas[0:141].values.flatten(),
    'Nudge' :  nudged_nhf_op_nas[0:141].values.flatten()
})

data_incr_nas = pd.DataFrame({
    'FOAM analysis' : foam_increment_nas[0:141].values.flatten()
})

regions_data = {
    '(a) WEIO': {'Total tendency': data_total_weio, 'Total advection': data_advection_weio, 'NHF tendency' : data_nhf_weio, 'Vertical mixing' : data_vmix_weio, 'Temp increments (DA)': data_incr_weio},
    '(b) Northern Bay of Bengal': {'Total tendency': data_total_bob, 'Total advection': data_advection_bob, 'NHF tendency' : data_nhf_bob, 'Vertical mixing' : data_vmix_bob, 'Temp increments (DA)': data_incr_bob},
    '(c) Northern Arabian Sea' : {'Total tendency': data_total_nas, 'Total advection': data_advection_nas, 'NHF tendency' : data_nhf_nas, 'Vertical mixing' : data_vmix_nas, 'Temp increments (DA)': data_incr_nas},
}

rows = []
for region, terms_dict in regions_data.items():
    for term, df in terms_dict.items():
        m = df.melt(var_name='Experiment', value_name='Value')
        m['Region'] = region
        m['Term'] = term
        rows.append(m)
long_df = pd.concat(rows, ignore_index=True)


fig, axes = plt.subplots(len(regions_data), 1, figsize=(14, 4*len(regions_data)), sharex=True, squeeze=False)
axes = axes.flatten()
experiments = data_nhf_nas.columns.tolist()
palette = dict(zip(experiments, sns.color_palette("Set2", len(experiments))))

for ax, region in zip(axes, regions_data):
    
    n_cats = 4
    minor_ticks = np.arange(-0.5, n_cats, 1)
    ax.set_xticks(minor_ticks, minor=True)
    ax.xaxis.grid(True, which='minor', linestyle='--', linewidth=0.8, alpha=0.8, zorder=1)
    ax.tick_params(axis='x', which='minor', length=0)
    ax.grid(which='major', axis='both', linestyle='--')
    sub = long_df[long_df['Region'] == region]
    sns.barplot(
        data=sub, x='Term', y='Value', hue='Experiment', palette='Set2', ax=ax,
        errorbar=None, capsize=0.1, legend=False, width = 0.9
    )
    ax.axhline(0, color='grey', linewidth=0.9)
    ax.set_title(f'{region}', fontsize = 12, loc='left')
    # ax.set_ylabel('degC/day')
    ax.set_xlabel('')
    ax.set_facecolor('aliceblue')
    ax.set_ylabel(r'$^\circ\mathrm{C}~\mathrm{day}^{-1}$', fontsize = 12)
    ax.tick_params(axis = 'x', which = 'major', labelsize = 12)
    
    for container in ax.containers:
        for bar in container:
            height = bar.get_height()
            # print(height)
            # if pd.isna(height):
            #     continue
            ax.text(
                bar.get_x() + bar.get_width()/2.3,
                height,
                f'{height:.3f}',
                ha='center',
                va='bottom' if height >= 0 else 'top',
                fontweight='bold', size=10, color='blue'
            )

# axes[-1].set_xlabel('Heat budget terms')
handles = [plt.Rectangle((0,0),1,1, color=palette[e]) for e in experiments]
fig.legend(handles, experiments, loc='upper center', ncol=len(experiments),
           bbox_to_anchor=(0.5, 0.94))
fig.patch.set_facecolor('aliceblue')

plt.show()
