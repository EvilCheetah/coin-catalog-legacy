from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()


class Membership(models.Model):
    """
    This table holds the membership plan that user has

    Plans:
        BASIC PLAN    - Default, non-paid, plan that gives the access
                        to the website.
        ADVANCED PLAN - A paid plan, that includes gives the access
                        to all coins(including rare coins) and price
                        history.
        BUSINESS PLAN - A paid plan, that provides a set of tools
                        for other developers. Gives readonly access
                        for models and full-info models.
        STAFF PLAN    - all staff members, admins and superuser(-s)
                        have this membership by default. All staff plan
                        members have the access to all information.

    Model Variables:
        account                - Extension of Account Model
        stripe_id              - Subscription Pricing Plan ID
        stripe_subscription_id - Unique subscription ID
        cancel_at_period_end   - Boolean Value, used for canceling the subscription
                                 plan at the end of the period
        membership_plan_type   - Holds the value of user membership type
    """
    PLAN = [
        (1, 'Basic'),
        (2, 'Advanced'),
        (3, 'Business'),
        (4, 'Staff')
    ]

    account                = models.OneToOneField(USER, on_delete = models.CASCADE)
    stripe_id              = models.CharField(max_length = 255)
    stripe_subscription_id = models.CharField(max_length = 255)
    cancel_at_period_end   = models.BooleanField(default = False)
    membership_plan_type   = models.IntegerField(
        choices = Plan.choices,
        default = 1
    )

    class Meta:
        db_table = 'membership'
