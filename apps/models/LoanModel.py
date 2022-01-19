from apps.models import Model


class Loan(Model):
    __table__ = 'neon'
    __primary_key__ = 'loanid'
