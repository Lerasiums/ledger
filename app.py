from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# 本地帳本
ledger = []  

# 首頁
@app.route("/")
def home():
    return render_template("index.html")  # 主頁面

# 新增交易
@app.route("/add_transaction", methods=["POST"])
def add_transaction():
    sender = request.form.get("sender")
    receiver = request.form.get("receiver")
    amount = float(request.form.get("amount"))
    
    # 新增交易
    transaction = {
        "sender": sender,
        "receiver": receiver,
        "amount": amount
    }
    ledger.append(transaction)
    
    # 重新回到結果頁面
    return render_template("transaction_success.html", transaction=transaction)

# 查詢餘額
@app.route("/check_balance", methods=["GET"])
def check_balance():
    user = request.args.get("user")
    balance = 0

    # 計算餘額
    for transaction in ledger:
        if transaction["receiver"] == user:
            balance += transaction["amount"]
        if transaction["sender"] == user:
            balance -= transaction["amount"]

    # 顯示餘額結果頁面
    return render_template("balance.html", user=user, balance=balance)

# 查看交易歷史
@app.route("/transaction_history", methods=["GET"])
def transaction_history():
    user = request.args.get("user")
    history = [t for t in ledger if t["sender"] == user or t["receiver"] == user]

    # 顯示交易歷史頁面
    return render_template("history.html", user=user, history=history)

if __name__ == "__main__":
    app.run(debug=True)
