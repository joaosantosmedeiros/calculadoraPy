from flask import Flask, render_template, request
from emprestimo_calculator import EmprestimoCalculator

app = Flask(__name__)

def validar_dados(renda, valor, numero_pagamentos):
    if renda < 0 or valor < 100 or numero_pagamentos < 1 or numero_pagamentos > 96:
        return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        renda = float(request.form['renda'])
        valor = float(request.form['valor'])
        numero_pagamentos = float(request.form['tempo'])

        if not validar_dados(renda, valor, numero_pagamentos):
            return render_template('index.html', result=(False, 'Negado', ''))

        calculadora = EmprestimoCalculator()

        limite_parcela = calculadora.calcular_limite_parcela(renda)
        taxa_juros_mensal = 12 / 12 / 100

        pagamento_mensal = calculadora.calcular_pagamento_mensal(valor, numero_pagamentos)
        valor_max_cedido = calculadora.calcular_valor_max_cedido(limite_parcela, taxa_juros_mensal, numero_pagamentos)
        
        if calculadora.aprovar_emprestimo(pagamento_mensal, limite_parcela):
            result = True, 'Aprovado', f'{pagamento_mensal:.2f}', f'{pagamento_mensal * numero_pagamentos:.2f}'
        else:
            result = False, 'Negado', f'{valor_max_cedido:.2f}'
        
        return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
