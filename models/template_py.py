from odoo import models, _

class L10nPyTemplates(models.AbstractModel):
    _name = 'l10n_py.templates'
    _inherit = 'account.chart.template'

    def _get_py_template_data(self):
        return {
            'name': _('Base'),
            'visible': False,
            'code_digits': '6',
            'property_account_receivable_id': 'a400',
            'property_account_payable_id': 'a440',
            'property_account_expense_categ_id': 'a600',
            'property_account_income_categ_id': 'a700',
        }

    def _get_py_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.py',
                'bank_account_code_prefix': '550',
                'cash_account_code_prefix': '570',
                'transfer_account_code_prefix': '580',
                'account_default_pos_receivable_account_id': 'a401',
                'income_currency_exchange_account_id': 'a754',
                'expense_currency_exchange_account_id': 'a654',
                'account_journal_suspense_account_id': 'a499',
                'account_sale_tax_id': 'attn_VAT-OUT-10',
                'account_purchase_tax_id': 'attn_VAT-IN-10',
                'transfer_account_id': 'a580',
            },
        }

    def _get_py_account_journal(self):
        return {
            'sale': {'refund_sequence': True},
            'purchase': {'refund_sequence': True},
        }
