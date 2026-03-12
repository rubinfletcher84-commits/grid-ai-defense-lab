import pandas as pd
import  random

def generate_normal_data (num_rows=500):
	data = []

	for i in range (num_rows):
		row = {
			"event_id": i + 1, 
			"generator_load": round(random.uniform(55, 85), 2), 
			"transfomer_temp": round(random.uniform(60, 90), 2),
			"line_voltage": round(random.uniform(228, 232), 2), 
			"network_traffic": round(random.uniform(100, 300), 2), 
			"login_failures": round(random.uniform(0, 2), 2),
			"plc_command_rate": round(random.uniform(5, 15), 2), 
			"label": "normal"
		}
	
		data.append(row)

	return pd.DataFrame(data)

def generate_attack_data(num_rows=100, start_id=501):
	data = []

	for i in range(num_rows):
		attack_type = random.choice([
			"dos", 
			"credential_attacks", 
			"plc_manipulation", 
			"voltage_anomaly", 
		])

		if attack_type == "dos":
			row = {
				"event_id": start_id + i, 
				"generator_load": round(random.uniform(60, 90), 2), 
			        "transfomer_temp": round(random.uniform(70, 100), 2),
                       	        "line_voltage": round(random.uniform(227, 233), 2), 
                       	        "network_traffic": round(random.uniform(700, 1500), 2), 
                                "login_failures": round(random.uniform(0, 3), 2),
                                "plc_command_rate": round(random.uniform(5, 18), 2), 
                                "label": "attack"
			 }

		elif attack_type == "credential_attack":
                        row = {
                                "event_id": start_id + i, 
                                "generator_load": round(random.uniform(55, 85), 2), 
                                "transfomer_temp": round(random.uniform(60, 90), 2),
                                "line_voltage": round(random.uniform(228, 232), 2), 
                                "network_traffic": round(random.uniform(200, 500), 2), 
                                "login_failures": round(random.uniform(8, 25), 2),
                                "plc_command_rate": round(random.uniform(5, 15), 2), 
                                "label": "attack"  
                         }

		elif attack_type == "plc_manipulation":
                        row = {
                                "event_id": start_id + i, 
                                "generator_load": round(random.uniform(80, 100), 2), 
                                "transfomer_temp": round(random.uniform(90, 120), 2),
                                "line_voltage": round(random.uniform(220, 238), 2), 
                                "network_traffic": round(random.uniform(250, 600), 2), 
                                "login_failures": round(random.uniform(1, 6), 2),
                                "plc_command_rate": round(random.uniform(25, 50), 2), 
                                "label": "attack"
                         }

		else:
                    row = {
                            "event_id": start_id + i, 
                            "generator_load": round(random.uniform(40, 95), 2), 
                            "transfomer_temp": round(random.uniform(75, 110), 2),
                            "line_voltage": round(random.uniform(210, 245), 2), 
                            "network_traffic": round(random.uniform(150, 400), 2), 
                            "login_failures": round(random.uniform(0, 4), 2),
                            "plc_command_rate": round(random.uniform(8, 20), 2), 
                            "label": "attack"
                         }
	
		data.append(row)

	return pd.DataFrame(data)

def main():
	normal_df = generate_normal_data(500)
	attack_df = generate_attack_data(100, start_id=501)

	full_df = pd.concat([normal_df, attack_df], ignore_index=True)
	full_df = full_df.sample(frac=1, random_state=42).reset_index(drop=True)

	full_df.to_csv("data/grid_attack_data.csv", index=False)

	print ("Dataset created successfully.")
	print ("Saved to: data/grid_attack_data.csv")
	print (f"Total rows: {len(full_df)}")
	print ("\nLabel counts:")
	print (full_df["label"].value_counts())

if __name__ == "__main__":
	main ()

