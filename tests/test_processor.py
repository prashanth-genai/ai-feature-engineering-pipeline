from src.processor import FeatureEngineer

def test_feature_generation():
    engineer = FeatureEngineer()
    engineer.run(["u1,25,100"])

    assert len(engineer.features) == 1
    assert engineer.features[0]["engagement"] == 4.0

def test_invalid_data_skipped():
    engineer = FeatureEngineer()
    engineer.run(["u2,xx,50"])

    assert len(engineer.features) == 0

