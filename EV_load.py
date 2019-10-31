def on_precommit(t) : 
	val_on_init = gridlabd.set_value("load_EV","constant_power_A","5000+0j")
	print("EV load is ",val_on_init)
	return True