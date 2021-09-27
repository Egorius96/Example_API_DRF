from django.db import models


class Messages(models.Model):

    POSSITION_CHOISES = (
        ("EXPECTATION", "Expectation"),
        ("DONE", "Done"),
    )

    message = models.CharField(max_length=250)
    created = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=POSSITION_CHOISES)
