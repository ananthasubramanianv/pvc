from flask import Flask, render_template, request, flash
from forms import PoldetailsForm

app = Flask(__name__)
app.secret_key = 'development key'

class Apol:
  bonus = 1000
  uplift = 40
  mfee = 3
  bdate = 1990

class Bpol:
  bonus = 1000
  uplift = 25
  mfee = 5
  bdate = 1990

class Cpol:
  bonus = 1000
  uplift = 10
  mfee = 7
  bdate = 1990

def polval(polnum):
    if polnum.startswith(('a', 'A')):
        pol = Apol()
    elif polnum.startswith(('b', 'B')):
        pol = Bpol()
    elif polnum.startswith(('c', 'C')):
        pol = Cpol()
    else:
        pol = 'invalid'
    return pol

def bonuschk(polnum, poldat, membership, pol):
    x = poldat.split("-")
    chkdt = int(x[0])
    if ((polnum[0] == "A" or polnum[0] == "a") and chkdt < pol.bdate) or \
       ((polnum[0] == "B" or polnum[0] == "b") and membership == 'Y') or \
       ((polnum[0] == "C" or polnum[0] == "c") and chkdt >= pol.bdate and membership == 'Y'):
        bonaprv = "Y"
    else:
        bonaprv = "N"
    return bonaprv

def matvalcalc(premium, pol, baprv):
    prem = float(premium)
    mgmtfee = (prem * pol.mfee)/100
    upliftval = (pol.uplift/100) + 1
    if baprv == "Y":
        matval = ((prem - mgmtfee) + pol.bonus) * upliftval
    else:
        matval = (prem - mgmtfee) * upliftval
    matvalfnl = round(matval,2)
    return matvalfnl

@app.route('/', methods=['GET', 'POST'])
def main():
    form = PoldetailsForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('Please check if all fields are filled correctly.')
            return render_template('index.html', form=form, value='?')
        else:
                polnum = request.form['polnum']
                premium = request.form['premium']
                poldat = request.form['poldat']
                membership = request.form['membership']
                pol = polval(polnum)
                if pol == 'invalid':
                    flash('Policy number invalid. Please check and try again.')
                    return render_template('index.html', form=form, value='?')
                else:
                    baprv = bonuschk(polnum, poldat, membership, pol)
                    matamt = matvalcalc(premium, pol, baprv)
                    return render_template('index.html', form=form, value=matamt)
    elif request.method == 'GET':
        return render_template('index.html', form=form, value='?')

if __name__ == '__main__':
    app.run()


