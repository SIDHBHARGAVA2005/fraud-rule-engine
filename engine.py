import logging

logging.basicConfig(level=logging.INFO)

class FraudEngine:
    def __init__(self, rules, threshold=50):
        self.rules=rules
        self.threshold=threshold

    def evaluate(self, transaction, history):
        risk_score=0
        triggered_rules=[]

        for rule in self.rules:
            if rule.evaluate(transaction, history):
                risk_score+=rule.score
                triggered_rules.append(rule.name)

        decision="FRAUD" if risk_score >=self.threshold else "LEGIT"

        return {
            "transaction_id": transaction["transaction_id"],
            "risk_score": risk_score,
            "decision": decision,
            "rules_triggered": triggered_rules
        }