{
    "name": "Gastos Simples",
    "version": "16.0.1.0.0",
    "author": "Ivan Arriola, Autodidacta TI",
    "category": "Account",
    "license": "AGPL-3",
    "depends": [
        "base",
        "mail",
        "product"
    ],
    "data": [
        "security/simple_expenses_label_security.xml",
        "security/ir.model.access.csv",
        "data/expense_sequence.xml",
        "views/manu_simple_expense.xml",
        "views/simple_expense_view.xml",
        "views/simple_expense_category_view.xml",
    ],
    "installable": True,
}
