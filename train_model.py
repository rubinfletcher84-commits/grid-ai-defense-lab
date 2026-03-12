import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib


def main():
	df = pd.read_csv("data/grid_attack_data.csv")


	X = df.drop(columns=["event_id", "label"])
	y = df["label"]

	X_train, X_test, y_train, y_test = train_test_split(
	   X, y, test_size=0.2, random_state=42, stratify=y
	)

	model = RandomForestClassifier(n_estimators=100, random_state=42)
	model.fit(X_train, y_train)

	y_pred = model.predict(X_test)

	print ("Confusion Matrix:")
	print (confusion_matrix(y_test, y_pred))
	print ("\nClassification Report:")
	print (classification_report(y_test, y_pred))

	joblib.dump(model, "models/grid_attack_model.pkl")
	print ("\nModel saved to models/grid_attack_model.pkl")


if __name__=="__main__":
    main()
