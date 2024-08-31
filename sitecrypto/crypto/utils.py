class FormMixin:
    """
    The form's title will be converted to lowercase.
    """
    def form_valid(self, form):
        form.instance.title = form.instance.title.lower()
        return super().form_valid(form)
