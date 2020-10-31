from django.db import models
from accounts.models import Account


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
    class Plan(models.IntegerChoices):
        """
        Enum Class for Different memberships
        """
        BASIC    = 1
        ADVANCED = 2
        BUSINESS = 3
        STAFF    = 4

    account                = models.OneToOneField(Account, on_delete = models.CASCADE)
    stripe_id              = models.CharField(max_length = 255)
    stripe_subscription_id = models.CharField(max_length = 255)
    cancel_at_period_end   = models.BooleanField(default = False)
    membership_plan_type   = models.IntegerField(
        choices = Plan.choices,
        default = Plan.BASIC
    )

    class Meta:
        db_table = 'membership'
