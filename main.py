from src.processor import FeatureEngineer

def main():
    raw_records = [
        "u1,25,100",
        "u2,30,150",
        "u3,40,200",
        "u4,xx,120"   # invalid
    ]

    engineer = FeatureEngineer()
    engineer.run(raw_records)

    print("\nGenerated Features:")
    for feature in engineer.features:
        print(feature)

if __name__ == "__main__":
    main()

