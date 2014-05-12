class CreditMixin(object):

    @property
    def template(self):
        return '{type_} = "{text}"'

    @property
    def lily_credit_type(self):
        try:
            return self.credit_type[:][0]
        except:
            return None

    @property
    def lily_credit_words(self):
        try:
            return self.credit_words[:][0].value()
        except:
            return None

    @property
    def lilypond_format(self):
        return self.template.format(
            type_ = self.lily_credit_type,
            text = self.lily_credit_words,
            ) 

