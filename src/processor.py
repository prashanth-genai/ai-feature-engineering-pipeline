class FeatureEngineer:
    """
    Converts raw user interaction data into AI-ready features.
    """

    def __init__(self):
        self.features = []

    def run(self, records):
        """
        Input format: user_id, age, total_clicks
        """
        for record in records:
            try:
                user_id, age, clicks = record.split(",")

                age = int(age)
                clicks = int(clicks)

                # Feature engineering logic
                engagement_score = round(clicks / age, 2)

                self.features.append({
                    "user_id": user_id,
                    "age": age,
                    "total_clicks": clicks,
                    "engagement": engagement_score
                })

            except Exception as error:
                # Skip invalid records
                continue

