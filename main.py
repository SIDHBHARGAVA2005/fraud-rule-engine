from rules import (
    HighAmountRule,
    VelocityRule,
    NightTransactionRule,
    BlackListedMerchantRule
)
from engine import FraudEngine
from data import load_transactions

BLACKLISTED_MERCHANTS={"DarkWebStore", "FakeShop"}

rules=[
    HighAmountRule(threshold=10000),
    VelocityRule(max_txn=3),
    NightTransactionRule(),
    BlackListedMerchantRule(BLACKLISTED_MERCHANTS)
]

engine=FraudEngine(rules, threshold=50)

transactions=load_transactions("transactions.xlsx")
history=[]

for txn in transactions:
    result=engine.evaluate(txn, history)
    history.append(txn)

    print(result)