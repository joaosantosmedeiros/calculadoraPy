class EmprestimoCalculator:
    @staticmethod
    def calcular_limite_parcela(renda):
        return 0.3 * renda

    @staticmethod
    def calcular_pagamento_mensal(valor, numero_pagamentos):
        taxa_juros_mensal = 12 / 12 / 100
        return (taxa_juros_mensal * valor) / (1 - (1 + taxa_juros_mensal)**(-numero_pagamentos))

    @staticmethod
    def calcular_valor_max_cedido(limite_parcela, taxa_juros_mensal, numero_pagamentos):
        return limite_parcela * (1 - (1 + taxa_juros_mensal)**(-numero_pagamentos)) / taxa_juros_mensal

    @staticmethod
    def aprovar_emprestimo(pagamento_mensal, limite_parcela):
        return pagamento_mensal <= limite_parcela
