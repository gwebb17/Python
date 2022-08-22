from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction
# Create your views here.

#this will render Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account'] #if form is submitted retrieve the desired account
        return balance(request, pk) #call balance to render balance sheet
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)

#this will render Create New Account page
def create_account(request):
    form = AccountForm(data=request.POST or None) #retrieve account form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index') #returns user to home page
    content = {'form': form} #saves template as dictionary
    return render(request, 'checkbook/CreateNewAccount.html', content)

#this will render Balance page
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) #retrieve requested account using pk
    transactions = Transaction.Transactions.filter(account=pk)
    current_total = account.initial_deposit
    table_contents = {} #create dictionary where transaction info will be placed
    for t in transactions: #loop through transactions and determine which is deposit and withdrawal
        if t.type == 'Deposit':
            current_total += t.amount #if despoit add amount to balance
            table_contents.update({t: current_total}) #add transaction and total to dictionary
        else:
            current_total -= t.amount #if withdrawal subtract from balance
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

#this will render Transaction page
def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    #might need to be uncommented below
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
