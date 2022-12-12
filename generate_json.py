import csv
import json


def main():
    urnen = []
    with open("urnen.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            urnen.append({
                "name": row["Bezeichnung"],
                "oefnung": f'{row["Tag"].replace("–", "-")} {row["Uhrzeit"].replace("–", "-")}',
                "position": row["Standort"],
                "cords": [float(x) for x in row["Lat/Lon"].split("/")],
            })

    with open("urnen.json", "w") as f:
        json.dump(urnen, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
