import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot

customers=pd.read_json("customers.json")
customers.to_csv("customers.csv")
# print(customers)

accounts=pd.read_json("accounts.json")
accounts.to_csv("accounts.csv")
# print(accounts)

transactions=pd.read_json("transactions.json")
transactions.to_csv("transactions.csv")
# print(transactions)

investments=pd.read_json("investments.json")
investments.to_csv("investments.csv")
# print(investments)

Loans=pd.read_json("Loans.json")
Loans.to_csv("Loans.csv")
# print(Loans)

credit_score=pd.read_json("credit score.json")
credit_score.to_csv("credit score.csv")
# print(credit_score)


print("1.How many accounts does each customer have?")
subplot(2,3,1)
bb=accounts.groupby('CustomerID')['AccountID'].count()
print(bb)

plt.bar(bb.index, bb.values,color='blue',edgecolor='blue')
plt.title("Number of Accounts per Customer")
plt.xlabel("Customer ID")
plt.ylabel("Account Count")
plt.xticks(rotation=90)
plt.tight_layout()

# plt.show()

print("*****************************************************")

print("2.Customer-wise Total Account Balance?")
subplot(2,3,2)
cc = accounts.groupby("CustomerID")["Balance"].sum()
print(cc)
plt.bar(cc.index, cc.values,color='red',edgecolor='red')
plt.title("Customer-wise Total Account Balance")
plt.xlabel("Customer ID")
plt.ylabel("Total Balance")
plt.xticks(rotation=90)
# plt.show()


print("*****************************************************")

print("3.Average balance per account type?")
subplot(2,3,3)
dd=accounts.groupby('Type')['Balance'].mean()
print(dd)

plt.bar(dd.index,dd.values,color='Pink',edgecolor='pink')
plt.title("Average Balance per Account Type")
plt.xlabel("Account Type")
plt.ylabel("Average Balance")
plt.title("Average Balance per Account Type")
# plt.show()

print("*****************************************************")

print("4.Which account type has highest balance?")
subplot(2,3,4)
ee=accounts.groupby('Type')['Balance'].sum()
ff=ee.sort_values(ascending=False).head(1)
print(ff)


plt.bar(ee.index,ee.values,color='blue',edgecolor='blue')
plt.xlabel(" Type")
plt.ylabel(" Balance")
plt.title("Highest Total Balance by Account Type")
plt.tight_layout()
# plt.show()


print("*****************************************************")

print("5.Customers with balance<0?")
gg=accounts[accounts["Balance"] < 0]
print(gg)
neg_balance = accounts[accounts["Balance"] < 0]

print("*****************************************************")


print("6.Identify the account type with the highest number of customers?")
subplot(2,3,5)
hh=accounts.groupby('Type')['CustomerID'].count()
ii=hh.sort_values(ascending=False).head(1)
print(ii)

plt.bar(hh.index,hh.values,color='red',edgecolor='black')
plt.title("identify the account type with the highest number of customers")
plt.xlabel("Type")
plt.ylabel("Customers")
# plt.show()

print("*************************************")

print("7.Credit score<700?")
aa=credit_score[credit_score["Score"]<700]
print(aa)
subplot(2,3,6)
plt.barh(aa["CustomerID"], aa["Score"],color='red',edgecolor='red')
plt.xlabel("Credit Score")
plt.ylabel("CustomerID")
plt.title("Customers with Credit Score < 700")
plt.tight_layout()
plt.show()

print("*************************************")

print("8.which customer has highest credit score?")
bb=credit_score.groupby("CustomerID")["Score"].max()
cc=bb.sort_values(ascending=False).head(1)
print(cc)
subplot(2,3,1)
plt.scatter(cc.index, cc.values,color='red')
plt.title("which customer has highest credit score")
plt.xlabel("customerID")
plt.ylabel("Score")
for i in range(len(cc)):
    plt.text(cc.index[i],cc.values[i],str(cc.values[i]))
# plt.show()

print("*************************************")

print("9.top 3 lowest credit scores?")
dd=credit_score.groupby("CustomerID")["Score"].max()
ee=bb.sort_values(ascending=True).head(3)
print(ee)
subplot(2,3,2)

plt.scatter(ee.index,ee.values,color='black')
plt.xlabel("CustomerID")
plt.ylabel("Score")
plt.title("Top 3 Lowest Credit Scores")
for i in range(len(ee)):
    plt.text(ee.index[i],ee.values[i],str(ee.values[i]))
# plt.show()



print("*************************************")

print("10.Find the average credit score of customers.")
ff=credit_score["Score"].mean()
print(ff)


print("*************************************")

print("11.What is the total balance per customer?")
subplot(2,3,3)
accounts=pd.read_json("accounts.json")
accounts.to_csv("accounts.csv")
# print(accounts)

aa=accounts.groupby("CustomerID")["Balance"].sum()
print(aa)

plt.scatter(aa.index,aa.values,color='yellow')
plt.xlabel("CustomerID")
plt.ylabel("Balance")
plt.title("Total Balance per Customer")
plt.xticks(rotation=90)
for i in range(len(aa)):
    plt.text(aa.index[i],aa.values[i],str(aa.values[i]))
# plt.show()

print("********************************************************")
print("12.Which customer holds the highest balance?")
accounts=pd.read_json("accounts.json")
accounts.to_csv("accounts.csv")
# print(accounts)
subplot(2,3,4)
bb=accounts.groupby("CustomerID")["Balance"].sum().sort_values(ascending=False).head(1)
print(bb)
plt.scatter(bb.index,bb.values,color='pink')
plt.xlabel("CustomerID")
plt.ylabel("Balance")
plt.title("Which customer holds the highest balance")
for i in range(len(bb)):
    plt.text(bb.index[i],bb.values[i],str(bb.values[i]))
# plt.show()

print("********************************************************")

print("13.Average balance by city?")
customers=pd.read_json("customers.json")
customers.to_csv("customers.csv")
# print(customers)

accounts=pd.read_json("accounts.json")
accounts.to_csv("accounts.csv")
# print(accounts)

vv=pd.merge(customers,accounts,on="CustomerID")
cc=vv.groupby("City")["Balance"].mean()
print(cc)
subplot(2,3,5)
plt.barh(cc.index, cc.values,color='red')
plt.title("Average Balance by City")
plt.xlabel("Balance")
plt.ylabel("City")
# plt.show()
print("********************************************************")


print("14.Analyze the account balance of Chennai customers?")
customers=pd.read_json("customers.json")
customers.to_csv("customers.csv")
# print(customers)

accounts=pd.read_json("accounts.json")
accounts.to_csv("accounts.csv")
# print(accounts)

ss=pd.merge(customers,accounts,on="CustomerID")
dd=ss[ss["City"]=="Chennai"][["Name","City","Balance"]]
print(dd)
subplot(2,3,6)
plt.bar(dd["Name"],dd["Balance"],color='brown')
plt.xlabel("Name")
plt.ylabel("Balance")
plt.title("Balance of Chennai customers")
plt.show()


print("********************************************************")

print("15.Total transaction amount per customer?")
accounts=pd.read_json("accounts.json")
accounts.to_csv("accounts.csv")
# print(accounts)

transactions=pd.read_json("transactions.json")
transactions.to_csv("transactions.csv")
# print(transactions)

ww=pd.merge(accounts,transactions,on="AccountID")
# print(ww)

gg=ww.groupby("CustomerID")["Amount"].sum()
print(gg)

subplot(2,3,1)
plt.bar(gg.index,gg.values,color='silver')
plt.xlabel("CustomerID")
plt.ylabel("Amount")
plt.xticks(rotation=90)
plt.title("Total transaction amount per customer")
# plt.show()


print("********************************************************")

print("16.Customers with highest number of transactions?")
accounts=pd.read_json("accounts.json")
accounts.to_csv("accounts.csv")
# print(accounts)

transactions=pd.read_json("transactions.json")
transactions.to_csv("transactions.csv")
# print(transactions)
subplot(2,3,2)
tt=pd.merge(accounts,transactions,on="AccountID")

ttt=tt.groupby("CustomerID")["TxnID"].count().sort_values(ascending=False).head(1)
print(ttt)
plt.scatter(ttt.index,ttt.values,color='red')
plt.xlabel("CustomerID")
plt.ylabel("TxnID")
plt.title("Total transaction amount per customer")
for i in range(len(ttt)):
    plt.text(ttt.index[i],ttt.values[i],str(ttt.values[i]))
# plt.show()

print("*********************************************************************************")

print("17.Average transaction value per customer?")
accounts=pd.read_json("accounts.json")
accounts.to_csv("accounts.csv")
# print(accounts)
transactions=pd.read_json("transactions.json")
transactions.to_csv("transactions.csv")
# print(transactions)
kk=pd.merge(accounts,transactions,on="AccountID")

k=kk.groupby("CustomerID")["Amount"].mean()
print(k)
subplot(2,3,3)
plt.bar(k.index,k.values,color='indigo')
plt.xlabel("CustomerID")
plt.ylabel("Amount")
plt.xticks(rotation=90)
plt.title("Average transaction value per customer")
# plt.show()

print("*********************************************************************************")

print("18.which customers invested in Stocks?")
investments=pd.read_json("investments.json")
investments.to_csv("investments.csv")
# print(investments)
aa=investments[investments["Type"]=='Stocks']
print(aa)
subplot(2,3,4)
plt.bar(aa["CustomerID"],aa["Amount"],color='gold')
plt.xlabel("CustomerID")
plt.ylabel("Amount")
plt.title("which customers invested in Stocks?")
# plt.show()
print("**************************************")

print("19.Investment type distribution?")
investments=pd.read_json("investments.json")
investments.to_csv("investments.csv")
# print(investments)
cc=investments.groupby('Type')['CustomerID'].count()
print(cc)
subplot(2,3,5)
plt.plot(cc.index, cc.values,color='red')
plt.xlabel("Type")
plt.ylabel("Customers")
plt.title("Investment type distribution")
for i in range(len(cc)):
    plt.text(cc.index[i],cc.values[i],str(cc.values[i]))
# plt.show()
print("**************************************")

print("20.Average investment per customer?")
investments=pd.read_json("investments.json")
investments.to_csv("investments.csv")
# print(investments)
dd=investments.groupby("CustomerID")['Amount'].mean()
print(dd)
subplot(2,3,6)
plt.barh(dd.index, dd.values,color='violet')
plt.xlabel("CustomerID")
plt.ylabel("CustomerID")
plt.title("Average investment per customer?")
plt.show()

print("**************************************")

print("Customers with highest investments?")
investments=pd.read_json("investments.json")
investments.to_csv("investments.csv")
# print(investments)
ee=investments.groupby('CustomerID')['Amount'].sum()
ff=ee.sort_values(ascending=False)
print(ff)
subplot(2,3,1)
plt.bar(ff.index,ff.values,color='magenta')
plt.xlabel("CustomerID")
plt.ylabel("Amount")
plt.xticks(rotation=90)
plt.title("Customers with highest investments?")
# plt.show()

print("**************************************")

print("21.Which investment type has the highest number of customers?")
investments=pd.read_json("investments.json")
investments.to_csv("investments.csv")
# print(investments)
gg=investments.groupby('Type')['CustomerID'].count()
hh=gg.sort_values(ascending=False).head(1)
print(hh)
subplot(2,3,2)
plt.scatter(hh.index,hh.values,color='cyan')
plt.xlabel("CustomerID")
plt.ylabel("Customers")
plt.title("Which investment type has the highest number of customers?")
for i in range(len(hh)):
    plt.text(hh.index[i],hh.values[i],str(hh.values[i]))
# plt.show()
print("**************************************")

print("22.Are there any customers with age < 20?")
customers=pd.read_json("customers.json")
customers.to_csv("customers.csv")
# print(customers)

vv=customers[customers["Age"]>40]
print(vv)

subplot(2,3,3)
plt.bar(vv["CustomerID"],vv["Age"],color='maroon')
plt.xlabel("CustomerID")
plt.ylabel("age")
plt.title("customers with age>40")
# plt.show()

print("*****************************************************")

print("23.How many total customers are there?")
customers=pd.read_json("customers.json")
customers.to_csv("customers.csv")
# print(customers)

v=customers["CustomerID"].count()
print(v)

print("*****************************************************")

print("24.Average customer age?")
vs=customers["Age"].mean()
print(vs)

print("*****************************************************")

print("25.City-wise customer count?")
customers=pd.read_json("customers.json")
customers.to_csv("customers.csv")
# print(customers)

vk=customers.groupby("City")["CustomerID"].count()
print(vk)
subplot(2,3,4)
plt.barh(vk.index,vk.values,color='blue')
plt.xlabel("City")
plt.ylabel("Customers")
plt.title("City-wise customer count")
# plt.show()

print("*****************************************************")

print("26.Which city has the highest number of customers?")
customers=pd.read_json("customers.json")
customers.to_csv("customers.csv")
# print(customers)
vk=customers.groupby("City")["CustomerID"].count()
vl= vk.sort_values(ascending=False).head(1)
print(vl)
subplot(2,3,5)
plt.scatter(vl.index,vl.values,color='olive')
plt.xlabel("City")
plt.ylabel("Customers")
plt.title("Which city has the highest number of customers")
for i in range(len(vl)):
    plt.text(vl.index[i],vl.values[i],str(vl.values[i]))
# plt.show()
print("*****************************************************")

print("27.Average income per city?")
customers=pd.read_json("customers.json")
customers.to_csv("customers.csv")
# print(customers)

vvv=customers.groupby("City")["Income"].mean()
print(vvv)
subplot(2,3,6)
plt.barh(vvv.index,vvv.values,color='red')
plt.xlabel("income")
plt.ylabel("city")
plt.title("Average income per city?")
plt.show()
print("*****************************************************")

print("28.Top 5 highest income customers?")
customers=pd.read_json("customers.json")
customers.to_csv("customers.csv")
# print(customers)
aa=customers.sort_values("Income", ascending=False).head(5)
print(aa)
subplot(2,3,1)
plt.scatter(aa["CustomerID"],aa["Income"],color='red')
plt.xlabel("CustomerID")
plt.ylabel("Income")
plt.title("Top 5 highest income customers?")
# plt.show()
print("*****************************************************")

print("29.Total loan amount issued?")

Loans=pd.read_json("Loans.json")
Loans.to_csv("Loans.csv")
# print(Loans)

aa=Loans["Amount"].sum()
print(aa)

print("***************************************************")
print("30.Average loan amount per customer?")
Loans=pd.read_json("Loans.json")
Loans.to_csv("Loans.csv")
# print(Loans)

bb=Loans.groupby("CustomerID")["Amount"].mean()
print(bb)

subplot(2,3,2)
plt.bar(bb.index,bb.values,color='aquamarine')
plt.xlabel("CustomerID")
plt.xticks(rotation=90)
plt.ylabel("Amount")
plt.title("Average loan amount per customer?")
import matplotlib.ticker as ticker
plt.ticklabel_format(style='plain', axis='y')

# plt.show()
print("***************************************************")

print("31.Loan amount by loan type?")
Loans=pd.read_json("Loans.json")
Loans.to_csv("Loans.csv")
# print(Loans)

cc=Loans.groupby("Type")["Amount"].sum()
print(cc)
subplot(2,3,3)
plt.barh(cc.index,cc.values,color='gold')
plt.xlabel("amount")
plt.ylabel("Type")
plt.title("Loan amount by loan type?")


from matplotlib.ticker import ScalarFormatter

ax = plt.gca()
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.ticklabel_format(style='plain', axis='x')


# plt.show()

print("***************************************************")

print("32.Identify customers with the highest loan amount?")
Loans=pd.read_json("Loans.json")
Loans.to_csv("Loans.csv")
# print(Loans)

dd=Loans.groupby("CustomerID")["Amount"].sum()
ee=dd.sort_values(ascending=False).head(1)
print(ee)

subplot(2,3,4)
plt.scatter(ee.index,ee.values,color='green')
plt.xlabel("CustomerID")
plt.ylabel("Amount")
plt.title("Identify customers with the highest loan amount?")
for i in range(len(ee.index)):
    plt.text(ee.index[i],ee.values[i],str(ee.values[i]))

import matplotlib.ticker as ticker
plt.ticklabel_format(style='plain', axis='y')

# plt.show()

print("***************************************************")

print("33.Which type of loan has the highest amount?")
Loans=pd.read_json("Loans.json")
Loans.to_csv("Loans.csv")
# print(Loans)

ff=Loans.groupby("Type")["Amount"].sum()
gg=ff.sort_values(ascending=False).head(1)
print(gg)
subplot(2,3,5)
plt.scatter(gg.index,gg.values,color='brown')
plt.xlabel("Type")
plt.ylabel("Amount")
plt.title("Which type of loan has the highest amount?")
for i in range(len(gg.index)):
    plt.text(gg.index[i],gg.values[i],str(gg.values[i]))
import matplotlib.ticker as ticker
plt.ticklabel_format(style='plain', axis='y')

# plt.show()
print("***************************************************")

print("34.which customers have personal loans")
Loans=pd.read_json("Loans.json")
Loans.to_csv("Loans.csv")
# print(Loans)

hh=Loans[Loans["Type"]=="Personal"]
print(hh)

subplot(2,3,6)
plt.bar(hh["CustomerID"],hh["Amount"],color='orchid')
plt.xlabel("Type")
plt.ylabel("Amount")
plt.title("Which customers have personal loans?")
plt.show()


print("*******************************************")
print("35.Total number of transactions?")
transactions=pd.read_json("transactions.json")
transactions.to_csv("transactions.csv")
# print(transactions)
aa=transactions['TxnID'].count()
print(aa)

print("*******************************************")

print("36.Total credit vs debit amount?")
transactions=pd.read_json("transactions.json")
transactions.to_csv("transactions.csv")
# print(transactions)

bb=transactions[transactions['Type']=='Credit']["Amount"].sum()
cc=transactions[transactions['Type']=='Debit']["Amount"].sum()
print(f"Total credit-{bb} vs Total debit-{cc}")
subplot(2,3,1)
plt.bar(["Credit", "Debit"], [bb, cc],color='gold')
plt.xlabel("Transaction Type")
plt.ylabel("Total Amount")
plt.title("Total Credit vs Debit Amount")
# plt.show()

print("*******************************************")

print("37.Average transaction amount?")
dd=transactions["Amount"].mean()
print(dd)
print("*******************************************")

print("38.Highest transaction amount?")
transactions=pd.read_json("transactions.json")
transactions.to_csv("transactions.csv")
# print(transactions)

ee=transactions["Amount"].max()
vj=transactions[transactions["Amount"]==ee]
vjj=vj[['Amount','AccountID']]

subplot(2,3,3)
plt.bar(vjj["AccountID"],vjj["Amount"],color='silver')
plt.xlabel("AccountID")
plt.ylabel("Amount")
plt.title("Highest transaction amount?")
# plt.show()
print("*******************************************")

print("39.Number of transactions per account?")
transactions=pd.read_json("transactions.json")
transactions.to_csv("transactions.csv")
# print(transactions)

ff=transactions.groupby('AccountID')["TxnID"].count()
print(ff)
print("*******************************************")

print("40. Customers who have both Investments and Loans")

investments=pd.read_json("investments.json")
investments.to_csv("investments.csv")
# print(investments)
customers=pd.read_json("customers.json")
customers.to_csv("customers.csv")
Loans=pd.read_json("Loans.json")
Loans.to_csv("Loans.csv")

kk=pd.merge(customers,Loans,on='CustomerID')
dd=pd.merge(investments,kk,on='CustomerID')
# print(dd)



# p=dd.groupby('CustomerID')[["InvestmentID",'LoanID']].sum()
# print(p)
# subplot(2,3,3)
# plt.bar(p.index,p.values,color='red')
# plt.xlabel("CustomerID")
# plt.ylabel("InvestmentID")
# plt.title("customer have Investments and LoanID?")
# plt.show()
print("*******************************************")

print("41.High Loan + Low Credit Score")

Loans=pd.read_json("Loans.json")
Loans.to_csv("Loans.csv")
# print(Loans)

credit_score=pd.read_json("credit score.json")
credit_score.to_csv("credit score.csv")
# print(credit_score)

f=pd.merge(Loans,credit_score,on='CustomerID')
print(f)
kk=f[(f['Amount']>300000)&(f['Score']<650)]
print(kk)

print("*******************************************")

print("*******************************************")

print("42.Amount per Customer")

accounts=pd.read_json("accounts.json")
accounts.to_csv("accounts.csv")
# print(accounts)

transactions=pd.read_json("transactions.json")
transactions.to_csv("transactions.csv")
# print(transactions)

ab=pd.merge(accounts, transactions, on="AccountID")

abb=ab.groupby('CustomerID')['Amount'].sum()
subplot(2,3,4)
plt.barh(abb.index,abb,color='red')
plt.xlabel("CustomerID")
plt.ylabel("Amount")
plt.title("Amount per Customer")
# plt.show()

print("*******************************************")

print("43.Investment Preference by City")
bb= pd.merge(customers, investments, on="CustomerID")

bbb=bb.groupby(["City", "Type"])["Amount"].sum()
print(bbb)
# subplot(2,3,5)
# plt.bar(bbb.index,bbb.values,color='red')
# plt.xlabel("CustomerID")
# plt.ylabel("Amount")
# plt.title("Investment Preference by City")
# # plt.show()


print("*******************************************")

print("44.Credit Score vs Total Balance")
dd= pd.merge(credit_score,accounts,on="CustomerID")
credit=dd.groupby("CustomerID")["Score"].mean()
balance=dd.groupby("CustomerID")["Balance"].sum()
ee=pd.merge(credit,balance,on="CustomerID")
print(ee)

print("*******************************************")


print("*******************************************")

print("45.Customers with Multiple Account Types")
tt = accounts.groupby("CustomerID")["Type"].count()
print(tt[tt > 1])

print("*******************************************")

print("46.Accounts wise Debit and Credit")
mm=transactions[['AccountID','Type','Amount']]
print(mm)

print("*******************************************")

print("47.Customers with High Transactions but Low Balance")
hh=pd.merge(transactions,accounts,on="AccountID")

t=hh.groupby("CustomerID")["TxnID"].count()
b=hh.groupby("CustomerID")["Balance"].sum()

pp=pd.merge(t,b,on="CustomerID")
print(pp)
print(pp[(pp["TxnID"]>5)&(pp["Balance"]<50000)])

print("*******************************************")

print("*******************************************")

print("48.Young Customers (<30) with High Investments")
v=pd.merge(customers, investments, on="CustomerID")

vk = v[v["Age"] < 30]
print(vk.groupby(["CustomerID","Age"])["Amount"].sum().sort_values(ascending=False))

print("*******************************************")

print("49.Senior Customers (50+) with Loans")
o=pd.merge(customers, Loans, on="CustomerID")
print(o[o["Age"] >= 50])

print("*******************************************")

print("50.High Income but Low Credit Score")
df=pd.merge(customers, credit, on="CustomerID")

h=df[(df["Income"]>50000)&(df["Score"]<650)]
print(h)

print("*******************************************")

print("51.Loan-Free Customers")

pp=pd.merge(customers, Loans, on="CustomerID")
# print(pp)
jj=pp.groupby("CustomerID")["Amount"].sum()
l=pp[pp["Amount"]==0]
print(l)

print("*******************************************")

print("52.Investors (Multiple Investment Types)")
i=investments.groupby("CustomerID")["Type"].count()
print(i[i>1])

print("*******************************************")

print("53.Investment-to-Income Ratio")
invested=pd.merge(customers,investments,on="CustomerID")
invested["InvIncomeRatio"]=invested["Amount"]/invested["Income"]
print(invested)

print("*******************************************")

print("*******************************************")

print("54.High Credit Score but No Investments")
invest=pd.merge(credit,investments,on="CustomerID",how="left")

print(invest[(invest["Score"]>750)&(invest["Amount"].isnull())])

print("*******************************************")

print("*******************************************")

print("55.Top 5 Most Active Cities (Transactions)")
transactions=pd.read_json("transactions.json")
transactions.to_csv("transactions.csv")
# print(transactions)

accounts=pd.read_json("accounts.json")
accounts.to_csv("accounts.csv")
# print(accounts)

txn_city = pd.merge(accounts, customers, on="CustomerID")
tttt=pd.merge(txn_city,transactions,on="AccountID")
tv=tttt.groupby("City")["TxnID"].count()
tvv=tv.sort_values(ascending=False).head(5)
print(tvv)

subplot(2,3,6)
plt.plot(tv.index,tv.values,color="red")
plt.xlabel("City")
plt.xticks(rotation=90)
plt.ylabel("Transactions")
plt.title("Top 5 most active cities")
plt.show()

print("*******************************************")

print("56.Loan Burden vs Balance")
ss=pd.merge(customers,accounts,on="CustomerID")
s=pd.merge(ss,Loans,on="CustomerID")

print(s.groupby("CustomerID")[["Amount","Balance"]].sum())

print("*******************************************")
print("**************************************")

print("57.Total investment amount?")
bb=investments['Amount'].sum()
print(bb)


print("*******************************************")

print("58.Total number of personal loans issued")
Loans=pd.read_json("Loans.json")
Loans.to_csv("Loans.csv")
# print(Loans)

hh=Loans[Loans["Type"]=="Personal"]["LoanID"].count()
print(hh)
print("***************************************************")














































