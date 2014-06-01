class LyricMixin(object):

    # TODO: default_y, elision
    
    @property
    def is_continued(self):
        if self.syllabic is not None:
            return self.syllabic[0] in ('begin', 'middle')

    @property
    def is_extended(self):
        return self.extend_ is not None

    @property
    def extension(self):
        extension = ''
        if self.is_continued:
            extension = '--'
        if self.is_extended:
            extension = '__'
        return extension

    @property
    def lyric_text(self):
        # TODO: catch non-ascii characters and encode them
        # return self.text[:][0].value().encode('utf-8')
        return 'Lo'
    
    @property
    def lilypond_format(self):
        return '"{}"{}'.format(self.lyric_text, self.extension)


