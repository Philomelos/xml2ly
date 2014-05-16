class WedgeMixin(object):

    xml_to_lily_mapping = {
        'crescendo': r'\<',
        'decrescendo': r'\>',
        'diminuendo': r'\>',
        'stop': 's1*0\!',
        # 'stop': '\!',
        }

    @property
    def before_note(self):
        return None

    @property
    def wedge_type(self):
        return self.xml_to_lily_mapping.get(self.type, None)

    @property
    def after_note(self):
        command = self.wedge_type
        if command:
            return command

     
    
