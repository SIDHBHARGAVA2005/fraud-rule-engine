from abc import ABC, abstractmethod

class FraudRule(ABC):
    def __init__(self, name, score):
        self.name=name 
        self.score=score

    def evaluate(self, transaction, history):
        pass


class HighAmountRule(FraudRule):
    def __init__(self, threshold=10000):
        super().__init__("High Amount", 30)
        self.threshold = threshold

    def evaluate(self, transaction, history):
        return transaction["amount"] > self.threshold 
    
class VelocityRule(FraudRule):
    def __init__(self, max_txn=3):
        super().__init__("High Velocity", 25)
        self.max_txn=max_txn

    def evaluate(self, transaction, history):
        recent_txns=[
            t for t in history
            if t["user_id"]==transaction["user_id"]
        ]
        return len(recent_txns) > self.max_txn
    
class NightTransactionRule(FraudRule):
    def __init__(self):
        super().__init__("Night Transaction", 15)

    def evaluate(self, transaction, history):
        hour=transaction["timestamp"].hour
        return hour < 5 or hour > 23
    
class BlackListedMerchantRule(FraudRule):
    def __init__(self, blacklist):
        super().__init__("Blacklisted Merchant", 40)
        self.blacklist=blacklist 

    def evaluate(self, transaction, history):
        return transaction["merchant"] in self.blacklist