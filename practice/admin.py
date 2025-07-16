from django.contrib import admin
from django import forms

from .models import Question, UserProgress, Topic, Skillset


class QuestionAdminForm(forms.ModelForm):
    """Custom form to select the correct option for multiple choice questions."""

    correct_choice = forms.ChoiceField(
        label="Correct answer",
        choices=[
            ("option_a", "A"),
            ("option_b", "B"),
            ("option_c", "C"),
            ("option_d", "D"),
        ],
        widget=forms.RadioSelect,
        required=False,
    )

    class Meta:
        model = Question
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Answer is optional at the model level but should be required only
        # for open questions. Always mark it non-required here and let the
        # clean() method enforce the rule based on the selected type.
        self.fields["answer"].required = False
        # Pre-select the correct option when editing an existing question
        instance = getattr(self, "instance", None)
        if instance and instance.pk and instance.type == Question.MULTIPLE_CHOICE:
            for opt in ["option_a", "option_b", "option_c", "option_d"]:
                if getattr(instance, opt) == instance.answer:
                    self.fields["correct_choice"].initial = opt
                    break

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("type") == Question.MULTIPLE_CHOICE:
            choice = cleaned.get("correct_choice")
            if not choice:
                raise forms.ValidationError("Select the correct answer option.")
            cleaned["answer"] = cleaned.get(choice)
        elif cleaned.get("type") == Question.OPEN:
            if not cleaned.get("answer"):
                raise forms.ValidationError("Answer is required for open questions.")
        return cleaned

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ("id", "skillset", "type")
    search_fields = ("skillset__name", "skillset__topic__name")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "topic_id", "name", "rank")
    ordering = ("rank",)


@admin.register(Skillset)
class SkillsetAdmin(admin.ModelAdmin):
    list_display = ("id", "skillset_id", "topic", "name", "rank")
    list_filter = ("topic",)
    ordering = ("topic", "rank")

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "correct", "attempts", "answered_at")
    search_fields = ("user__username",)
