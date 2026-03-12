import pandas as pd
import joblib


def main():
	model = joblib.load("models/grid_attack_model.pkl")

	new_events = pd.DataFrame([
	    {
		"generator_load": 72.5,
		"transfomer_temp": 81.2, 
		"line_voltage": 230.1, 
		"network_traffic": 210.4,
		"login_failures": 1.0,
		"plc_command_rate": 10.5
	    },
	    {
                "generator_load": 91.3,
                "transfomer_temp": 108.7, 
                "line_voltage": 221.4, 
                "network_traffic": 980.2,
                "login_failures": 12.0,
                "plc_command_rate": 34.6
            },
	    {
                "generator_load": 64.8,
                "transfomer_temp": 74.5, 
                "line_voltage": 229.8, 
                "network_traffic": 185.0,
                "login_failures": 0.0,
                "plc_command_rate": 9.3
            },
	    {
                "generator_load": 88.9,
                "transfomer_temp": 115.2, 
                "line_voltage": 214.6, 
                "network_traffic": 520.8,
                "login_failures": 4.0,
                "plc_command_rate": 29.1
            },
	])
	
	print ("Model expects:", list(model.feature_names_in_))
	print ("New events have:", list(new_events.columns))
	
	new_events = new_events.rename(columns={
	    "transfromer_temp": "transfomer_temp",
	    "transforer_temp": "transfomer_temp"
	})
	
	expected_cols = [
	    "generator_load",
	    "transfomer_temp",
	    "line_voltage", 
	    "network_traffic",
	    "login_failures", 
	    "plc_command_rate"
	]

	new_events = new_events[expected_cols]

	print ("After cleanup:", list(new_events.columns))
	predictions = model.predict (new_events)
	new_events["prediction"] = predictions

	print ("Detection Results:")
	print (new_events)

	print ("\nAlerts:")
	for index, row in new_events.iterrows():
	    if row["prediction"] == "attack":
	        print (
		    f"ALERT: Suspicious activities detected on event {index + 1} | "
		    f"Traffic={row['network_traffic']} | "
		    f"Login Failures={row['login_failures']} | "
		    f"PLC Command Rate={row['plc_command_rate']}"
		)

if  __name__=="__main__":
	main()

